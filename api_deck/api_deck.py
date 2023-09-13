
import requests
from typing import Any

from core import constants


class DeckAPI:

    def __init__(self) -> None:
        pass

    def create_deck(self):
        return requests.get(constants.URL_CREATE_DECK).json()
    
    def draw_card(self):
        deck =  self.create_deck()
        return requests.get(constants.DRAW_A_CARD.format(deck["deck_id"])).json()

