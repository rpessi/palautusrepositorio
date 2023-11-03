import unittest
from statistics_service import SortBy, StatisticsService
from statistics_service import sort_by_points, sort_by_goals, sort_by_assists
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_players_by_team(self):
        players = self.stats.team("PIT")
        self.assertEqual(1, len(players))
        players = self.stats.team("EDM")
        self.assertEqual(3, len(players))
        player = self.stats.team("DET")[0]
        self.assertEqual(player.name, "Yzerman")

    def test_player_points(self):
        player = self.stats.team("DET")[0]
        points = sort_by_points(player)
        self.assertEqual(points, 98)

    def test_search_works(self):
        players = self.stats
        player = players.search("Kurri")
        self.assertEqual(player.name, "Kurri")
        player = players.search("Greztky")
        self.assertEqual(player, None)

    def test_top_ranking_by_points_works(self):
        players = self.stats
        top_5 = players.top(5)
        self.assertEqual(len(top_5), 5)
        self.assertEqual(top_5[0].points, 124)
        self.assertEqual(top_5[1].points, 99)
        top_5 = players.top(5, SortBy.POINTS)
        self.assertEqual(len(top_5), 5)
        self.assertEqual(sort_by_points(top_5[0]), 124)
        self.assertEqual(sort_by_points(top_5[4]), 16)
        
    def test_top_ranking_by_goals_works(self):
        players = self.stats
        top_5 = players.top(5, SortBy.GOALS)
        self.assertEqual(len(top_5), 5)
        self.assertEqual(top_5[0].goals, 45)
        self.assertEqual(top_5[0].name, "Lemieux")
        self.assertEqual(top_5[1].goals, 42)

    def test_top_ranking_by_assists_works(self):
        players = self.stats
        top_5 = players.top(5, SortBy.ASSISTS)
        self.assertEqual(len(top_5), 5)
        self.assertEqual(top_5[0].assists, 89)
        self.assertEqual(top_5[0].name, "Gretzky")
        self.assertEqual(top_5[1].assists, 56)
