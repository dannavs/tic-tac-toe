import random

values_dict = {}
row_1 = row_2 = row_3 = horiz = ""


def set_values(the_key):
    global values_dict

    values_dict = {
        "a": the_key,
        "b": the_key,
        "c": the_key,
        "d": the_key,
        "e": the_key,
        "f": the_key,
        "g": the_key,
        "h": the_key,
        "i": the_key,
    }
    print(f"Values of boxes set as: {values_dict}")


def draw_grid():
    global row_1, row_2, row_3, horiz
    row_1 = f"  {values_dict["a"]}  |  {values_dict["b"]}  |  {values_dict["c"]}        ||         a | b | c"
    row_2 = f"  {values_dict["d"]}  |  {values_dict["e"]}  |  {values_dict["f"]}        ||   Key:  d | e | f"
    row_3 = f"  {values_dict["g"]}  |  {values_dict["h"]}  |  {values_dict["i"]}        ||         g | h | i"
    horiz = f" - - - - - - - -       ||         --|---|--"
    print("")
    print(row_1)
    print(horiz)
    print(row_2)
    print(horiz)
    print(row_3)
    print("")


def welcome():
    set_values(" ")
    draw_grid()


def check_open_positions():
    open_positions_list = []
    # print(values_dict)
    for key in values_dict:
        if values_dict.get(key) == " ":
            open_positions_list.append(key)
    return open_positions_list


def check_for_winner():
    global game_on
    if (values_dict["a"] == values_dict["b"] == values_dict["c"] == "X"
            or values_dict["d"] == values_dict["e"] == values_dict["f"] == "X"
            or values_dict["g"] == values_dict["h"] == values_dict["i"] == "X"
            or values_dict["a"] == values_dict["d"] == values_dict["g"] == "X"
            or values_dict["b"] == values_dict["e"] == values_dict["h"] == "X"
            or values_dict["c"] == values_dict["f"] == values_dict["i"] == "X"
            or values_dict["a"] == values_dict["e"] == values_dict["i"] == "X"
            or values_dict["c"] == values_dict["e"] == values_dict["g"] == "X"):
        return "X WINNER"
    elif (values_dict["a"] == values_dict["b"] == values_dict["c"] == "O"
          or values_dict["d"] == values_dict["e"] == values_dict["f"] == "O"
          or values_dict["g"] == values_dict["h"] == values_dict["i"] == "O"
          or values_dict["a"] == values_dict["d"] == values_dict["g"] == "O"
          or values_dict["b"] == values_dict["e"] == values_dict["h"] == "O"
          or values_dict["c"] == values_dict["f"] == values_dict["i"] == "O"
          or values_dict["a"] == values_dict["e"] == values_dict["i"] == "O"
          or values_dict["c"] == values_dict["e"] == values_dict["g"] == "O"):
        return "O WINNER"
    else:
        return  # No winner yet


game_on = True

welcome()  # set the board up
player_1 = input("The game is ready! Input Player One's name: ")  # Player One's name
player_2 = input("Please input Player Two's name (type computer if vs. random computer) : ")  # Player Two's name
player = random.choice([player_1, player_2])  # Random choice of first player
print(f"Game on! First player is: {player}! You play X!")  # Let the first player know they're playing X
if player == player_1:  # Set the correct signs to the first/second players
    player_1_sign = "X"
    player_2_sign = "O"
else:
    player_1_sign = "O"
    player_2_sign = "X"

while game_on:
    # print(f"Player is {player}")
    open_positions = check_open_positions()
    if not open_positions:
        print("Board full, game over with a tie.")
        game_on = False

    if player.lower() == "computer":
        if player == player_1:
            player_1_sign_pos = random.choice(open_positions)
            open_positions.index(player_1_sign_pos) # Do I still need to check?
            values_dict[player_1_sign_pos] = player_1_sign
            player = player_2
            print(f"Computer randomly played {player_1_sign_pos}")
        elif player == player_2:
            player_2_sign_pos = random.choice(open_positions)
            open_positions.index(player_2_sign_pos) # Do I still need to check?
            values_dict[player_2_sign_pos] = player_2_sign
            player = player_1
            print(f"Computer randomly played {player_2_sign_pos}")
        else:
            print("Computer Player Error #1")


    else:
        if player == player_1:
            print("-------------------------------------------------------------")
            print(f"{player_1} playing {player_1_sign}")
            draw_grid()
            # print(f"Current values_dict: {values_dict}")
            player_1_sign_pos = input(
                f"Available positions are ({" ".join(open_positions)}). Which position will you play {player_1_sign}? ")
            try:
                open_positions.index(player_1_sign_pos)
            except ValueError:
                print("Bad position choice. Lose a turn")
            else:
                values_dict[player_1_sign_pos] = player_1_sign
            finally:
                player = player_2

        elif player == player_2:
            print("-------------------------------------------------------------")
            print(f"{player_2} playing {player_2_sign}")
            draw_grid()
            # print(f"Current values_dict: {values_dict}")
            player_2_sign_pos = input(
                f"Available positions are ({" ".join(open_positions)}). Which position will you play {player_2_sign}? ")
            try:
                open_positions.index(player_2_sign_pos)
            except ValueError:
                print("Bad position choice. Lose a turn")
            else:
                values_dict[player_2_sign_pos] = player_2_sign
            finally:
                player = player_1

        else:
            print("Player is neither.")

        if check_for_winner() == "X WINNER":
            print(" X WINS ")
            print(" X WINS ")
            print(" X WINS ")
            if player_1_sign == "X":
                print(f"{player_1} has won!")
            else:
                print(f"{player_2} has won!")
            game_on = False

        elif check_for_winner() == "O WINNER":
            print(" O WINS ")
            print(" O WINS ")
            print(" O WINS ")
            if player_1_sign == "O":
                print(f"{player_1} has won!")
            else:
                print(f"{player_2} has won!")
            game_on = False

        else:
            pass