from rich.console import Console
from rich.table import Table
from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or, QueryBuilder

def main():
    console = Console()
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(10, "goals"),
        HasAtLeast(20, "assists"),
        PlaysIn("PHI")
    )
    print()

    table = Table(title = "SELECTED PLAYERS", title_style = 'bold dark_violet', safe_box=True)
    table.add_column(f"Player", justify='left', style="navy_blue", no_wrap=True)
    table.add_column(f"Team", style="purple4")
    table.add_column(f"Stats", justify='right', style='green4')

    for player in stats.matches(matcher):
        table.add_row(player.playerprint()[0], player.playerprint()[1],player.playerprint()[2])
    #console = Console()
    console.print(table)
    message = "Retrieving selected players"
    print("\n")
    console = Console()
    grid = Table.grid(expand=True)
    grid.add_column(max_width=35)
    grid.add_column(justify="left")
    grid.add_column(width=20)
    grid.add_row(f"[deep_sky_blue4] {message}", "[bold magenta]READY[green4] :fire:", "")
    console.print(grid)
    print("\n")

    query = QueryBuilder()
    matcher = query.playsIn("NYR").hasAtLeast(10, "goals").hasFewerThan(20, "goals").build()

    for player in stats.matches(matcher):
        print(player)

    m1 = (
        query
            .playsIn("PHI")
            .hasAtLeast(10, "assists")
            .hasFewerThan(5, "goals")
            .build()
        )

    m2 = (
        query
            .playsIn("EDM")
            .hasAtLeast(50, "points")
            .build()
    )
    print()
    query = QueryBuilder()
    matcher = query.oneOf(m1, m2).build()

    for player in stats.matches(matcher):
        print(player)

if __name__ == "__main__":
    main()
