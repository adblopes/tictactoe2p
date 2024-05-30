import console_movement
from os import system, name

playsX = []
playsO = []
win = False

def main():
    input("Let's play tic-tac-toe! Note: This version is 2 player only")
    play()

def drawBoard():
    print("Move the cursor with the arrow keys and press ENTER to make your play.")
    print("        |     |       ")
    print("        |     |       ")
    print("   _____|_____|_____  ")
    print("        |     |       ")
    print("        |     |       ")
    print("   _____|_____|_____  ")
    print("        |     |       ")
    print("        |     |       ")
    print("        |     |       ")

def clear():
    system("cls") if name == "nt" else system("clear")

def play():
    global win, playsX, playsO

    win = False
    round = 0
    playsX.clear()
    playsO.clear()

    clear()
    drawBoard()
    console_movement.move_cursor(0,0)

    while(win != True):
        coords = ()
        player = "X" if round % 2 == 0 else "O"
        
        try:
            coords = console_movement.run_cursor_movement()
            if coords is None:
                raise KeyboardInterrupt
        except KeyboardInterrupt:
            clear()
            print("Program interrupted by user. Exiting...")
            break

        coords = validate_coords(coords, player)
        if coords is not None:
            console_movement.replace_at_position(player, coords[0], coords[1])
            round += 1

            if win:
                input(f"Player {player} has won! Press ENTER to play again.")
                play()

            if (round == 9):
                input("It's a tie! Press ENTER to settle the score!")
                play()

# verify cursor is in valid position and centers inputs 
def validate_coords(coords, player):
    match coords:
        case (x, y) if 3 <= coords[1] <= 7 and 1 <= coords[0] <= 3:
            coords =  (2,5)
        case (x, y) if 9 <= coords[1] <= 13 and 1 <= coords[0] <= 3:
            coords =  (2,11)
        case (x, y) if 15 <= coords[1] <= 19 and 1 <= coords[0] <= 3:
            coords =  (2,17)
        case (x, y) if 3 <= coords[1] <= 7 and 4 <= coords[0] <= 6:
            coords =  (5,5)
        case (x, y) if 9 <= coords[1] <= 13 and 4 <= coords[0] <= 6:
            coords =  (5,11)
        case (x, y) if 15 <= coords[1] <= 19 and 4 <= coords[0] <= 6:
            coords =  (5,17)
        case (x, y) if 3 <= coords[1] <= 7 and 7 <= coords[0] <= 9:
            coords =  (8,5)
        case (x, y) if 9 <= coords[1] <= 13 and 7 <= coords[0] <= 9:
            coords =  (8,11)
        case (x, y) if 15 <= coords[1] <= 19 and 7 <= coords[0] <= 9:
            coords =  (8,17)
        case _:
            coords =  None
    
    return check_rules(player, coords)

def check_rules(player, coords):
    global win, playsX, playsO
    countLines = 0
    countColunms = 0

    if coords is None or player in playsX or player in playsO:
        return None
    
    elif player == "X":
        playsX.append(coords)

        # check diagonals
        if (5,11) in playsX:
            if (2,5) in playsX and (8,17) in playsX or (2,17) in playsX and (8,5) in playsX:
                win = True

        for i in playsX:
            if i[0] == coords[0]:
                countColunms += 1
            if i[1] == coords[1]:
                countLines += 1
            if countLines == 3 or countColunms == 3:
                win = True            

    elif player == "O":
        playsO.append(coords)
        
        # check diagonals
        if (5,11) in playsO:
            if (2,5) in playsO and (8,17) in playsO or (2,17) in playsO and (8,5) in playsO:
                win = True

        for i in playsO:
            if i[0] == coords[0]:
                countColunms += 1
            if i[1] == coords[1]:
                countLines += 1
            if countLines == 3 or countColunms == 3:
                win = True
    
    return coords

main()    