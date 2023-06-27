
rows, cols = (3,3)

board= [[0 for i in range(cols)] for j in range(rows)]
def game_history():
    print("\nGame Previous Match Winners")
    with open("game.txt") as f:
            for read in f:
                print(read, end = '')
def check(board,set,dice):
    if(board[0][0]=='X' and board[0][1]=='X' and board[0][2]=='X'):
        print("Winner is ",player1)
        with open("game.txt",'a') as f:
            f.write("Winner\n")
            f.write(player1)
            f.write("\n")
        set=1
    elif(board[1][0]=='X' and board[1][1]=='X' and board[1][2]=='X'):
        print("Winner is ",player1)
        with open("game.txt",'a') as f:
            f.write("Winner\n")
            f.write(player1)
            f.write("\n")
        set=1
    elif(board[2][0]=='X' and board[2][1]=='X' and board[2][2]=='X'):
        print("Winner is ",player1)
        with open("game.txt",'a') as f:
            f.write("Winner\n")
            f.write(player1)
            f.write("\n")
        set=1
    elif(board[0][0]=='X' and board[1][0]=='X' and board[2][0]=='X'):
        print("Winner is ",player1)
        with open("game.txt",'a') as f:
            f.write("Winner\n")
            f.write(player1)
            f.write("\n")
        set=1
    elif(board[0][1]=='X' and board[1][1]=='X' and board[2][1]=='X'):
        print("Winner is ",player1)
        with open("game.txt",'a') as f:
            f.write("Winner\n")
            f.write(player1)
            f.write("\n")
        set=1
    elif(board[0][2]=='X' and board[1][2]=='X' and board[2][2]=='X'):
        print("Winner is ",player1)
        with open("game.txt",'a') as f:
            f.write("Winner\n")
            f.write(player1)
            f.write("\n")
        set=1
    elif(board[0][0]=='X' and board[1][1]=='X' and board[2][2]=='X'):
        print("Winner is ",player1)
        with open("game.txt",'a') as f:
            f.write("Winner\n")
            f.write(player1)
            f.write("\n")
        set=1
    elif(board[0][2]=='X' and board[1][1]=='X' and board[2][0]=='X'):
        print("Winner is ",player1)
        with open("game.txt",'a') as f:
            f.write("Winner\n")
            f.write(player1)
            f.write("\n")
        set=1

    if(board[0][0]=='O' and board[0][1]=='O' and board[0][2]=='O'):
        print("Winner is ",player2)
        with open("game.txt",'a') as f:
            f.write("Winner\n")
            f.write(player2)
            f.write("\n")
        set=1
    elif(board[1][0]=='O' and board[1][1]=='O' and board[1][2]=='O'):
        print("Winner is ",player2)
        with open("game.txt",'a') as f:
            f.write("Winner\n")
            f.write(player2)
            f.write("\n")
        set=1
    elif(board[2][0]=='O' and board[2][1]=='O' and board[2][2]=='O'):
        print("Winner is ",player2)
        with open("game.txt",'a') as f:
            f.write("Winner\n")
            f.write(player2)
            f.write("\n")
        set=1
    elif(board[0][0]=='O' and board[1][0]=='O' and board[2][0]=='O'):
        print("Winner is ",player2)
        with open("game.txt",'a') as f:
            f.write("Winner\n")
            f.write(player2)
            f.write("\n")
        set=1
    elif(board[0][1]=='O' and board[1][1]=='O' and board[2][1]=='O'):
        print("Winner is ",player2)
        with open("game.txt",'a') as f:
            f.write("Winner\n")
            f.write(player2)
            f.write("\n")
        set=1
    elif(board[0][2]=='O' and board[1][2]=='O' and board[2][2]=='O'):
        print("Winner is ",player2)
        with open("game.txt",'a') as f:
            f.write("Winner\n")
            f.write(player2)
            f.write("\n")
        set=1
    elif(board[0][0]=='O' and board[1][1]=='O' and board[2][2]=='O'):
        print("Winner is ",player2)
        with open("game.txt",'a') as f:
            f.write("Winner\n")
            f.write(player2)
            f.write("\n")
        set=1
    elif(board[0][2]=='O' and board[1][1]=='O' and board[2][0]=='O'):
        print("Winner is ",player2)
        with open("game.txt",'a') as f:
            f.write("Winner\n")
            f.write(player2)
            f.write("\n")
        set=1
    if(board[0][0]!=0 and board[0][1]!=0 and board[0][2]!=0 and board[1][0]!=0 and board[1][1]!=0 and board[1][2]!=0 and board[2][0]!=0 and board[2][1]!=0 and board[2][2]!=0):
        print("Match Draw")
        with open("game.txt",'a') as f:
            f.write("Draw")
            f.write("\n")
        set=1
    if(set==0):
        roll_dice(dice)
def Display_Board(row,col,dice,set):
        if(dice ==0):
            piece='X'
            if(board[row][col]==0):
                board[row][col]=piece
            else:
                roll_dice(dice)
        elif(dice==1):
            piece='O'
            if(board[row][col]==0):
                board[row][col]=piece
            else:
                roll_dice(dice)
        print(board[0][0] , "|" , board[0][1] , "|" , board[0][2])
        print("----------")
        print(board[1][0] , "|" , board[1][1] , "|" , board[1][2])
        print("----------")
        print(board[2][0] , "|" , board[2][1] , "|" , board[2][2])
        dice+=1;
        if dice%2==0:
            dice=0
        check(board,set,dice)
def roll_dice(dice):
    if(dice==0):
        print("Player_1\t\t")
    elif(dice==1):
        print("Player_2\t\t")
    row=int(input("Enter Row"))
    col=int(input("Enter Column"))
    Display_Board(row,col,dice,set)

player1=input("Enter Player1 Name")
player2=input("Enter Player2 Name")
dice=0
set=0
roll_dice(dice)
game_history()

