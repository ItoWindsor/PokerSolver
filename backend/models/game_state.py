from dataclasses import dataclass, field
from typing import List

from backend.core.game_type import GameType
from backend.core.playing_action import PlayingAction
from backend.models.board import Board
from backend.models.card import Card


@dataclass
class GameState:
    game_type: GameType
    board: Board
    num_players: int

    player_cards: List[List[Card]]

    stacks: List[int]
    active_players: List[bool]

    pot: int = 0
    history: List[PlayingAction] = field(default_factory=list)
    current_player_index: int = 0
