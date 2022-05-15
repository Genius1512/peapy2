from peapy2.color import Color
from peapy2.component import Component
from peapy2.__pygame import pygame


class ShapeRenderer(Component):
    """
    ShapeRenderer component to render shapes.
    """

    NAME = "Renderer"

    def __init__(
        self, shape, color
    ):
        """
        Construct a ShapeRenderer.

        :param shape: The name of the shape to render. Valid: "circle", "rectangle"
        :type shape: str
        :param color: The color of the shape.
        :type color: Color
        """
        super().__init__()
        self.shape = shape
        self.color = color

        self.is_visible = True

    # Called when the component is created
    def init(self):
        pass

    # Called when the game gets updated
    def update(self):
        if not self.is_visible:
            return

        if self.shape == "circle":
            center = self.peapy[self.parent_name]["Transform"].top_left
            radius = self.peapy[self.parent_name]["Transform"].width

            pygame.draw.circle(self.peapy.window.screen, self.color, center, radius)

        elif self.shape == "rectangle":
            top_left = self.peapy[self.parent_name]["Transform"].top_left
            width = self.peapy[self.parent_name]["Transform"].width
            height = self.peapy[self.parent_name]["Transform"].height

            pygame.draw.rect(
                self.peapy.window.screen,
                self.color.rgba,
                (top_left[0], top_left[1], width, height),
            )
