from enum import Enum
from typing import Protocol

class Player(Enum):
    Draw = "-"
    P1 = "X"
    P2 = "O"


class TicTacToeInfo(Protocol):
    @property
    def grid(self) -> list[list[None | Player]]: ...

    @property
    def winner(self) -> Player | None: ...

    @property
    def is_draw(self) -> bool: ...

    @property
    def is_locked(self) -> bool: ...

    def place(self, i: int, j: int, player: Player) -> bool: ... 