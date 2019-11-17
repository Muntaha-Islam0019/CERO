import random

print(
    '''Hey there!
Welcome to CERO.
To play the game, type '?p' or 'play'.
To know about the rules, type '?h' or 'help'.
'''
)

cards = [
    "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9", "b10",
    "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10",
    "r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "r9", "r10",
    "o1", "o2", "o3", "o4", "o5", "o6", "o7", "o8", "o9", "o10",
    "i1", "i2", "i3", "i4", "i5", "i6", "i7", "i8", "i9", "i10",
    "Uno", "Dos", "Tres", "Cuatro", "Cinco"
]


def game_help():
    print(
        '''Here I have 55 cards.
50 of them are of 5 different colors; Black, Cyan, Red, Orange, Indigo.
The other 5 are called Uno, Dos, Tres, Cuatro, Cinco.
This game can be played by more than one number of players.
You'll give me a number more than 20 to deal with.
Now a player will turn the 'Wheel of luck'.
If in those numbers you have 3 or more colors with even numbers, you'll get 2 points.
If you get Uno, you'll get 1 points, for Dos, 2 and so on.
The player with most points will win.
If they are still tied, then there would be a toss.
'''
    )


def point_counter(player):

    point = 0

    black = 0
    cyan = 0
    red = 0
    orange = 0
    indigo = 0

    for item in player:

        if item == "Uno":
            point += 1
        elif item == "Dos":
            point += 2
        elif item == "Tres":
            point += 3
        elif item == "Cuatro":
            point += 4
        elif item == "Cinco":
            point += 5
        elif str(item).startswith('b'):
            black += 1
        elif str(item).startswith('c'):
            cyan += 1
        elif str(item).startswith('r'):
            red += 1
        elif str(item).startswith('o'):
            orange += 1
        elif str(item).startswith('i'):
            indigo += 1

    if black % 2 == 0:
        point += 2

    if cyan % 2 == 0:
        point += 2

    if red % 2 == 0:
        point += 2

    if orange % 2 == 0:
        point += 2

    if indigo % 2 == 0:
        point += 2

    return point


def result(players, players_points):

    max_points = 0

    for count in range(0, len(players)):

        print(f"Player {count + 1}'s cards: {players[count]}.")
        print(f"Player {count + 1}'s points: {players_points[count]}.")
        print()

        if players_points[count] > max_points:
            max_points = players_points[count]

    winners = []

    for count in range(0, len(players)):

        if players_points[count] == max_points:
            winners.append(count)

    print(f"Thus, the winner is: Player {random.choice(winners) + 1}!")


def game_play():

    global card_count
    player_count = 0
    integer_check_players = False

    while integer_check_players is not True:
        try:
            player_count = int(input("Please enter the number of players: "))
            print()

            if player_count > 1:
                integer_check_players = True
            else:
                print("Please enter a number larger than 1.")
                print()
                integer_check_players = False
        except:
            print("Please enter an integer.")
            print()
            integer_check_players = False

    integer_check_cards = False

    while integer_check_cards is not True:
        try:
            card_count = int(input("Please enter the number of cards: "))
            print()

            if card_count > 20:
                integer_check_cards = True
            else:
                print("Please enter a number larger than 20.")
                print()
                integer_check_cards = False
        except:
            print("Please enter an integer.")
            print()
            integer_check_cards = False

    players = []
    players_points = []

    for count in range(0, player_count):

        player = random.sample(cards, card_count)
        players.append(player)

        point = point_counter(player)
        players_points.append(point)

        print(f"Player {count + 1}'s 'Wheel of luck' has rolled!")
        print()

    reply_result = input("Wanna see the results? Reply with 'yes' or '?y' to get surprised: ")
    print()

    if reply_result == "yes" or reply_result == "?y":
        result(players, players_points)
    else:
        print("Well, I wanna show them as I've already calculated them!")
        print()
        result(players, players_points)


check = False
while check is not True:

    init_input = input("Please type here: ")
    print()

    if init_input == "?h" or init_input == "help":

        check = True
        game_help()

        reply = input("Wanna play right now? Reply with 'yes' or '?y' to play: ")
        print()

        if reply == "yes" or reply == "?y":
            game_play()

    elif init_input == "?p" or init_input == "play":
        check = True
        game_play()
    else:
        check = False
        print("Please enter a valid input: ")
        print()

print("Thanks for visiting, see you around!")
