teams = dict()

def read_input_file(fileName):
    '''
    get all lines from txt file as an array withouth the \n
    '''
    with open(fileName) as file:
        file_data = file.readlines()
    input_data = [element.strip() for element in file_data]
    return input_data

def add_team_to_dict(team):
    '''
    This is for adding the team to the dictionary if it's not in the dictionary
    '''
    global teams
    if team["name"] not in teams:
        teams[team["name"]] = 0
    return

def get_team_and_score(team):
    '''
    This is for getting the team's real name and it's score
    '''
    score = int(''.join(i for i in team if i.isdigit()))
    name = str(''.join(j for j in team if not j.isdigit())).rstrip()

    team_dict = {
        "name": name,
        "score": score,
    }

    return team_dict

def match_status(team_1, team_2):
    '''
    This is for getting the result of the match
    '''
    global teams
    if team_1["score"] > team_2["score"]:
        teams[team_1["name"]] += 3
    elif team_1["score"] < team_2["score"]:
        teams[team_2["name"]] += 3
    elif team_1["score"] == team_2["score"]:
        teams[team_1["name"]] += 1
        teams[team_2["name"]] += 1
    return

def sort_results_chart(final_status):
    '''
    This is for sorting the results chart by the highest score then by the alphabetical order
    '''
    sorted_teams = sorted(final_status.items(), key = lambda dict_element: (-dict_element[1], dict_element[0]))
    return sorted_teams

def main():
    global teams
    data_file = input("Please enter the filename: ")
    data = read_input_file(data_file);
    for match in data:
        team_1, team_2 = match.split(', ')
        team_1 = get_team_and_score(team_1)
        team_2 = get_team_and_score(team_2)
        add_team_to_dict(team_1)
        add_team_to_dict(team_2)
        match_status(team_1, team_2)
    tournament_result = sort_results_chart(teams)
    for num, element in enumerate(tournament_result):
        print(str(num + 1) + ".", element[0] + ",", element[1], "pts" if element[1] != 1 else "pt")

if __name__ == "__main__":
    main()