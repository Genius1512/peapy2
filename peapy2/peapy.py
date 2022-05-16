from peapy2.color import Color
from peapy2 import exceptions
from peapy2.game_object import GameObject
from peapy2.window import Window


class PeaPy:
    def __init__(
            self, title, width, height, background_color=Color(0, 0, 0),
    ):
        """
        Construct a PeaPy object.

        :param title: Title of the window
        :type title: str
        :param width: Width of the window
        :type width: int
        :param height: Height of the window
        :type height: int
        :param background_color: Color of the window
        :type background_color: Color
        """
        self.title = title
        self.width = width
        self.height = height
        self.background_color = background_color

        self.window = Window(self.width, self.height, title)

        self.objects: dict[str, GameObject] = {}
        self.should_delete: list[str] = []

    def update(self) -> bool:
        """
        Update the game.

        :return: True if the game should continue, False if the window should close.
        """
        self.window.screen.fill(self.background_color.rgba)

        for name in self.should_delete:
            if name not in self.objects:
                raise exceptions.ObjectDoesNotExist(name)

            self.objects[name].destroy_()
            del self.objects[name]

        self.should_delete = []

        for obj in self.objects.values():
            obj.update_()

        return self.window.update()

    def add_object(self, obj: GameObject) -> GameObject:
        """
        Add the given GameObject to the PeaPy object.

        :param obj: The GameObject to add.
        :type obj: peapy2.GameObject
        :return: The given GameObject. This allows for this syntax: game_object = game.add_object(peapy2.GameObject())
        """
        if not isinstance(obj, GameObject):
            raise TypeError(f"Expected type peapy2.GameObject, got {type(obj)}")

        if obj.name in self.objects:
            raise exceptions.ObjectAlreadyExists(obj.name)

        self.objects[obj.name] = obj
        self.objects[obj.name].init_(self)
        return self.objects[obj.name]

    def get_object(self, name) -> GameObject:
        """
        Get a GameObject with the given name. Raises an exception when the GameObject is not found.

        :param name: The name of the GameObject.
        :type name: str
        :return: The GameObject with the given name.
        """
        if name not in self.objects:
            raise exceptions.ObjectDoesNotExist(name)

        return self.objects[name]

    def get_objects(self) -> dict[str, GameObject]:
        """
        Get a dictionary of all GameObjects.

        :return: A dictionary with all GameObjects.
        """
        return self.objects

    def remove_object(self, name) -> None:
        """
        Remove the GameObject with the given name.

        :param name: The name of the GameObject
        :type name: str
        """
        self.should_delete.append(name)

    def tree(self) -> str:
        """
        Get a tree representation of the PeaPy object.

        :return: A tree representation of the PeaPy object.
        """
        out = f"{self.title}\n"
        for obj in self.objects.values():
            out += f"\t{obj.name}\n"
            for component in obj.get_components().values():
                out += f"\t\t{component.NAME}\n"
        return out

    def __getattr__(self, item):
        return self.get_object(item)

    def __getitem__(self, item) -> GameObject:
        return self.get_object(item)

    def __repr__(self) -> str:
        return f"peapy2.PeaPy({self.title})"
