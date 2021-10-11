from uno_game.cards import Card


class Action:
    def __init__(self, card:Card=None, draw=False):
        self.draw = draw
        if draw:
            return

        self.color = card.color
        self.state =




class Player:
    def __init__(self):
        self.cards = []

    def get_cards(self, cards):
        self.cards += cards

    def pop_cards(self, idx):
        return self.cards.pop(idx)

    def make_move(self):

    def view_game(self, game):
        pass

