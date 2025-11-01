from common_types import BombInfo, PlayerInfo


class KoyukiView:
    def display_frame(self, frame: int):
        print()
        print(f"Frame: {frame}")

    def display_grid(
        self,
        width: int,
        height: int,
        player: PlayerInfo,
        bombs: list[BombInfo],
    ) -> None:

        ... # your code here

        print()

    def display_game_over(self):
        print("Game over!")

    def get_input(self):
        while True:
            inp = input("Move: ").lower()
            if inp in {"w", "a", "s", "d", ""}:
                return inp