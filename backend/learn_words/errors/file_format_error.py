"""Defining a new exception called FileFormatError."""


class FileFormatError(Exception):
    """FileFormatError: Raised when intended and actual formats don't match."""

    def __init__(self, message: object) -> None:
        """
        __init__: Initializer function.

        Parameters
        ----------
        message : object
            Message that needs to be provided when the error is raised.
        """
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        """
        __str__: String representation of the error.

        Returns
        -------
        str
            The error message that needs to be displayed.
        """
        return f"{self.message}"
