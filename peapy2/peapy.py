from peapy2 import exceptions
from peapy2.game_object import GameObject
from peapy2.window import Window


class PeaPy:
    def __init__(
        self, title: str, width: int, height: int, background_color: tuple = (0, 0, 0)
    ):
        self.title = title
        self.width = width
        self.height = height
        self.background_color = background_color

        self.window = Window(self.width, self.height, title)

        self.objects: dict[str, GameObject] = {}

    def update(self) -> bool:
        self.window.screen.fill(self.background_color)

        for obj in self.objects.values():
            obj.update_()

        return self.window.update()

    def add_object(self, obj: GameObject) -> GameObject:
        if not isinstance(obj, GameObject):
            raise TypeError(f"Expected type peapy2.GameObject, got {type(obj)}")

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

    def __getattr__(self, item):
        return self.get_object(item)

    def __getitem__(self, item) -> GameObject:
        return self.get_object(item)

    def __repr__(self) -> str:
        return f"peapy2.PeaPy({self.title})"
