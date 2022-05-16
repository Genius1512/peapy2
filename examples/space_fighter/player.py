import keyboard
import os

import peapy2


class Player(peapy2.GameObject):
    def __init__(self, name: str):
        super().__init__(name)
        self.score_text = None
        self.image_renderer = None
        self.transform = None

        self.velocity = 5
        self.score = 0

    # Called when the object is created
    def init(self):
        self.transform: peapy2.Transform = self.add_component(peapy2.Transform(
            175,
            500,
            50,
            50
        ))

        self.image_renderer: peapy2.ImageRenderer = self.add_component(peapy2.ImageRenderer(
            os.path.join("assets", "images", "player.png"),
            -2,
            -2
        ))

        self.score_text: peapy2.Text = self.add_component(peapy2.Text(
            "0",
            "Arial",
            20,
            peapy2.Color(255, 255, 255),
            0,
            -20
        ))

    # Called when the object gets updated
    def update(self):
        if keyboard.is_pressed("a") and self.transform.x > 0:
            self.transform.x -= self.velocity

        if keyboard.is_pressed("d") and self.transform.x < self.peapy.width - self.transform.width:
            self.transform.x += self.velocity

        if keyboard.is_pressed("w") and self.transform.y > 0:
            self.transform.y -= self.velocity

        if keyboard.is_pressed("s") and self.transform.y < self.peapy.height - self.transform.height:
            self.transform.y += self.velocity

        self.score_text.text = str(self.score)

    # Called when the object is destroyed
    def destroy(self):
        pass
