def matrix_printer():
    print("-" * 9)
    print("|", " ".join(row_1), "|")
    print("|", " ".join(row_2), "|")
    print("|", " ".join(row_3), "|")
    print("-" * 9)
    return


row_1 = [" " for i in range(3)]
row_2 = [" " for j in range(3)]
row_3 = [" " for k in range(3)]

matrix_printer()
counter = 1

while True:
    row_coord, col_coord = input("Enter the coordinates: ").split()
    row_int = int(row_coord)
    col_int = int(col_coord)
    if row_coord.isdigit() is False or col_coord.isdigit() is False:
        print("You should enter numbers!")
    elif (0 < row_int > 3) or (0 < col_int > 3):
        print("Coordinates should be from 1 to 3!")
    else:
        #  selecting next player
        if counter % 2 == 1:
            player = "X"
        else:
            player = "O"
        if row_int == 1 and row_1[col_int - 1] == " ":
            row_1[col_int - 1] = player
            counter += 1
            matrix_printer()
        elif row_int == 2 and row_2[col_int - 1] == " ":
            row_2[col_int - 1] = player
            counter += 1
            matrix_printer()
        elif row_int == 3 and row_3[col_int - 1] == " ":
            row_3[col_int - 1] = player
            counter += 1
            matrix_printer()
        else:
            print("This cell is occupied! Choose another one!")
        winner_1 = row_1[0] == row_1[1] == row_1[2] == player
        winner_2 = row_2[0] == row_2[1] == row_2[2] == player
        winner_3 = row_3[0] == row_3[1] == row_1[2] == player
        winner_4 = row_1[0] == row_2[0] == row_3[0] == player
        winner_5 = row_1[1] == row_2[1] == row_3[1] == player
        winner_6 = row_1[2] == row_2[2] == row_3[2] == player
        winner_7 = row_1[0] == row_2[1] == row_3[2] == player
        winner_8 = row_1[2] == row_2[1] == row_3[0] == player
        winner = [winner_1, winner_2, winner_3, winner_4, winner_5, winner_6, winner_7, winner_8]
        if any(winner):
            print(f"{player} wins")
            break
        elif " " not in row_1 and " " not in row_2 and " " not in row_3 and not any(winner):
            print("Draw")
            break
