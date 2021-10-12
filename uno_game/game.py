from cards import CardHeap, STATE, COLOR
from player import Player


class Game:
    def __init__(self, player_num=4):
        self.card_heap = CardHeap()
        self.player_num = player_num
        self.players = [Player()] * player_num
        self.round_num = 0
        self.state = None
        self.color = None
        self.direction = 1

    def one_round(self):
        if self.state == STATE.SKIP:
            self.round_num += self.direction

        if self.state == STATE.DRAW_TWO:






        player_idx = self.round_num % self.player_num
        player = self.players[player_idx]
        player.view_game(self)
        action = player.make_move()

        if action.draw:
            cards = self.card_heap.draw(1)
            player.get_cards(cards)

        self.state = action.content
        if action.color != COLOR.BLACK:
            self.color = action.color




