import warnings

warnings.filterwarnings(
    "ignore",
    category=ResourceWarning,
    message="unclosed.*<ssl.SSLSocket.*>"
)
