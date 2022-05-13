from peapy2.__pygame import pygame


class Window:
    def __init__(self, width, height, title, background_color: tuple = (0, 0, 0)):
        self.width = width
        self.height = height
        self.title = title
        self.background_color = background_color

        pygame.init()

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

        self.clock = pygame.time.Clock()

        self.delta_time = 0.0
        self.fps = 0.0

    def update(self) -> bool:
        self.delta_time = self.clock.tick(60) / 1000.0
        self.fps = self.clock.get_fps()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        pygame.display.update()
        return True
