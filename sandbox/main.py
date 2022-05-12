import peapy2


def main():
    game = peapy2.PeaPy("Sandbox")

    player = game.add_object(peapy2.GameObject("Player"))

    while game.update():
        pass

    game.quit()


if __name__ == "__main__":
    main()
