from peapy2.component import Component
from peapy2 import exceptions


class GameObject:
    """
    GameObject class to be used in the PeaPy object.
    """

    def __init__(self, name):
        """
        Construct a GameObject

        :param name: The name of the GameObject.
        :type name: str
        """
        self.name = name

        self.peapy = None

        self.__components: dict[str, Component] = {}

    def init_(self, peapy):
        """
        Called when the GameObject gets added to a PeaPy object.
        Don't override this method (!), use the init() method instead

        :param peapy: The parent PeaPy object.
        :type peapy: peapy2.PeaPy
        """
        self.peapy = peapy

        self.init()

    def init(self):
        """
        Called when the GameObject gets added to a PeaPy object.
        Do things here that require the parent PeaPy object to be initialized.
        """

    def update_(self):
        """
        Called when the GameObject gets updated.
        Don't override this method (!), use the update() method instead
        """
        for component in self.__components.values():
            component.update_()

        self.update()

    def update(self):
        """
        Called when the GameObject gets updated.
        """

    def destroy_(self):
        """
        Called when the GameObject or the parent Peapy object gets destroyed.
        Don't override this method (!), use the destroy() method instead
        """
        for component in self.__components.values():
            component.destroy_()

        self.destroy()

    def destroy(self):
        """
        Called when the GameObject or the parent Peapy object gets destroyed.
        """

    def add_component(self, component: Component) -> Component:
        """
        Add the given component to the GameObject.
        The init() method of the component gets called.

        :param component: The component to add. :type component: peapy2.Component :return: The given component. This
                          allows for this syntax: component = game_object.add_component(peapy2.Component())
        """
        if not isinstance(component, Component):
            raise TypeError(f"Expected type peapy2.Component, got {type(component)}")

        if component.NAME in self.__components:
            raise exceptions.ComponentAlreadyExists(component.NAME)

        self.__components[component.NAME] = component
        self.__components[component.NAME].init_(self.peapy, self.name)
        return self.__components[component.NAME]

    def get_component(self, name: str) -> Component:
        """
        Get a component by it's name

        :param name: The name of the component.
        :type name: str
        :return: The component.
        """
        if name not in self.__components:
            raise exceptions.ComponentDoesNotExist(name)

        return self.__components[name]

    def get_components(self) -> dict[str, Component]:
        """
        Get a dictionary of all components.

        :return: A dictionary with all components.
        """
        return self.__components

    def remove_component(self, name: str):
        """
        Remove the component with the given name.

        :param name: The name of the component
        :type name: str
        """
        if name not in self.__components:
            raise exceptions.ComponentDoesNotExist(name)

        self.__components[name].destroy_()
        del self.__components[name]

    def __getitem__(self, item) -> Component:
        return self.get_component(item)

    def __repr__(self) -> str:
        return f"peapy2.GameObject({self.name})"
