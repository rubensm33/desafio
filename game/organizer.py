from api_deck.api_deck import DeckAPI
from core import constants
from user.user import User


class Organizer:
    """Class responsible to handler data from DeckAPI
    """
    def __init__(self, user: User, deck_api: DeckAPI) -> None:
        self.user = user
        self.deck_api = deck_api
        self._draw_cards_to_user()
        self._filter_cards_values_and_suits()
        self._sum_points_of_cards()
        self._order_data()
        self._verify_sequence()
        self._json_format()

    def _draw_cards_to_user(self) -> None:
        """Draw cards to instance User
        """
        self.user.cards = self.deck_api.draw_card()

    def _filter_cards_values_and_suits(self) -> None:
        """Converts user cards in a Dict with value and suit only
        """
        cards = [{"value": constants.CARDS_VALUES[card["value"]], "suit": constants.PORTUGUESE_SUITS[card["suit"]]}
         for card in self.user.cards["cards"]]
        
        self.user.cards = cards

    def _sum_points_of_cards(self) -> None:
        """Adds user points according cards values
        """
        self.user.points = sum(card["value"] for card in self.user.cards)

    def _order_data(self) -> None:
        """Sort cards according Suit and Value"""
        self.user.cards = sorted(self.user.cards, key=lambda x: (x['suit'], x['value']))

    def _verify_sequence(self) -> None:
        """Checks if there is sequence between user cards
        """
        for i in range(len(self.user.cards) - 2):
            card_1 = self.user.cards[i]
            card_2 = self.user.cards[i + 1]
            card_3 = self.user.cards[i + 2]
            
            if card_1['suit'] == card_2['suit'] == card_3['suit'] and card_1["value"] == card_2["value"]-1 and card_1["value"] == card_3["value"]-2:
                self.user.sequence = True 
                return
                
        self.user.sequence = False 

    def _json_format(self) -> None:
        """Format data to desired format
        """
        def create_card(value, suit) -> str:
            """Create a string with value and suit in portuguese

            Args:
                value (int): Card value
                suit (str): Card Type
            Returns:
                str: Card in portuguese
            """
            return f"{value} de {suit}"
        
        self.user.cards = [create_card(card['value'], card['suit']) for card in self.user.cards]
        self.user.json_format = {self.user.name:{"cartas":self.user.cards,"tem_sequencia":self.user.sequence}}

