from peapy2.component import Component
from .__pygame import pygame


class Sound(Component):
    """
    Component to play sounds.
    """

    NAME = "Sound"

    def __init__(self, file_path: str, channel: int):
        """
        Construct a Sound.

        :param file_path: Path to the sound file.
        :type file_path: str
        :param channel: The channel to play the sound on.
        :type channel: int
        """
        super().__init__()

        pygame.mixer.init()
        self.sound = pygame.mixer.Sound(file_path)
        self.channel_num = channel
        self.channel = pygame.mixer.Channel(self.channel_num)

    def play(self):
        """
        Play the sound.
        """
        self.channel.play(self.sound)

    def stop(self):
        """
        Stop the sound.
        """
        self.channel.stop()

    def pause(self):
        """
        Pause the sound.
        """
        self.channel.pause()

    def unpause(self):
        """
        Unpause the sound.
        """
        self.channel.unpause()

    def set_volume(self, volume: float):
        """
        Set the volume of the sound.
        :param volume: The volume to set the sound to.
        :type volume: float
        """
        self.sound.set_volume(volume)

    @property
    def volume(self):
        """
        Get the volume of the sound.
        :return: float
        """
        return self.sound.get_volume()

    @property
    def is_playing(self):
        """
        Check if the sound is playing.
        :return: bool
        """
        return pygame.mixer.Channel(self.channel).get_busy()
