"""Specialized exceptions for the database client."""


class NegativeIntegerError(ValueError):
    """Exception for illegal negative integer values

    Args:
      value (int): The offending value.

    Attributes:
      msg (str): Human readable string describing the exception and
        displaying the offending value

    """
    def __init__(self, value):
        self.msg = 'Illegal value for `start` argument: %i. \
                    Cannot be negative' % value
