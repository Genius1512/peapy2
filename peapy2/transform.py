from peapy2.component import Component


class Transform(Component):
    NAME = "Transform"

    def __init__(
        self,
        x: float | int,
        y: float | int,
        width: float | int,
        height: float | int,
        rotation: float | int = 0,
    ):
        super().__init__()

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotation = rotation

    # Called when the component is created
    def init(self):
        pass

    # Called when the game gets updated
    def update(self):
        pass

    # Called when the component is destroyed
    def destroy(self):
        pass

    @property
    def top_left(self):
        return self.x, self.y

    @property
    def top_right(self):
        return self.x + self.width, self.y

    @property
    def bottom_left(self):
        return self.x, self.y + self.height

    @property
    def bottom_right(self):
        return self.x + self.width, self.y + self.height
