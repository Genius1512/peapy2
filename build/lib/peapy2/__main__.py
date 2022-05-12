import os
from sys import argv

MAIN = """import peapy2


def main():
    game = peapy2.PeaPy("PeaPy")
    while game.update():
        pass
        

if __name__ == "__main__":
    main()
"""

GAME_OBJECT_TEMPLATE = """import peapy2


class {name}(peapy2.GameObject):
    def __init__(self, name: str):
        super().__init__(name)

    # Called when the object is created
    def init(self):
        pass

    # Called when the object gets updated
    def update(self):
        pass

    # Called when the object is destroyed
    def destroy(self):
        pass
"""

COMPONENT_TEMPLATE = """import peapy2


class {name}(peapy2.Component):
    NAME = "{name}"

    def __init__(self):
        super().__init__()

    # Called when the component is created
    def init(self):
        pass

    # Called when the game gets updated
    def update(self):
        pass

    # Called when the component is destroyed
    def destroy(self):
        pass
"""


def main(args):
    try:
        if args[1] == "init":
            print("Initializing new PeaPy project...")
            with open("main.py", "w") as f:
                f.write(MAIN)
            os.mkdir("assets")
            os.mkdir("assets/images")
            os.mkdir("assets/sounds")
            print("Done!")

        elif args[1] == "new":
            try:
                if args[2] == "game_object":
                    try:
                        print("Creating new object {}".format(args[3]))
                        with open(args[3].lower() + ".py", "w") as f:
                            f.write(GAME_OBJECT_TEMPLATE.format(name=args[3]))
                    except IndexError:
                        print("Please specify a name for the object")

                elif args[2] == "component":
                    try:
                        print("Creating new component {}".format(args[3]))
                        with open(args[3].lower() + ".py", "w") as f:
                            f.write(COMPONENT_TEMPLATE.format(name=args[3]))
                    except IndexError:
                        print("Please specify a name for the component")

            except IndexError:
                print("Please specify the type of component you want to create.")
    except IndexError:
        print("Use either init or new")


if __name__ == "__main__":
    main(argv)
