from enum import Enum


class PlayingAction(Enum):
    FOLD = 'FOLD'
    BET = 'BET'
    CHECK = 'CHECK'
    RAISE = 'RAISE'
