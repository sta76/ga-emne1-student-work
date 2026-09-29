def show_match_result(home_team,away_team, home_score, away_score):
    if home_score < away_score:
        won_by = away_score - home_score
        print(f"{away_team} vant kampen med {won_by} mål")
    elif home_score > away_score:
        won_by = home_score - away_score
        print(f"{home_team} vant kampen med {won_by} mål")
    else:
        print(f"Det ble uavgjort mellom {home_team} og {away_team} med {home_score}-{away_score}")


def get_team(prompt):
    while True:
        team = input(prompt).strip()
        if len(team) <= 0:
            print("Lagets navn kan ikke være tomt!")
            continue
        elif team.isdigit():
            print("Lagets navn skal ikke være tall!")
            continue
        return team


def get_score(prompt):
    while True:
        try:
            team_score = int(input(prompt))
            if team_score < 0:
                raise ValueError
            return team_score
        except ValueError:
            print("Antall mål skal være '0' eller positiv heltall!")



def main():

    home_team = get_team("Hva er navnet på hjemmelaget: ")
    home_score = get_score(f"Hvor mange mål scoret {home_team}: ")

    away_team = get_team("Hva heter bortelaget: ")
    away_score = get_score(f"Hvor mange mål scoret {away_team}: ")

    show_match_result(home_team, away_team, home_score, away_score)

if __name__ == "__main__":
    main()