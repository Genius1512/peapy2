from peapy2.component import Component
from peapy2.exceptions import ComponentDoesNotExist
from peapy2.__pygame import pygame


FROM_TRANSFORM = -2
FROM_IMAGE = -1


class ImageRenderer(Component):
    NAME = "ImageRenderer"

    def __init__(self, path: str, width: int = -1, height: int = -1):
        super().__init__()

        self.path = path
        self.width = width
        self.height = height

        self.is_visible = True
        self.image = None

    # Called when the component is created
    def init(self):
        self.image = pygame.image.load(self.path)

    # Called when the game gets updated
    def update(self):
        try:
            self.peapy[self.parent_name]["Transform"]
        except ComponentDoesNotExist:
            raise ComponentDoesNotExist("Image renderer requires a transform component")

        if not self.is_visible:
            return

        if self.width == FROM_TRANSFORM:
            width = self.peapy[self.parent_name].get_component("Transform").width

        elif self.width == FROM_IMAGE:
            width = self.image.get_width()

        else:
            width = self.width

        if self.height == FROM_TRANSFORM:
            height = self.peapy[self.parent_name].get_component("Transform").height

        elif self.height == FROM_IMAGE:
            height = self.image.get_height()

        else:
            height = self.height

        image = pygame.transform.scale(self.image, (width, height))

        self.peapy.window.screen.blit(image, self.peapy[self.parent_name].get_component("Transform").top_left)

    # Called when the component is destroyed
    def destroy(self):
        pass
