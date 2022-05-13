from peapy2.component import Component
from peapy2.__pygame import pygame


class Text(Component):
    NAME = "Text"

    def __init__(
        self,
        text: str,
        font_name: str,
        font_size: int,
        color: tuple = (0, 0, 0),
        x_offset: int = 0,
        y_offset: int = 0,
    ):
        super().__init__()

        self.text = text
        self.font_name = font_name
        self.font_size = font_size
        self.color = color
        self.x_offset = x_offset
        self.y_offset = y_offset

        self.font_size = font_size
        self.__font = None
        self.is_visible = True

        pygame.font.init()

    # Called when the component is created
    def init(self):
        self.__font = pygame.font.SysFont(self.font_name, self.font_size)

    # Called when the game gets updated
    def update(self):
        if not self.is_visible:
            return

        text = self.__font.render(self.text, True, self.color)
        self.peapy.window.screen.blit(text, (
            self.peapy[self.parent_name]["Transform"].x + self.x_offset,
            self.peapy[self.parent_name]["Transform"].y + self.y_offset
        ))