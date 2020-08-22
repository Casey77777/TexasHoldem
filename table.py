from discord.ext import commands

class Table:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        if player in self.players:
            raise ValueError
        self.players.append(player)

    def remove_player(self, player):
        if not player in self.players:
            raise ValueError
        self.players.remove(player)
