"""WHATWG-compliant Server-Sent Events parser.

Three-layer architecture:
  Layer 1: _iter_lines / _aiter_lines — byte stream to text lines
  Layer 2: SSEDecoder — text lines to ServerSentEvent objects
  Layer 3: iter_sse_events / aiter_sse_events — top-level composers

Reference: https://html.spec.whatwg.org/multipage/server-sent-events.html#event-stream-interpretation
"""

import codecs
from dataclasses import dataclass
from typing import (
    Any,
    AsyncIterable,
    AsyncIterator,
    Dict,
    Generic,
    Iterable,
    Iterator,
    List,
    Optional,
)

from typing_extensions import TypeVar

_MAX_LINE_SIZE = 10 * 1024 * 1024  # 10 MB
_BOM = "\ufeff"

T = TypeVar("T", default=Dict[str, Any])


@dataclass
class ServerSentEvent:
    """A single SSE event dispatched from the event stream."""

    data: str
    event: str
    id: Optional[str] = None
    retry: Optional[int] = None


@dataclass
class StreamEvent(Generic[T]):
    """Wrapper for a parsed SSE event yielded by the typed ``*_stream`` methods.

    ``data`` is the deserialized payload when parsing succeeds, ``None`` otherwise.
    ``raw`` is the original :class:`ServerSentEvent` (always present).
    ``error`` is set when JSON parsing / deserialization of ``event.data`` failed.
    """

    data: Optional[T]
    raw: ServerSentEvent
    error: Optional[Exception] = None


# ---------------------------------------------------------------------------
# Layer 2 — SSEDecoder (shared between sync and async)
# ---------------------------------------------------------------------------


class SSEDecoder:
    """Decodes text lines into ServerSentEvent objects per the WHATWG spec.

    Feed lines one at a time via :meth:`decode`. A blank line triggers event
    dispatch if the data buffer is non-empty. ``_last_event_id`` persists
    across dispatches; ``_event_type`` resets to ``""`` after each dispatch.
    """

    def __init__(self) -> None:
        self._data: List[str] = []
        self._event_type: str = ""
        self._last_event_id: Optional[str] = None
        self._retry: Optional[int] = None

    def decode(self, line: str) -> Optional[ServerSentEvent]:
        """Process a single line. Returns a :class:`ServerSentEvent` on
        dispatch (blank line with non-empty data buffer), or ``None``."""

        # Blank line → dispatch if data buffer is non-empty
        if not line:
            # eventType resets on EVERY blank line per WHATWG spec,
            # regardless of whether we actually dispatch an event
            current_event_type = self._event_type
            self._event_type = ""

            if not self._data:
                return None

            event = ServerSentEvent(
                data="\n".join(self._data),
                event=current_event_type,
                id=self._last_event_id,
                retry=self._retry,
            )

            # Reset per WHATWG spec — _last_event_id and _retry persist
            self._data = []

            return event

        # Comment line (starts with ':')
        if line.startswith(":"):
            return None

        # Field line
        if ":" in line:
            field, _, value = line.partition(":")
            # Strip exactly one leading space if present
            if value.startswith(" "):
                value = value[1:]
        else:
            field = line
            value = ""

        if field == "data":
            self._data.append(value)
        elif field == "event":
            self._event_type = value
        elif field == "id":
            # If the value contains a NULL character, ignore the field entirely
            if "\x00" not in value:
                self._last_event_id = value
        elif field == "retry":
            # Only accept if value is non-empty and consists entirely of
            # ASCII digits. Do NOT use int() directly — it accepts negatives,
            # whitespace, underscores, etc.
            if value and value.isdigit():
                self._retry = int(value)

        return None


# ---------------------------------------------------------------------------
# Layer 1 — Line iterators (byte stream → text lines)
# ---------------------------------------------------------------------------


def _iter_lines(byte_iter: Iterable[bytes]) -> Iterator[str]:
    """Decode a byte stream into individual text lines.

    Handles ``\\r``, ``\\n``, and ``\\r\\n`` line endings including the edge
    case where ``\\r\\n`` is split across two chunks. Strips the BOM from the
    very first line only. Raises :class:`ValueError` if the internal buffer
    exceeds 10 MB.
    """
    decoder = codecs.getincrementaldecoder("utf-8")()
    buf = ""
    trailing_cr = False
    first_line = True

    for raw_chunk in byte_iter:
        chunk = decoder.decode(raw_chunk)

        if not chunk:
            continue

        # Handle \r\n split across chunk boundary
        if trailing_cr:
            if chunk[0] == "\n":
                chunk = chunk[1:]
            trailing_cr = False
            if not chunk:
                continue

        # Track trailing \r for next chunk's \r\n check
        if chunk[-1] == "\r":
            trailing_cr = True

        # Normalize all line endings to \n, then split
        lines = chunk.replace("\r\n", "\n").replace("\r", "\n").split("\n")

        # First segment extends the buffer; remaining segments are after
        # line breaks (i.e. the buffer holds a complete line).
        buf += lines[0]

        for i in range(1, len(lines)):
            line = buf
            if first_line:
                if line.startswith(_BOM):
                    line = line[1:]
                first_line = False
            yield line
            buf = lines[i]

        if len(buf) > _MAX_LINE_SIZE:
            raise ValueError("SSE line exceeds maximum buffer size of 10 MB")

    # Flush the incremental UTF-8 decoder
    remaining = decoder.decode(b"", final=True)
    if remaining:
        buf += remaining

    # At end-of-stream with trailing_cr the \r already caused a line split,
    # so only yield if buf accumulated content after that split.
    if trailing_cr:
        if buf:
            line = buf
            if first_line:
                if line.startswith(_BOM):
                    line = line[1:]
            yield line
        return

    if buf:
        line = buf
        if first_line:
            if line.startswith(_BOM):
                line = line[1:]
        yield line


async def _aiter_lines(byte_iter: AsyncIterable[bytes]) -> AsyncIterator[str]:
    """Async variant of :func:`_iter_lines`."""
    decoder = codecs.getincrementaldecoder("utf-8")()
    buf = ""
    trailing_cr = False
    first_line = True

    async for raw_chunk in byte_iter:
        chunk = decoder.decode(raw_chunk)

        if not chunk:
            continue

        if trailing_cr:
            if chunk[0] == "\n":
                chunk = chunk[1:]
            trailing_cr = False
            if not chunk:
                continue

        if chunk[-1] == "\r":
            trailing_cr = True

        lines = chunk.replace("\r\n", "\n").replace("\r", "\n").split("\n")

        buf += lines[0]

        for i in range(1, len(lines)):
            line = buf
            if first_line:
                if line.startswith(_BOM):
                    line = line[1:]
                first_line = False
            yield line
            buf = lines[i]

        if len(buf) > _MAX_LINE_SIZE:
            raise ValueError("SSE line exceeds maximum buffer size of 10 MB")

    remaining = decoder.decode(b"", final=True)
    if remaining:
        buf += remaining

    if trailing_cr:
        if buf:
            line = buf
            if first_line:
                if line.startswith(_BOM):
                    line = line[1:]
            yield line
        return

    if buf:
        line = buf
        if first_line:
            if line.startswith(_BOM):
                line = line[1:]
        yield line


# ---------------------------------------------------------------------------
# Layer 3 — Top-level composers
# ---------------------------------------------------------------------------


def iter_sse_events(byte_iter: Iterable[bytes]) -> Iterator[ServerSentEvent]:
    """Parse a byte stream into SSE events (sync).

    Pipes bytes through :func:`_iter_lines` then feeds each line to
    :class:`SSEDecoder`, yielding every dispatched event.
    """
    decoder = SSEDecoder()
    for line in _iter_lines(byte_iter):
        event = decoder.decode(line)
        if event is not None:
            yield event


async def aiter_sse_events(
    byte_iter: AsyncIterable[bytes],
) -> AsyncIterator[ServerSentEvent]:
    """Parse a byte stream into SSE events (async).

    Async variant of :func:`iter_sse_events`.
    """
    decoder = SSEDecoder()
    async for line in _aiter_lines(byte_iter):
        event = decoder.decode(line)
        if event is not None:
            yield event
