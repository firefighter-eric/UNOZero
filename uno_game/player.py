from uno_game.cards import Card, STATE


def get_legal_states(color, state):
        legal_states = []
        if state == STATE.DRAW_TWO:
            legal_states += [STATE.DRAW_TWO, STATE.WILD_DRAW_FOUR]
        elif state == STATE.WILD_DRAW_FOUR:
            legal_states += [STATE.WILD_DRAW_FOUR]
        legal_states.append()



class Action:
    def __init__(self, card: Card = None, draw=False):
        self.draw = draw
        if draw:
            return

        self.color = card.color
        self.content = card.content


class Player:
    def __init__(self):
        self.cards = []

    def get_cards(self, cards):
        self.cards += cards

    def pop_cards(self, idx):
        return self.cards.pop(idx)

    @staticmethod
    def make_move(action: Action):
        return action

    def view_game(self, game):
        pass
