class Color:
    def __init__(self, *args):
        self.r = None
        self.g = None
        self.b = None
        self.a = None

        if len(args) == 0:
            self.r = 0
            self.g = 0
            self.b = 0
            self.a = 0
            return

        elif len(args) == 1:
            if type(args[0]) == int:
                self.r, self.g, self.b, self.a = args[0]
                return

            elif type(args[0]) == tuple:
                self.r, self.g, self.b, self.a = args[0]
                return

            elif type(args[0]) == str:
                hexadecimal = args[0].replace("#", "")

                if len(hexadecimal) == 2:
                    self.r = int(hexadecimal, 16)
                    self.g = int(hexadecimal, 16)
                    self.b = int(hexadecimal, 16)
                    self.a = 255

                    print(self.r, self.g, self.b, self.a)
                    return

                elif len(hexadecimal) == 3:
                    self.r = int(hexadecimal[0] * 2, 16)
                    self.g = int(hexadecimal[1] * 2, 16)
                    self.b = int(hexadecimal[2] * 2, 16)
                    self.a = 255
                    return

                elif len(hexadecimal) == 6:
                    self.r = int(hexadecimal[0:2], 16)
                    self.g = int(hexadecimal[2:4], 16)
                    self.b = int(hexadecimal[4:6], 16)
                    self.a = 255
                    return

                elif len(hexadecimal) == 8:
                    self.r = int(hexadecimal[0:2], 16)
                    self.g = int(hexadecimal[2:4], 16)
                    self.b = int(hexadecimal[4:6], 16)
                    self.a = int(hexadecimal[6:8], 16)
                    return

        elif len(args) == 3:
            self.r, self.g, self.b = args
            self.a = 255
            return

        elif len(args) == 4:
            self.r, self.g, self.b, self.a = args
            return

        raise ValueError("Invalid color arguments")

    @property
    def rgb(self) -> tuple[int, int, int]:
        return self.r, self.g, self.b

    @property
    def rgba(self) -> tuple[int, int, int, int]:
        return self.r, self.g, self.b, self.a

    @property
    def hex(self) -> str:
        return str(self)

    def __str__(self):
        return "#{:02x}{:02x}{:02x}{:02x}".format(self.r, self.g, self.b, self.a)
