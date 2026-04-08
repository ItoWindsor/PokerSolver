from dataclasses import dataclass
from typing import List

from src.card import Card

@dataclass
class Deck:
    cards : List[Card]
