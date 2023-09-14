
import requests

from core import constants


class DeckAPI:
    """Class responsible to handler with Deck of Cards API
    """
    def __init__(self) -> None:
        pass

    def create_deck(self) -> None:
        """Creates a deck with 52 cards

        Returns:
            dict: Deck from API
        """
        return requests.get(constants.URL_CREATE_DECK).json()
    
    def draw_card(self) -> None:
        """Gets 11 randomly cards

        Returns:
            dict: Cards
        """
        deck =  self.create_deck()
        return requests.get(constants.DRAW_A_CARD.format(deck["deck_id"])).json()

