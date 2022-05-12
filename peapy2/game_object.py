from peapy2.component import Component
from peapy2 import exceptions


class GameObject:
    def __init__(self, name: str):
        self.name = name

        self.peapy = None

        self.components: dict[str, Component] = {}

    def init_(self, peapy):
        self.peapy = peapy

        try:
            self.init()
        except AttributeError:
            pass

    def init(self):
        pass

    def update_(self):
        for component in self.components.values():
            component.update()

        try:
            self.update()
        except AttributeError:
            pass

    def update(self):
        pass

    def destroy_(self):
        for component in self.components.values():
            component.destroy_()
        try:
            self.destroy()
        except AttributeError:
            pass

    def destroy(self):
        pass

    def add_component(self, component: Component) -> Component:
        if type(component) != Component:
            raise TypeError(f"Expected type peapy2.Component, got {type(component)}")

        if component.NAME in self.components:
            raise exceptions.ComponentAlreadyExists(component.NAME)

        self.components[component.NAME] = component
        self.components[component.NAME].init_(self.peapy, self.name)
        return self.components[component.NAME]

    def get_component(self, name: str) -> Component:
        if name not in self.components:
            raise exceptions.ComponentDoesNotExist(name)

        return self.components[name]

    def get_components(self) -> dict[str, Component]:
        return self.components

    def remove_component(self, name: str) -> None:
        if name not in self.components:
            raise exceptions.ComponentDoesNotExist(name)

        self.components[name].destroy_()
        del self.components[name]

    def tree(self) -> str:
        out = f"\t{self.name}\n"
        for component in self.components.values():
            out += component.tree()
        return out

    def __getitem__(self, item) -> Component:
        return self.get_component(item)

    def __repr__(self) -> str:
        return f"peapy2.GameObject({self.name})"
