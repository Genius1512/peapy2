from . import exceptions
from .game_object import GameObject
from .window import Window


class PeaPy:
    # TODO: Access objects as attributes
    def __init__(self, title: str):
        self.title = title

        self.window = Window(640, 480, title)

        self.objects: dict[str, GameObject] = {}

    def update(self) -> bool:
        for obj in self.objects.values():
            obj.update_()

        return self.window.update()

    def add_object(
            self, obj: GameObject
    ) -> GameObject:  # TODO: Check if type is game_object
        if obj.name in self.objects:
            raise exceptions.ObjectAlreadyExists(obj.name)

        self.objects[obj.name] = obj
        self.objects[obj.name].init_(self)
        return self.objects[obj.name]

    def get_object(self, name: str) -> GameObject:
        if name not in self.objects:
            raise exceptions.ObjectDoesNotExist(name)

        return self.objects[name]

    def get_objects(self) -> dict[str, GameObject]:
        return self.objects

    def remove_object(self, name: str) -> None:
        if name not in self.objects:
            raise exceptions.ObjectDoesNotExist(name)

        self.objects[name].destroy_()
        del self.objects[name]

    def tree(self) -> str:
        out = f"{self.title}\n"
        for obj in self.objects.values():
            out += f"{obj.tree()}\n"
        return out

    def quit(self):
        pass

    def __getitem__(self, item) -> GameObject:
        return self.get_object(item)

    def __repr__(self) -> str:
        return f"peapy2.PeaPy({self.title})"
