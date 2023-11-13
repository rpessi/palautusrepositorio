from reader import PlayerReader

class PlayerStats:
    def __init__(self, data: PlayerReader):
        self.players = data.players

    def top_scorers_by_nationality(self, nationality:str):
        top_scorers = []
        for player in self.players:
            if player.nationality == nationality:
                top_scorers.append(player)
        top_scorers.sort(key=lambda x: x.points, reverse=True)
        return top_scorers
