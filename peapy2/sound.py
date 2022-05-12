from peapy2.component import Component


class Sound(Component):
    NAME = "Sound"

    def __init__(self, path: str):
        super().__init__()

        self.path = path

    # Called when the component is created
    def init(self):
        pass

    # Called when the game gets updated
    def update(self):
        pass

    # Called when the component is destroyed
    def destroy(self):
        pass
