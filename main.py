import os


class Player:
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, weight_kg=weight_kg, height_cm=height_cm)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, weight_kg=weight_kg, height_cm=height_cm)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


def adding_player(sport):
    print(f"Add data of your favorite football player")

    if sport == "basketball":

        f_name = input("First name: ")
        l_name = input("Last name: ")
        height_in_cm = input("Height (cm): ")
        weight_in_kg = input("Weight (kg): ")
        points_scored = input("Points scored: ")
        rebounds_succeeded = input("Rebounds: ")
        assist_succeeded = input("Assists: ")

        new_player = FootballPlayer(f_name, l_name, height_in_cm, weight_in_kg, points_scored, rebounds_succeeded,
                                    assist_succeeded)

        with open("basketball_players.json", "a") as players_data:
            players_data.write(str(new_player.__dict__))
            print("Player successfully added!")

        return f"New players data: {new_player.__dict__}"

    elif sport == "football":

        f_name = input("First name: ")
        l_name = input("Last name: ")
        height_in_cm = input("Height (cm): ")
        weight_in_kg = input("Weight (kg): ")
        goals_scored = input("Goals scored: ")
        yellow_card = input("Yellow cards: ")
        red_card = input("Red cards: ")

        new_player = FootballPlayer(f_name, l_name, height_in_cm, weight_in_kg, goals_scored, yellow_card, red_card)

        with open("football_players.json", "a") as players_data:
            players_data.write(str(new_player.__dict__))
            print("Player successfully added!")

        return f"New players data: {new_player.__dict__}"


def reading_data(sport):
    if os.path.exists(f"{sport}_players.json"):
        with open(f"{sport}_players.json", "r") as players_data:
            data = players_data.read()
            print(f"{sport.capitalize()} players in your list:\n{data}")
    else:
        print("You don't have any players in your list.")


while True:
    task = input("Do you want to add player or read data? (add/read): ").lower()

    if task == "add":
        basketball_or_football = input("Which player do you want to add to your list? (basketball/football): ").lower()

        if basketball_or_football == "basketball":
            adding_player(basketball_or_football)
        elif basketball_or_football == "football":
            adding_player(basketball_or_football)
        else:
            print("You can only add basketball or football players. Try again.")
    elif task == "read":
        basketball_or_football = input("Which list do you want to read? (basketball/football): ").lower()

        if basketball_or_football == "football":
            reading_data("football")
        elif basketball_or_football == "basketball":
            reading_data("basketball")

    exit_loop = input("Dou you want to do something else or do you want to exit? (more/exit): ")

    if exit_loop == "exit":
        break
