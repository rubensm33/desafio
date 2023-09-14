import json

from api_deck.api_deck import DeckAPI
from game.organizer import Organizer
from user.user import User
from core import constants


user_alan = User(name="alan")
user_bruno = User(name="bruno")

deck_api = DeckAPI()
Organizer(user=user_alan,deck_api=deck_api)
Organizer(user=user_bruno, deck_api=deck_api)

if user_alan.points > user_bruno.points:
    json_data = {**user_alan.json_format, **user_bruno.json_format, constants.WINNER: user_alan.name}

elif user_bruno.points > user_alan.points:
    json_data = {**user_alan.json_format, **user_bruno.json_format, constants.WINNER: user_bruno.name}

else:
    json_data = {**user_alan.json_format, **user_bruno.json_format, constants.WINNER: constants.DRAW}

print(json.dumps(json_data, indent=4))
