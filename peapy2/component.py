class Component:
    """
    Component class to modify the behaviour of a GameObject
    """

    NAME = "Component"

    def __init__(self):
        """
        Construct a component
        """
        self.peapy = None
        self.parent_name = None

    def init_(self, peapy, parent_name: str):
        """
        Called when the component gets added to a GameObject.
        Don't overwrite this method (!), use the init() method instead

        :param peapy: The PeaPy object
        :param parent_name: The name of the parent GameObject
        """
        self.peapy = peapy
        self.parent_name = parent_name

        self.init()

    def init(self):
        """
        Called when the component gets added to a GameObject.
        Do things here that require the PeaPy object to be present
        """

    def update_(self):
        """
        Called when the Game gets updated.
        Don't overwrite this method (!), use the update() method instead
        """
        self.update()

    def update(self):
        """
        Called when the Game gets updated.
        """

    def destroy_(self):
        """
        Called when the parent GameObject gets destroyed, or the component gets destroyed.
        Don't overwrite this method (!), use the destroy() method instead
        """
        self.destroy()

    def destroy(self):
        """
        Called when the parent GameObject gets destroyed, or the component gets destroyed.
        """

    @property
    def game_object(self):
        """
        The parent GameObject
        :return: Object
        """
        return self.peapy[self.parent_name]

    def __repr__(self):
        return f"peapy2.Component({self.NAME})"
