from dataclasses import dataclass, field
from typing import List

from backend.models.card import Card
from backend.core.game_type import GameType

import logging


@dataclass
class Board:
    game_type: GameType
    cards: List[Card] = field(default_factory=list)

    @property
    def max_cards(self) -> int:
        """
        Dynamically set the maximum allowed community cards 
        based on the game.
        """
        match self.game_type:
            case GameType.KUHN:
                return 0
            case GameType.TEXAS_HOLDEM:
                return 5
            case _:
                error_msg = f"Max cards not defined for {self.game_type.name}"
                logging.error(error_msg)
                raise NotImplementedError(error_msg)

    def add_card(
            self,
            card: Card
    ) -> None:
        """Adds a single card (e.g., Turn or River)."""
        if len(self.cards) >= self.max_cards:
            error_msg = f"""
            Board is full for 
            {self.game_type.name} 
            (Max: {self.max_cards})
            """
            raise ValueError(error_msg)

        self.cards.append(card)

    def add_cards(
            self,
            new_cards: List[Card]
    ) -> None:
        """Adds multiple cards at once (e.g., dealing the Flop)."""
        if len(self.cards) + len(new_cards) > self.max_cards:
            error_msg = f"""
            Adding these cards exceeds the 
            board limit for {self.game_type.name}
            """
            raise ValueError(error_msg)

        self.cards.extend(new_cards)

    def __str__(self) -> str:
        if not self.cards:
            return "Empty Board"
        return " | ".join(str(card) for card in self.cards)
