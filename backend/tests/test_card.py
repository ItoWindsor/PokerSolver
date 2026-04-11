import pytest

from backend.core.card_enum import CardSuit, CardRank
from backend.models.card import Card


def test_card_comparison():
    """
    Check if the basic card comparison are well-defined
    """
    king = Card(CardRank.KING, CardSuit.SPADES)
    queen = Card(CardRank.QUEEN, CardSuit.HEARTS)
    jack = Card(CardRank.JACK, CardSuit.CLUBS)

    assert king > queen
    assert jack < queen
    assert king > jack
