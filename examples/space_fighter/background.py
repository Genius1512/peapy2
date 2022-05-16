import os

import peapy2


class Background(peapy2.GameObject):
    def __init__(self, name: str, velocity: int = 2, start_y: int = 0):
        super().__init__(name)

        self.image_renderer = None
        self.transform = None
        self.velocity = velocity
        self.start_y = start_y

    # Called when the object is created
    def init(self):
        self.transform: peapy2.Transform = self.add_component(peapy2.Transform(
            0,
            self.start_y,
            0,
            0
        ))

        self.image_renderer: peapy2.ImageRenderer = self.add_component(peapy2.ImageRenderer(
            os.path.join("assets", "images", "background.png")
        ))

    # Called when the object gets updated
    def update(self):
        self.transform.y += self.velocity

        if self.transform.y > self.peapy.height:
            self.transform.y = -self.peapy.height + 2

    # Called when the object is destroyed
    def destroy(self):
        pass
