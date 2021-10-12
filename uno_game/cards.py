import random
from typing import List

COLOR = ['RED', 'GREEN', 'BLUE', 'YELLOW', 'BLACK']
NUMBER = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
STATE = ['NONE', 'SKIP', 'DRAW_TWO', 'REVERSE', 'WILD', 'WILD_DRAW_FOUR']
CONTENT = NUMBER + STATE


class Card:
    def __init__(self, uid, idx, color, content, state):
        self.uid = uid
        self.idx = idx
        self.color = color
        self.content = content
        self.state = state


class Cards:
    def __init__(self):
        self.all = []

        uid = 0
        idx = 0
        for color in COLOR[:-1]:
            # number card
            for number in NUMBER[1:]:
                for n in range(2):
                    card = Card(uid, idx, color, number, 'NONE')
                    self.all.append(card)
                    uid += 1
                idx += 1

            # '0' card
            card = Card(uid, idx, color, '0', 'NONE')
            self.all.append(card)
            uid += 1
            idx += 1

            # state card
            for state in STATE[1:4]:
                for n in range(2):
                    card = Card(uid, idx, color, state, state)
                    self.all.append(card)
                    uid += 1
                idx += 1

        # 'BLACK' card
        for state in STATE[4:]:
            for n in range(4):
                card = Card(uid, idx, 'BLACK', state, state)
                self.all.append(card)
                uid += 1
            idx += 1

    def __len__(self):
        return len(self.all)


class CardHeap:
    def __init__(self):
        self.unused = Cards().all
        self.shuffle()
        self.used = []

    def draw(self, n: int = 1) -> List[Card]:
        out = []
        for i in range(n):
            out.append(self.unused.pop())
            if not self.unused:
                self.unused, self.used = self.used, self.unused
                self.shuffle()
        return out

    def discard(self, cards: List[Card]):
        self.used += cards

    def shuffle(self):
        random.shuffle(self.unused)


if __name__ == '__main__':
    _cards = Cards()
    _ch = CardHeap()
