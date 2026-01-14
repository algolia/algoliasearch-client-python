# PYTHON CLIENT - AI AGENT INSTRUCTIONS

## ⚠️ CRITICAL: CHECK YOUR REPOSITORY FIRST

Before making ANY changes, verify you're in the correct repository:

```bash
git remote -v
```

- ✅ **CORRECT**: `origin .../algolia/api-clients-automation.git` → You may proceed
- ❌ **WRONG**: `origin .../algolia/algoliasearch-client-python.git` → STOP! This is the PUBLIC repository

**If you're in `algoliasearch-client-python`**: Do NOT make changes here. All changes must go through `api-clients-automation`. PRs and commits made directly to the public repo will be discarded on next release.

## ⚠️ BEFORE ANY EDIT: Check If File Is Generated

Before editing ANY file, verify it's hand-written by checking `config/generation.config.mjs`:

```javascript
// In generation.config.mjs - patterns WITHOUT '!' are GENERATED (do not edit)
'clients/algoliasearch-client-python/algoliasearch/**',              // Generated
'!clients/algoliasearch-client-python/algoliasearch/http/**',        // Hand-written ✓
```

**Hand-written (safe to edit):**

- `algoliasearch/http/**` - HTTP transport, retry logic, exceptions
- `algoliasearch/py.typed` - Type marker

**Generated (DO NOT EDIT):**

- `algoliasearch/{client}/` directories (search, insights, etc.)
- `algoliasearch/{client}/models/` - API models
- `algoliasearch/{client}/client.py` - API clients
- `pyproject.toml`, `poetry.lock`, `requirements.txt`

## Language Conventions

### Naming

- **Files**: `snake_case.py`
- **Variables/Functions**: `snake_case`
- **Classes**: `PascalCase`
- **Constants**: `UPPER_SNAKE_CASE`
- **Private**: `_leading_underscore`

### Formatting

- Ruff for linting (line-length: 88)
- Pyright for type checking
- Run formatting via CLI: `yarn cli format python clients/algoliasearch-client-python`

### Type Hints

- Full type hints required (Python 3.8+ style)
- Use `Optional[T]` for nullable, `Union[A, B]` for unions
- Use `List`, `Dict` from `typing` module (not built-in generics for 3.8 compat)

### Dependencies

- **HTTP**: `aiohttp` for async requests
- **Async timeout**: `async-timeout`
- **Build**: Poetry
- **Types**: Pydantic for models

## Client Patterns

### Transporter Architecture

```python
# Core transport in algoliasearch/http/
class Transporter(BaseTransporter):
    def __init__(self, config: BaseConfig):
        self._session: Optional[ClientSession] = None
        self._retry_strategy = RetryStrategy()

    async def request(self, verb, path, request_options, use_read_transporter):
        # Retry logic with host failover
```

### Async-First Design

- All API methods are `async def`
- Must run in asyncio event loop
- Use `async with` for client lifecycle

```python
async with SearchClient("APP_ID", "API_KEY") as client:
    response = await client.search(...)
```

### Retry Strategy

- `RetryOutcome`: `SUCCESS`, `RETRY`, `FAILURE`
- Host states: `UP`, `DOWN`, `TIMED_OUT`
- Exponential backoff on timeouts

### Exception Hierarchy

```python
# algoliasearch/http/exceptions.py
AlgoliaException              # Base
├── RequestException          # Request failed
├── AlgoliaUnreachableHostException  # All hosts failed
└── AlgoliaApiException       # API error response
```

## Common Gotchas

### Async Context Required

```python
# WRONG - won't work outside async context
response = client.search(...)

# CORRECT
response = await client.search(...)

# Or use asyncio.run() for scripts
import asyncio
asyncio.run(main())
```

### Session Lifecycle

```python
# Always close the client or use context manager
client = SearchClient("APP_ID", "API_KEY")
try:
    await client.search(...)
finally:
    await client.close()

# Or prefer context manager
async with SearchClient("APP_ID", "API_KEY") as client:
    await client.search(...)
```

### Type Narrowing

```python
# Use isinstance for union types
from algoliasearch.search.models import Hit

if isinstance(result, Hit):
    print(result.object_id)
```

### Python Version Compatibility

- Support Python 3.8 - 3.12
- Avoid walrus operator `:=` (3.8 has issues)
- Use `typing` module generics, not built-in `list[T]`

## Build & Test Commands

```bash
# From repo root (api-clients-automation)
yarn cli build clients python                  # Build Python client
yarn cli cts generate python                   # Generate CTS tests
yarn cli cts run python                        # Run CTS tests
yarn cli playground python search              # Interactive playground
yarn cli format python clients/algoliasearch-client-python

# From client directory (requires Poetry)
cd clients/algoliasearch-client-python
poetry install                                 # Install dependencies
poetry run pytest                              # Run tests
poetry run pyright                             # Type check
```
