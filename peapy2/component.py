class Component:
    NAME = "Component"

    def __init__(self):
        self.peapy = None
        self.parent_name = None

    def init_(self, peapy, parent_name: str):
        self.peapy = peapy
        self.parent_name = parent_name

        self.init()  # TODO: make component.init() optional

    def init(self):
        pass

    def update_(self):
        self.update()  # TODO: make component.update() optional

    def update(self):
        pass

    def destroy_(self):
        self.destroy()  # TODO: make component.destroy() optional

    def destroy(self):
        pass

    #  TODO: .gameObject property

    def tree(self) -> str:
        return f"\t\t{self.NAME}\n"

    def __repr__(self):
        return f"peapy2.Component({self.NAME})"
