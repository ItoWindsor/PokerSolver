import pytest 

from src.card_enum import CardRank, CardSuit
from src.card import Card
from src.game_type import GameType
from src.deck import Deck
from src.board import Board


@pytest.mark.parametrize(
    "game_type, expected_max_cards", 
    [
        (GameType.KUHN, 0),
        (GameType.TEXAS_HOLDEM, 5),
    ]
)
def test_board_max_cards_by_game_type(
        game_type : GameType,
        expected_max_cards : int
):
    board = Board(game_type = game_type)

    assert board.max_cards == expected_max_cards
