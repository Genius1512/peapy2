import peapy2


class Logo(peapy2.GameObject):
    def __init__(self, name: str):
        super().__init__(name)

        self.transform = None
        self.text = None

        self.x_vel = 2
        self.y_vel = 2

        self.vel = 200

    # Called when the object is created
    def init(self):
        self.transform: peapy2.Transform = self.add_component(peapy2.Transform(
            100,
            100,
            5,
            5
        ))
        self.text: peapy2.Text = self.add_component(peapy2.Text(
            "DVD",
            "Arial",
            50,
            peapy2.Color(0, 0, 0),
            0,
            0
        ))

    # Called when the object gets updated
    def update(self):
        self.transform.x += self.x_vel
        self.transform.y += self.y_vel

        if self.transform.x > self.peapy.width - self.text.font_size - 30:
            self.x_vel = -self.vel * self.peapy.window.delta_time
        elif self.transform.x < 0:
            self.x_vel = self.vel * self.peapy.window.delta_time

        if self.transform.y > self.peapy.height - self.text.font_size:
            self.y_vel = -self.vel * self.peapy.window.delta_time
        elif self.transform.y < 0:
            self.y_vel = self.vel * self.peapy.window.delta_time

    # Called when the object is destroyed
    def destroy(self):
        pass
