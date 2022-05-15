from peapy2.component import Component
from peapy2.exceptions import ComponentDoesNotExist
from peapy2.__pygame import pygame


FROM_TRANSFORM = -2
FROM_IMAGE = -1


class ImageRenderer(Component):
    """
    Component to render images in the window
    """

    NAME = "ImageRenderer"

    def __init__(self, path: str, width: int = -1, height: int = -1):
        """
        Construct a ImageRenderer.

        :param path: Path to the image to render
        :type path: str
        :param width: Width the image should be displayed in. Use -2 to set the width to the width of the parent's
                      GameObject's Transform. Use -1 to set the width to the width of the image
        :type width: int
        :param height: Height the image should be displayed in. Use -2 to set the height to the height of the parent's
                       GameObject's Transform. Use -1 to set the height to the height of the image
        :type height: int
        """
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

        self.peapy.window.screen.blit(
            image, self.peapy[self.parent_name].get_component("Transform").top_left
        )

    # Called when the component is destroyed
    def destroy(self):
        pass
