import peapy2

from logo import Logo


def main():
    game = peapy2.PeaPy(
        "PeaPy",
        800,
        600,
        (255, 255, 255)
    )

    logo = game.add_object(Logo("Logo"))

    while game.update():
        pass
        

if __name__ == "__main__":
    main()
