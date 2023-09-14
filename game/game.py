

from api_deck.api_deck import DeckAPI
from core import constants
from user.user import User


class Organizer:

    def __init__(self, user: User, deck_api: DeckAPI) -> None:
        self.user = user
        self.deck_api = deck_api
        self._draw_cards_to_user()
        self._filter_cards_values_and_suits()
        self._sum_points_of_cards()

    def _draw_cards_to_user(self):
        self.user.cards = self.deck_api.draw_card()

    def _filter_cards_values_and_suits(self):
        cards = [{"value": constants.CARDS_VALUES[card["value"]], "suit": constants.PORTUGUESE_SUITS[card["suit"]]}
         for card in self.user.cards["cards"]]
        
        self.user.cards = cards

    def _sum_points_of_cards(self):
        self.user.points += [constants.CARDS_VALUES[card["value"]] for card in self.user.cards["cards"]]
