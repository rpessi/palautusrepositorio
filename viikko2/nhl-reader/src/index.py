import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response[0])

    players = []

    for player_dict in response:
        player = Player(player_dict)
        if player.nationality == 'FIN':
            players.append(player)
        players.sort(key=lambda x: x.points, reverse=True)

    print("Players from FIN:\n")

    #print(players[0])
    for player in players:
        print(player)

if __name__ == "__main__":
    main()
