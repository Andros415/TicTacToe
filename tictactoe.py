playerSym = {"P1": 'X', "P2": 'O'}
playerPos = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9}
H2H = {"P1": 0 , "P2": 0}
numTurns = 0
validinput = False
hasWonP1 = False
rematch = True
def markpos(player,pos):
        playerPos[pos] = playerSym[player]

def checkWin(player):
    return (playerPos[1] == playerSym[player] and playerPos[2] == playerSym[player] and playerPos[3] == playerSym[player]) or (playerPos[4] == playerSym[player] and playerPos[5] == playerSym[player] and playerPos[6] == playerSym[player]) or (playerPos[7] == playerSym[player] and playerPos[8] == playerSym[player] and playerPos[9] == playerSym[player]) or (playerPos[1] == playerSym[player] and playerPos[4] == playerSym[player] and playerPos[7] == playerSym[player]) or (playerPos[2] == playerSym[player] and playerPos[5] == playerSym[player] and playerPos[8] == playerSym[player]) or (playerPos[3] == playerSym[player] and playerPos[6] == playerSym[player] and playerPos[9] == playerSym[player]) or (playerPos[1] == playerSym[player] and playerPos[5] == playerSym[player] and playerPos[9] == playerSym[player]) or (playerPos[3] == playerSym[player] and playerPos[5] == playerSym[player] and playerPos[7] == playerSym[player])
 
def checkTie():
    return not checkWin("P1") and not checkWin("P2") and numTurns == 9
        
print("Welcome to Tic Tac Toe!")
while rematch:
    playerPos = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9}
    hasWonP1 = False
    numTurns = 0
    playsym = input("Player 1: Do you want to be X or O? ")
    if playsym.upper() == 'O':
        playerSym["P1"] = 'O'
        playerSym["P2"] = 'X' 
        print("Player 2 will go first. Let's play!")
        while hasWonP1 == False:
            print(f"     |     |     \n  {playerPos[1]}  |  {playerPos[2]}  |  {playerPos[3]}    \n     |     |     \n------------------ \n     |     |     \n  {playerPos[4]}  |  {playerPos[5]}  |  {playerPos[6]}   \n     |     |     \n------------------ \n     |     |     \n  {playerPos[7]}  |  {playerPos[8]}  |  {playerPos[9]}  \n     |     |     \n")
            while validinput == False:
                playpos = int(input("Player 2: Choose your next position: "))
                if playpos in range(0,10):
                    if playerPos[playpos] != 'X' and playerPos[playpos] != 'O':
                        break
                print("Number not in range or has already been marked. Try Again")    
            markpos("P2", playpos)
            numTurns += 1
            print(f"     |     |     \n  {playerPos[1]}  |  {playerPos[2]}  |  {playerPos[3]}    \n     |     |     \n------------------ \n     |     |     \n  {playerPos[4]}  |  {playerPos[5]}  |  {playerPos[6]}   \n     |     |     \n------------------ \n     |     |     \n  {playerPos[7]}  |  {playerPos[8]}  |  {playerPos[9]}  \n     |     |     \n")
            if checkWin("P2"):
                break
            if checkTie():
                break
            while validinput == False:
                playpos = int(input("Player 1: Choose your next position: "))
                if playpos in range(0,10):
                    if playerPos[playpos] != 'X' and playerPos[playpos] != 'O':
                        break
                print("Number not in range or has already been marked. Try Again")    
            markpos("P1", playpos)
            numTurns += 1
            print(f"     |     |     \n  {playerPos[1]}  |  {playerPos[2]}  |  {playerPos[3]}    \n     |     |     \n------------------ \n     |     |     \n  {playerPos[4]}  |  {playerPos[5]}  |  {playerPos[6]}   \n     |     |     \n------------------ \n     |     |     \n  {playerPos[7]}  |  {playerPos[8]}  |  {playerPos[9]}  \n     |     |     \n")
            if checkWin("P1"):
                hasWonP1 = True
                break
            if checkTie():
                break
    else:    
        print("Player 1 will go first. Let's play!")
        while hasWonP1 == False:
            print(f"     |     |     \n  {playerPos[1]}  |  {playerPos[2]}  |  {playerPos[3]}    \n     |     |     \n------------------ \n     |     |     \n  {playerPos[4]}  |  {playerPos[5]}  |  {playerPos[6]}   \n     |     |     \n------------------ \n     |     |     \n  {playerPos[7]}  |  {playerPos[8]}  |  {playerPos[9]}  \n     |     |     \n")
            while validinput == False:
                playpos = int(input("Player 1: Choose your next position: "))
                if playpos in range(0,10):
                    if playerPos[playpos] != 'X' and playerPos[playpos] != 'O':
                        break
                print("Number not in range or has already been marked. Try Again")    
            markpos("P1", playpos)
            numTurns += 1
            print(f"     |     |     \n  {playerPos[1]}  |  {playerPos[2]}  |  {playerPos[3]}    \n     |     |     \n------------------ \n     |     |     \n  {playerPos[4]}  |  {playerPos[5]}  |  {playerPos[6]}   \n     |     |     \n------------------ \n     |     |     \n  {playerPos[7]}  |  {playerPos[8]}  |  {playerPos[9]}  \n     |     |     \n")
            if checkWin("P1"):
                hasWonP1 = True
                break
            if checkTie():
                break
            while validinput == False:
                playpos = int(input("Player 2: Choose your next position: "))
                if playpos in range(0,10):
                    if playerPos[playpos] != 'X' and playerPos[playpos] != 'O':
                        break
                print("Number not in range or has already been marked. Try Again")    
            markpos("P2", playpos)
            numTurns += 1
            print(f"     |     |     \n  {playerPos[1]}  |  {playerPos[2]}  |  {playerPos[3]}    \n     |     |     \n------------------ \n     |     |     \n  {playerPos[4]}  |  {playerPos[5]}  |  {playerPos[6]}   \n     |     |     \n------------------ \n     |     |     \n  {playerPos[7]}  |  {playerPos[8]}  |  {playerPos[9]}  \n     |     |     \n")
            if checkWin("P2"):
                break
            if checkTie():
                break
    if checkTie():
        print("It's a Tie! Do a rematch to find out the real winner!")
    else:    
        if hasWonP1:
             print("Congratulations Player 1! You Won!")
             H2H["P1"] += 1
        else:
            print("Congratulations Player 2! You Won!")
            H2H["P2"] += 1
    print(f"Overall Head to Head: {H2H['P1']} vs. {H2H['P2']}")    
    rematchin = input("Rematch? (Enter 'yes' or 'no') ")    
    if rematchin.lower() == 'no':
        break

         