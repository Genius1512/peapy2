class PeaPyNotStarted(Exception):
    """Raised when the game is not started, but gets updated."""


class ObjectAlreadyExists(Exception):
    """Raised when trying to create an object that already exists."""


class ObjectDoesNotExist(Exception):
    """Raised when trying to access an object that does not exist."""


class ComponentAlreadyExists(Exception):
    """Raised when trying to create a component that already exists."""


class ComponentDoesNotExist(Exception):
    """Raised when trying to access a component that does not exist."""


class RequiredComponentDoesNotExist(Exception):
    """Raised when a component requires a component that does not exist."""
