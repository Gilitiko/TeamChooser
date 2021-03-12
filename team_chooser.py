import random

NUM_OF_TEAMS = 3
MAX_SCORE_DIFF = 12

def calc_team_score(team):
    return sum([x[1] for x in team])


def sort_teams(teams):
    teams.sort(key=lambda x: calc_team_score(x))

def _build_teams(players):
    teams = []
    players = sorted(players, key=lambda x: x[1], reverse=True)
    average_score = sum([x[1] for x in players]) / len(players)
    team_size = len(players) / NUM_OF_TEAMS
    top_players = players[:NUM_OF_TEAMS]
    players = players[NUM_OF_TEAMS:]
    for top_player in top_players:
        teams.append([top_player])
    ideal_team_score = average_score * team_size
    while len(players) > 0:
        sort_teams(teams)
        random_players = random.sample(players, NUM_OF_TEAMS)
        random_players.sort(key=lambda x: x[1], reverse=True)
        for i in range(len(teams)):
            teams[i].append(random_players[-i])
            players.remove(random_players[i])
    for team in teams:
        team.sort(key=lambda x: x[1], reverse=True)
    return teams
    print("Ideal score: {}".format(ideal_team_score))
    for i in range(len(teams)):
        print("Team{}: {}".format(i, calc_team_score(teams[i])))
        
        


def good_build_teams(players, bad_pairs):
    average_score = sum([x[1] for x in players]) / len(players)
    team_size = len(players) / NUM_OF_TEAMS
    ideal_team_score = average_score * team_size
    while True:
        teams = _build_teams(players)
        bad_team = False
        for pair in bad_pairs:
            pair = set(pair)
            for team in teams:
                just_players = {p[0] for p in team}
                if pair.issubset(just_players):
                    bad_team = True
        if bad_team:
            continue
        sort_teams(teams)
        score_difference = calc_team_score(teams[NUM_OF_TEAMS-1]) - calc_team_score(teams[0])
        if score_difference < MAX_SCORE_DIFF:
            return teams
 
 
 
def show_team_options(players, options=3, bad_pairs=[]):
    for i in range(options):
        print("Option {}:\n".format(i + 1))
        good_teams = good_build_teams(players, bad_pairs)
        for i in range(len(good_teams)):
            print("Team {}: {}".format(i+1, calc_team_score(good_teams[i])))
            for player in good_teams[i]:
                print(player[0])
            print("")
        print("------------------")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    