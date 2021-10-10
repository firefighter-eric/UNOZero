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
        for color in ['RED', 'GREEN', 'BLUE', 'YELLOW']:
            for content in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'SKIP', 'DRAW_TWO', 'REVERSE']:
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
        for content in ['WILD', 'WILD_DRAW_FOUR']:
            for n in range(4):
                card = Card(uid, idx, 'BLACK', content)
                self.all.append(card)
                uid += 1
            idx += 1

    def __len__(self):
        return len(self.all)


if __name__ == '__main__':
    cards = Cards()
