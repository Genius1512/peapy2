class Component:
    NAME = "Component"

    def __init__(self):
        self.peapy = None
        self.parent_name = None

    def init_(self, peapy, parent_name: str):
        self.peapy = peapy
        self.parent_name = parent_name

        try:
            self.init()
        except AttributeError:
            pass

    def init(self):
        pass

    def update_(self):
        print(f"Updating {self.NAME}")

        try:
            self.update()
        except AttributeError:
            pass

    def update(self):
        pass

    def destroy_(self):
        try:
            self.destroy()
        except AttributeError:
            pass

    def destroy(self):
        pass

    @property
    def game_object(self):
        return self.peapy[self.parent_name]

    def tree(self) -> str:
        return f"\t\t{self.NAME}\n"

    def __repr__(self):
        return f"peapy2.Component({self.NAME})"
