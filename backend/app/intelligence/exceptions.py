class IntelligenceError(Exception):
    """Base exception for the Knowledge Intelligence Engine."""


class UnsupportedDomainError(IntelligenceError):
    """Raised when a knowledge item references an unsupported domain."""
