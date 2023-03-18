import numpy as np

try: from .player import Player
except: from player import Player


class Game:

    def __init__(self, n):
        self.players = self.initialize_players(n)

    def initialize_players(self, n):
        players = []
        for i in range(n):
            player = Player(index=i)
            players.append(player)
        return players
        
    def __str__(self):
        txt = ''
        for player in self.players:
            txt += str(player)
            txt += ' / is alive: ' + str(player.is_alive())
            txt += '\n'
        return txt
    
    def filter_active_players(self):
        result = []
        for player in self.players:
            if player.is_alive() is True:
                result.append(player)
        return result

    def is_done(self):
        result = False
        active_players = self.filter_active_players()
        if len(active_players) == 1:
            result = True
        return result
    
    def run_step(self, k):
        active_players = self.filter_active_players()
        all_feet = []
        for player in active_players:
            feet = player.filter_active_feet()
            all_feet = [*all_feet, *feet]
        length = len(all_feet)
        index = k - 1
        while index >= length:
            index -= length
        #print(index)
        burnt_foot = all_feet[index]
        txt = ''
        txt += 'player '
        txt += str(burnt_foot.player.index)
        txt += ', '
        txt += burnt_foot.side
        txt += ' side'
        print(txt)
        burnt_foot.active = False

    def solve(self, k):
        while self.is_done() is False:
            self.run_step(k)
        active_players = self.filter_active_players()
        winner = active_players[0]
        return winner
        


if __name__ == "__main__":
    game = Game(n=5)
    #game.run_step(k=11)
    winner = game.solve(k=7)
    print('winner is: ', winner)
