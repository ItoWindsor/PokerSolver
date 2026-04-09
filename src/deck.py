import itertools
import random
from dataclasses import dataclass, field
from typing import List

from src.card_enum import CardRank, CardSuit
from src.card import Card
from src.game_type import GameType

import logging

@dataclass
class Deck:
    cards : List[Card] =  field(default_factory=list)
    
    def populate_deck(
        self,
        game_type : GameType
    ) -> None:
        """
       Populate the deck according to the game type.

       A deck is composed of cards but the number and the type of cards 
       is determined by the game we are playing.
       :param game_type: Game type 
        e.g : GameType.KUHN 
       """ 
        match game_type:
            case GameType.KUHN:
                self.cards = [
                    Card(CardRank.JACK, CardSuit.HEARTS),
                    Card(CardRank.QUEEN, CardSuit.HEARTS),
                    Card(CardRank.KING, CardSuit.HEARTS)
                ]
            case GameType.TEXAS_HOLDEM:
                self.cards = [
                    Card(r,s) for r,s in itertools.product(CardRank,CardSuit) 
                ]
            case _:
                error_msg : str = f"game_type : {game_type} has not been implemented"
                logging.error(error_msg)
                raise NotImplementedError(error_msg)

    def shuffle_deck(self) -> None:
        """
        Shuffle the deck so that the order of the cards is 
        not deterministic.
        """
        random.shuffle(self.cards)

    def instantiate_deck(
        self,
        game_type : GameType
    ) -> None:
        """
        Instantiate a deck according to the game type.
        """
        self.populate_deck(
            game_type=game_type
        )
        self.shuffle_deck()

    def draw_card(self) -> Card:
        """Draw a card from the deck and retire it"""
        if not self.cards:
            error_msg : str = "All cards have been drawn"
            logging.error(error_msg)
            raise ValueError(error_msg)
        return self.cards.pop()
    
    def __str__(self) -> str:
        """String representation of a Deck"""
        nb_cards = len(self.cards)
        
        dict_suit_number = {
            s: sum(1 for c in self.cards if c.suit == s)
            for s in CardSuit
        }
        
        output = f"Deck with {nb_cards} cards remaining: "
        output += " | ".join(
            [f"{num}{s.value}" for s, num in dict_suit_number.items()]
        )
        
        return output

        
