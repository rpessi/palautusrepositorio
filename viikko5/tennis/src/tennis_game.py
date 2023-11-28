class TennisGame:
    def __init__(self, player1:str, player2:str):
        self.player1 = player1 #pelaajan 1 nimi
        self.player2 = player2 #pelaajan 2 nimi
        self.score1 = 0 #pelaajan 1 pisteet
        self.score2 = 0 #pelaajan 2 pisteet

    def won_point(self, player:str):
        if player == self.player1:
            self.score1 = self.score1 + 1
        else:
            self.score2 = self.score2 + 1

    def get_score(self):
        #score = "" #alustetaan tyhjäksi
        #temp_score = 0
        if self.score1 == self.score2:
            return self.even_points()
        elif self.score1 > 3 or self.score2 > 3:
            return self.big_points()
        return self.small_points()

    def small_points(self):
        score = ""
        for i in range(1, 3):
            if i == 1:
                temp_score = self.score1
            else:
                score = score + "-"
                temp_score = self.score2
            scorelist = ["Love", "Fifteen", "Thirty", "Forty"]
            score = score + scorelist[temp_score]
        return score

    def big_points(self):
        advance = self.score1 - self.score2
        if advance == 1:
            score = f"Advantage {self.player1}"
        elif advance == -1:
            score = f"Advantage {self.player2}"
        elif advance >= 2: #miten voi muka olla suurempi kuin 2?
            score = f"Win for {self.player1}"
        else:
            score = f"Win for {self.player2}"
        return score

    def even_points(self):
        #if self.score1 == self.score2: #tasapisteet
        point_list = ["Love-All", "Fifteen-All", "Thirty-All", "Deuce"]
        if self.score1 < 3:
            score = point_list[self.score1]
        else:
            score = point_list[3]
        return score
