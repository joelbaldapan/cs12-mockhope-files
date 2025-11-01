from common_types import Player, TicTacToeInfo


class UltimateTicTacToeView:
    def display_full_board(self, small_grids: list[list[TicTacToeInfo]]) -> None:
        """Display the full board"""
        print("\n=====\n")
        print("Full Board:")
        print()

        ... # your code here

        print()

    def display_ultimate_grid(self, ultimate_grid: TicTacToeInfo) -> None:
        """Display the 3x3 ultimate grid"""
        print("Ultimate Tic-Tac-Toe Grid:")
        print()

        ... # your code here

        print()

    def prompt_big_cell(self) -> tuple[int, int]:
        """Must prompt 'Enter (bi, bj): '"""
        ... # your code here

    def prompt_small_cell(self) -> tuple[int, int]:
        """Must prompt 'Enter (si, sj): '"""
        ... # your code here

    def show_forced_cell(self, forced: tuple[int, int]) -> None:
        print(f"Forced at {forced}.")

    def show_turn(self, player: Player) -> None:
        print(f"Player {self._parse_player(player)}'s turn:")

    def show_winner(self, player: Player) -> None:
        print(f"Player {self._parse_player(player)} wins!")

    def show_draw(self) -> None:
        print("It's a draw!")

    def _parse_player(self, raw: Player) -> int:
        return 1 if raw == Player.P1 else 2