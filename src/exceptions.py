"""Exceptions for this application."""


class Error(Exception):
    """Base class for exceptions."""

    pass


class InputError(Error):
    """Exception for errors in the input."""

    def __init__(self, expression, message):
        """Initialize the InputError."""
        self.expression = expression
        self.message = message
