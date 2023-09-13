from api_deck.api_deck import DeckAPI
import core.constants
from game.game import Organizer
from user.user import User

user_alan = User(name="alan")
user_bruno = User(name="bruno")

deck_api = DeckAPI()
Organizer(user=user_alan,deck_api=deck_api)
Organizer(user=user_bruno, deck_api=deck_api)

print(user_alan.cards)
print("\n\n\n\n")
print(user_bruno.cards)