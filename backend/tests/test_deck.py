import pytest

from backend.core.game_type import GameType
from backend.models.deck import Deck


@pytest.mark.parametrize(
    "game_type, expected_length",
    [
        (GameType.KUHN, 3),
        (GameType.TEXAS_HOLDEM, 52),
    ]
)
def test_deck_length_by_game_type(
        game_type: GameType,
        expected_length: int
):
    """Check that the length of the deck is the expected one."""

    deck = Deck()
    deck.instantiate_deck(
        game_type=game_type
    )

    assert len(deck.cards) == expected_length
