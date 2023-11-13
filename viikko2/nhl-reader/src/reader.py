from player import Player
import requests

class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.response = requests.get(url).json()
        self.players = []
        self.get_players()

    def get_players(self):
        for player_dict in self.response:
            player = Player(player_dict)
            self.players.append(player)
        return self.players
