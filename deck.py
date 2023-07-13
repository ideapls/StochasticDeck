from card import Card
from enum import Enum

TOTAL = 52
CARD_VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


class Naipes(Enum):
    COPAS = 0
    OUROS = 1
    PAUS = 2
    ESPADAS = 3


class Deck:

    def __init__(self, cards_in_deck=0):
        self._cards_in_deck = cards_in_deck

    def insert_all_cards(self):
        p = Card()
        for i in range(len(CARD_VALUES)):
            for j in list(Naipes):
                p.set_naipe(j)
                p.set_value(CARD_VALUES[i])
                self._cards_in_deck += 1
        return self._cards_in_deck

    def __str__(self):
        return "Number of cards in deck:" + str(self._cards_in_deck)
