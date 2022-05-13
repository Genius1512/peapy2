import peapy2


def main():
    game = peapy2.PeaPy(
        "Sandbox", width=800, height=600, background_color=(255, 255, 255)
    )

    player = game.add_object(peapy2.GameObject("Player"))
    player_pos: peapy2.Transform = player.add_component(
        peapy2.Transform(100, 100, 50, 50)
    )
    player_text: peapy2.Text = player.add_component(peapy2.Text(
        "Player",
        font_name="Arial",
        font_size=20,
        color=(0, 0, 0),
        x_offset=200,
        y_offset=0,
    ))

    while game.update():
        player_pos.x += 1

    game.quit()


if __name__ == "__main__":
    main()
