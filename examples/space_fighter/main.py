import peapy2
import random

from background import Background
from meteor import Meteor
from player import Player


def main():
    game = peapy2.PeaPy(
        "PeaPy",
        400,
        600,
        peapy2.Color(0, 0, 0)
    )

    game.add_object(Background("background1", 2, 0))
    game.add_object(Background("background2", 2, -600))

    game.add_object(Player("player"))

    game_manager = game.add_object(peapy2.GameObject("GameManager"))
    game_manager.add_component(peapy2.Transform(0, 0, 0, 0))
    fps_text: peapy2.Text = game_manager.add_component(peapy2.Text(
        "",
        "Arial",
        40,
        peapy2.Color(255, 255, 255),
        0,
        0
    ))

    frame_distance = 100

    while game.update():
        if game.window.frame_count % frame_distance == 0:
            game.add_object(Meteor(f"Meteor{game.window.frame_count}",
                                   random.randint(0, game.window.width),
                                   random.randint(2, 10)))

            if frame_distance > 20:
                frame_distance -= 5

        fps_text.text = str(round(game.window.fps))


if __name__ == "__main__":
    main()
