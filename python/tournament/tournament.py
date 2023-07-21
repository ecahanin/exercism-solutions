
POINTS = {
    'win': 3,
    'loss': 0,
    'draw': 1
}


def tally(rows):
    teams = {}
    for row in rows:
        team1, team2, result = row.split(';')
        if team1 not in teams:
            teams[team1] = initialize_team(team1)    
        if team2 not in teams:
            teams[team2] = initialize_team(team2)
        if result == 'win':
            win(teams[team1])
            loss(teams[team2])
        elif result == 'loss':
            loss(teams[team1])
            win(teams[team2])
        elif result == 'draw':
            draw(teams[team1])
            draw(teams[team2])

    return build_grid(teams)


def initialize_team(name):
    return {
        'Team': name,
        'MP': 0,
        'W' : 0,
        'D' : 0,
        'L' : 0,
        'P' : 0
    }


def win(team):
    team['MP'] += 1
    team['W'] += 1
    team['P'] += POINTS['win']


def loss(team):
    team['MP'] += 1
    team['L'] += 1


def draw(team):
    team['MP'] += 1
    team['D'] += 1
    team['P'] += POINTS['draw']


def build_grid(teams):
    headers = ("Team", "MP", "W", "D", "L", "P")
    grid = [format_line(headers)]
    teams = sorted(teams.values(), key=lambda team: team['Team'])
    for team in sorted(teams, key=lambda team: team['P'], reverse=True):
        grid.append(format_line(team.values()))
    return grid


def format_line(cols):
    column_lengths = (30, 2, 2, 2, 2, 2)
    formatted_cols = []
    for i, col in enumerate(cols):
        col = str(col)
        if i == 0:
            formatted_cols.append(col.ljust(column_lengths[i]))
        else:
            formatted_cols.append(col.rjust(column_lengths[i]))
    return " | ".join(formatted_cols)
