

class YouTubeAPIError(Exception):
    pass


class NoSelectionError(YouTubeAPIError):
    """Exception raised for errors in the input selection.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Select from the drop down menu, then try again!"):
        self.message = message
        super().__init__(self.message)


class APIError(YouTubeAPIError):
    """Exception raised for API errors.

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class NotFoundError(YouTubeAPIError):
    """Exception raised for not found errors.

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message="404 Not Found Error, Category may no longer exist!"):
        self.message = message
        super().__init__(self.message)
