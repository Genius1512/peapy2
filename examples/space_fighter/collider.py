import peapy2
from shapely.geometry import Polygon
from sys import exit


class Collider(peapy2.Component):
    NAME = "Collider"

    def __init__(self, x_offset: int = 0, y_offset: int = 0, width: int = -1, height: int = -1):
        super().__init__()

        self.x_offset = x_offset
        self.y_offset = y_offset

        self.width = width
        self.height = height

        self.inherit_width = False
        self.inherit_height = False

    def init(self):
        if self.width == -1:
            self.inherit_width = True
            self.width = self.game_object.transform.width

        if self.height == -1:
            self.inherit_height = True
            self.height = self.game_object.transform.height

    # Called when the game gets updated
    def update(self):
        if self.inherit_width:
            self.width = self.game_object.transform.width

        if self.inherit_height:
            self.height = self.game_object.transform.height

        if self.collides_with_player():
            exit(0)

    def collides_with_player(self):
        p1 = Polygon([
            (self.game_object.transform.x + self.x_offset, self.game_object.transform.y + self.y_offset),
            (self.game_object.transform.x + self.x_offset + self.width, self.game_object.transform.y + self.y_offset),
            (self.game_object.transform.x + self.x_offset + self.width, self.game_object.transform.y +
             self.y_offset + self.height),
            (self.game_object.transform.x + self.x_offset, self.game_object.transform.y + self.y_offset + self.height)
        ])

        p2 = Polygon([
            (self.peapy.player.transform.x, self.peapy.player.transform.y),
            (self.peapy.player.transform.x + self.peapy.player.transform.width, self.peapy.player.transform.y),
            (self.peapy.player.transform.x + self.peapy.player.transform.width, self.peapy.player.transform.y +
                self.peapy.player.transform.height),
            (self.peapy.player.transform.x, self.peapy.player.transform.y + self.peapy.player.transform.height)
        ])

        return p1.intersects(p2)
