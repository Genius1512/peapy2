import os

import peapy2

from collider import Collider


class Meteor(peapy2.GameObject):
    def __init__(self, name: str, x_pos: int, velocity: int = 2):
        super().__init__(name)

        self.image_renderer = None
        self.transform = None
        self.x_pos = x_pos
        self.velocity = velocity

    # Called when the object is created
    def init(self):
        self.transform = self.add_component(peapy2.Transform(
            self.x_pos,
            0,
            40,
            40
        ))

        self.image_renderer = self.add_component(peapy2.ImageRenderer(
            os.path.join("assets", "images", "meteor.png"),
            -2,
            -2
        ))

        self.add_component(Collider(
            0,
            0
        ))

    # Called when the object gets updated
    def update(self):
        self.transform.y += self.velocity

        if self.transform.y > self.peapy.height:
            self.peapy.player.score += 1
            self.peapy.remove_object(self.name)

    # Called when the object is destroyed
    def destroy(self):
        pass
