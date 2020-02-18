from enum import Enum


class GameStatus(Enum):
    """
    статусы игры
    const
    """
    WON = 1
    LOST = 2
    IN_PROGRESS = 3
    NOT_STARTED = 4
