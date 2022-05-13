from peapy2.component import Component
from .__pygame import pygame


class Sound(Component):
    def __init__(self, file_path: str, channel: int):
        super().__init__()

        pygame.mixer.init()
        self.sound = pygame.mixer.Sound(file_path)
        self.channel_num = channel
        self.channel = pygame.mixer.Channel(self.channel_num)

    def play(self):
        self.channel.play(self.sound)

    def stop(self):
        self.channel.stop()

    def pause(self):
        self.channel.pause()

    def unpause(self):
        self.channel.unpause()

    def set_volume(self, volume: float):
        self.sound.set_volume(volume)

    @property
    def volume(self):
        return self.sound.get_volume()

    @property
    def is_playing(self):
        return pygame.mixer.Channel(self.channel).get_busy()
