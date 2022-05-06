class ObjectAlreadyExists(Exception):
    """Raised when trying to create an object that already exists."""


class ObjectDoesNotExist(Exception):
    """Raised when trying to access an object that does not exist."""


class ComponentAlreadyExists(Exception):
    """Raised when trying to create a component that already exists."""


class ComponentDoesNotExist(Exception):
    """Raised when trying to access a component that does not exist."""
