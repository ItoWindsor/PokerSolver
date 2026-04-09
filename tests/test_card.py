import pytest 

from src.card import CardSuit, CardRank
from src.card import Card

def test_card_comparison():
    """
    Check if the basic card comparison are well defined
    """
    king = Card(CardRank.KING, CardSuit.SPADES)
    queen = Card(CardRank.QUEEN, CardSuit.HEARTS)
    jack = Card(CardRank.JACK, CardSuit.CLUBS)
    
    assert king > queen
    assert jack < queen
    assert king > jack
