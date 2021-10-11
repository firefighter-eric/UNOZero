from cards import CardHeap
from player import Player


class Game:
    def __init__(self, player_num=4):
        self.card_heap = CardHeap()
        self.player_num = player_num
        self.players = [Player()] * player_num
        self.round_num = 0
        self.state = None
        self.color = None

    def one_round(self):
        player_idx = self.round_num % self.player_num
        player = self.players[player_idx]
        player.view_game(self)
        out = player.make_move()

        if out == 'draw':
            cards = self.card_heap.draw(1)
            player.get_cards(cards)

        if is_out

        if out == 'draw_four':
            self.state = 'draw_four'
        if out == 'draw_two':




