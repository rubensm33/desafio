from typing import List


class User:
    """Class responsible to create a instance with user data
    """
    def __init__(self, name: str, cards:List = None) -> None:
        self.name = name
        self.cards = cards
        self.points = 0
        self.sequence = False
        self.json_format = None

