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

    @property
    def top_left(self):
        """
        Returns the top left corner of the transform.
        :return: tuple[int, int]
        """
        return self.x, self.y

    @property
    def top_right(self):
        """
        Returns the top right corner of the transform.
        :return: tuple[int, int]
        """
        return self.x + self.width, self.y

    @property
    def bottom_left(self):
        """
        Returns the bottom left corner of the transform.
        :return: tuple[int, int]
        """
        return self.x, self.y + self.height

    @property
    def bottom_right(self):
        """
        Returns the bottom right corner of the transform.
        :return: tuple[int, int]
        """
        return self.x + self.width, self.y + self.height
