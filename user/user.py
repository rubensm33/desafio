

from ast import List


class User:

    def __init__(self, name: str, cards:List = None) -> None:
        self.name = name
        self.cards = cards

