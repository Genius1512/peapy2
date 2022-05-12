import peapy2


def main():
    game = peapy2.PeaPy("Sandbox")

    player = game.add_object(peapy2.GameObject("Player"))
    player.add_component(peapy2.Transform(100, 100, 50, 50))
    player.add_component(peapy2.ImageRenderer(r".\assets\images\player.png", -2, -2))

    while game.update():
        pass

    game.quit()


if __name__ == "__main__":
    main()
