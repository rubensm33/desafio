

from api_deck.api_deck import DeckAPI
from core import constants
from user.user import User


class Organizer:

    def __init__(self, user: User, deck_api: DeckAPI) -> None:
        self.user = user
        self.deck_api = deck_api
        self._draw_cards_to_user()
        self._filter_cards_values_and_suits()

    def _draw_cards_to_user(self):
        self.user.cards = self.deck_api.draw_card()

    def _filter_cards_values_and_suits(self):
        cards = []
        for card in self.user.cards["cards"]:
            cards.append({"value": constants.CARDS_VALUES[card["value"]], "suit":constants.PORTUGUESE_SUITS[card["suit"]]})

        self.user.cards = cards
