from peapy2.component import Component
from peapy2.__pygame import pygame


VALID_SHAPES = ["circle", "rectangle"]


class ShapeRenderer(Component):
    NAME = "Renderer"

    def __init__(
        self, shape: str, color: tuple[int, int, int] | tuple[int, int, int, int]
    ):
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
                self.color,
                (top_left[0], top_left[1], width, height),
            )

    # Called when the component is destroyed
    def destroy(self):
        pass
