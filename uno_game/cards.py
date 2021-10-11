import random
from typing import List


class COLOR:
    RED = 0
    GREEN = 1
    BLUE = 2
    YELLOW = 3
    BLACK = 4


class STATE:
    SKIP = 0
    DRAW_TWO = 1
    REVERSE = 2
    WILD = 3
    WILD_DRAW_FOUR = 4


class Card:
    def __init__(self, uid, idx, color, content):
        self.uid = uid
        self.idx = idx
        self.color = color
        self.content = content


class Cards:
    def __init__(self):
        self.all = []

        uid = 0
        idx = 0
        for color in [COLOR.RED, COLOR.GREEN, COLOR.BLUE, COLOR.YELLOW]:
            for content in ['1', '2', '3', '4', '5', '6', '7', '8', '9', STATE.SKIP, STATE.DRAW_TWO, STATE.REVERSE]:
                for n in range(2):
                    card = Card(uid, idx, color, content)
                    self.all.append(card)
                    uid += 1
                idx += 1

            # card '0'
            card = Card(uid, idx, color, '0')
            self.all.append(card)
            uid += 1
            idx += 1

        # card 'BLACK'
        for content in [STATE.WILD, STATE.WILD_DRAW_FOUR]:
            for n in range(4):
                card = Card(uid, idx, COLOR.BLACK, content)
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
    cards = Cards()
    ch = CardHeap()
