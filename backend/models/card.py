from typing import Any
from dataclasses import dataclass
import logging

from backend.core.card_enum import CardRank, CardSuit


@dataclass(frozen=True)
class Card:
    """
    Class Card supposed to represent the in game card values
    
    :params rank: The rank of the card 
        e.g : CardRank.ACE 
    :params suit: The suit of the card 
        e.g : CardSuit.HEARTS
    """
    rank: CardRank
    suit: CardSuit

    def __lt__(
            self,
            other: Any
    ) -> bool:
        """
        Overloading of the comparison operator. 


        :params other: object to compare the card to.
        """
        if not isinstance(other, Card):
            error_msg: str = f"Can't compare type Card and type {type(other)}"
            logging.error(error_msg)
            raise TypeError(error_msg)

        return self.rank < other.rank

    def __repr__(self) -> str:
        """Debug Version of the string representation of a card."""
        if self.rank < 11:
            rank_str = str(self.rank.value)
        else:
            rank_str = self.rank.name[0]

        return f"{rank_str}{self.suit.value}"

    def __str__(self) -> str:
        return f"{self.rank.name.capitalize()} of {self.suit.value}"
