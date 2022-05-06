from .component import Component


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

    # TODO: Add properties
