from typing import Protocol
from enum import Enum, StrEnum


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


class ExplosionType(StrEnum):
    SOLID = "Solid"
    HOLLOW = "Hollow"


class PlayerInfo(Protocol):
    @property
    def i(self) -> int: ...

    @property
    def j(self) -> int: ...

    def move(self, di: int, dj: int, grid_width: int, grid_height: int) -> bool: ...


class ExplosionRule(Protocol):
    def get_explosion_coords(self, i: int, j: int, r: int) -> set[tuple[int, int]]: ...


class BombInfo(Protocol):
    @property
    def i(self) -> int: ...

    @property
    def j(self) -> int: ...

    @property
    def full_timer(self) -> int: ...

    @property
    def full_radius(self) -> int: ...

    @property
    def current_timer(self) -> int: ...

    @property
    def current_radius(self) -> int: ...

    @property
    def is_done(self) -> bool: ...

    def tick(self) -> None: ...

    def get_explosion_coords(self) -> set[tuple[int, int]]: ...
