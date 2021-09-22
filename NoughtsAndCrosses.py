startRequest = input("Hello! Would you like to play 'Noughts and Crosses'? ").lower()
if startRequest != "yes" and startRequest != "y":
    quit()


def displayBoard(board):
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])


def checkIfWinner(boardType, opponent, differentiate, p1Score, p2Score, CPUScore):
    row1 = boardType[0] == boardType[1] == boardType[2]
    row2 = boardType[3] == boardType[4] == boardType[5]
    row3 = boardType[6] == boardType[7] == boardType[8]
    if row1:
        if differentiate == "CPU move":
            return True
        else:
            if boardType[0] == "X":
                print("Player 1 wins!")
                p1Score += 1
            else:
                print(opponent, "wins!")
                if opponent == p2Score:
                    p2Score += 1
                else:
                    CPUScore += 1
        scores = [p1Score, p2Score, CPUScore]
        return scores
    if row2:
        if differentiate == "CPU move":
            return True
        else:
            if boardType[3] == "X":
                print("Player 1 wins!")
                p1Score += 1
            else:
                print(opponent, "wins!")
                if opponent == p2Score:
                    p2Score += 1
                else:
                    CPUScore += 1
        scores = [p1Score, p2Score, CPUScore]
        return scores
    if row3:
        if differentiate == "CPU move":
            return True
        else:
            if boardType[6] == "X":
                print("Player 1 wins!")
                p1Score += 1
            else:
                print(opponent, "wins!")
                if opponent == p2Score:
                    p2Score += 1
                else:
                    CPUScore += 1
        scores = [p1Score, p2Score, CPUScore]
        return scores

    column1 = boardType[0] == boardType[3] == boardType[6]
    column2 = boardType[1] == boardType[4] == boardType[7]
    column3 = boardType[2] == boardType[5] == boardType[8]
    if column1:
        if differentiate == "CPU move":
            return True
        else:
            if boardType[0] == "X":
                print("Player 1 wins!")
                p1Score += 1
            else:
                print(opponent, "wins!")
                if opponent == p2Score:
                    p2Score += 1
                else:
                    CPUScore += 1
        scores = [p1Score, p2Score, CPUScore]
        return scores
    if column2:
        if differentiate == "CPU move":
            return True
        else:
            if boardType[1] == "X":
                print("Player 1 wins!")
                p1Score += 1
            else:
                print(opponent, "wins!")
                if opponent == p2Score:
                    p2Score += 1
                else:
                    CPUScore += 1
        scores = [p1Score, p2Score, CPUScore]
        return scores
    if column3:
        if differentiate == "CPU move":
            return True
        else:
            if boardType[2] == "X":
                print("Player 1 wins!")
                p1Score += 1
            else:
                print(opponent, "wins!")
                if opponent == p2Score:
                    p2Score += 1
                else:
                    CPUScore += 1
        scores = [p1Score, p2Score, CPUScore]
        return scores

    diagonal1 = boardType[0] == boardType[4] == boardType[8]
    diagonal2 = boardType[2] == boardType[4] == boardType[6]
    if diagonal1:
        if differentiate == "CPU move":
            return True
        else:
            if boardType[0] == "X":
                print("Player 1 wins!")
                p1Score += 1
            else:
                print(opponent, "wins!")
                if opponent == p2Score:
                    p2Score += 1
                else:
                    CPUScore += 1
        scores = [p1Score, p2Score, CPUScore]
        return scores
    if diagonal2:
        if differentiate == "CPU move":
            return True
        else:
            if boardType[2] == "X":
                print("Player 1 wins!")
                p1Score += 1
            else:
                print(opponent, "wins!")
                if opponent == p2Score:
                    p2Score += 1
                else:
                    CPUScore += 1
    if differentiate == "CPU move":
        return False
    else:
        scores = [p1Score, p2Score, CPUScore]
        return scores


def checkIfTie(board):
    turnsPlayed = 0
    for i in board:
        if i.isdigit():
            pass
        else:
            turnsPlayed += 1
    return turnsPlayed


def multiplayer(scoreTo):
    opponent = "Player 2"
    playerNum = 1
    playerSymbol = "X"
    p1Score = 0
    p2Score = 0
    roundsPlayed = 0

    while p1Score < scoreTo and p2Score < scoreTo:
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        turnsPlayed = 0

        while turnsPlayed < 9:
            displayBoard(board)
            while turnsPlayed < 9:
                playerMove = int(input("Player " + str(playerNum) + " where would you like to play? "))
                if board[playerMove - 1].isdigit():
                    board[playerMove - 1] = playerSymbol
                    scores = checkIfWinner(board, opponent, "player Move", p1Score, p2Score, 0)
                    p1Score = scores[0]
                    p2Score = scores[1]
                    turnsPlayed = checkIfTie(board)
                    break
                else:
                    print("That slot is already filled. Please choose somewhere else. ")
                    continue

            if roundsPlayed < p1Score + p2Score:
                if p1Score == scoreTo or p2Score == scoreTo:
                    break
                else:
                    print("SCORE = PLAYER 1:", p1Score, " PLAYER 2:", p2Score)
                    roundsPlayed += 1
                    break

            if turnsPlayed == 9 and roundsPlayed == p1Score + p2Score:
                print("It's a Draw! Time to restart.")
                print("SCORE = PLAYER 1:", p1Score, " PLAYER 2:", p2Score)
                break

            if playerSymbol == 'X' and playerNum == 1:
                playerSymbol = 'O'
                playerNum = 2
            else:
                playerSymbol = 'X'
                playerNum = 1

    print("GAME OVER")
    print("Player 1 won the series!") if p1Score == scoreTo else print("Player 2 won the series!")
    print("FINAL SCORE = PLAYER 1:", p1Score, " PLAYER 2:", p2Score)


def singlePlayer(scoreTo):
    opponent = "CPU"
    p1Score = 0
    CPUScore = 0
    roundsPlayed = 0

    while p1Score < scoreTo and CPUScore < scoreTo:
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        turnsPlayed = 0

        while turnsPlayed < 9:
            scores = checkIfWinner(board, opponent, "player Move", p1Score, 0, CPUScore)
            p1Score = scores[0]
            CPUScore = scores[2]
            turnsPlayed = checkIfTie(board)
            if roundsPlayed < CPUScore + p1Score:
                break

            displayBoard(board)

            # Player's move
            playerMove = int(input("Where would you like to play? "))
            if board[playerMove - 1].isdigit():
                board[playerMove - 1] = "X"
                scores = checkIfWinner(board, opponent, "player Move", p1Score, 0, CPUScore)
                p1Score = scores[0]
                CPUScore = scores[2]
                turnsPlayed = checkIfTie(board)
                if roundsPlayed < CPUScore + p1Score:
                    break
            else:
                print("That slot is already filled. Please choose somewhere else. ")
                continue

            # CPU MOVE
            import random
            possibleMoves = [x for x, position in enumerate(board) if position.isdigit()]
            movePlaced = 0

            # Try to place or prevent winning move
            for letter in ["O", "X"]:
                if movePlaced == 1:
                    continue
                for i in possibleMoves:
                    boardCopy = board.copy()
                    boardCopy[i] = letter
                    if checkIfWinner(boardCopy, opponent, "CPU move", p1Score, 0, CPUScore):
                        board[i] = "O"
                        movePlaced = 1
                        break
            if movePlaced == 1:
                continue

            # Try to take a corner
            cornerOptions = []
            for i in possibleMoves:
                if i in [0, 2, 6, 8]:
                    cornerOptions.append(i)
            if len(cornerOptions) > 0:
                CPUCorner = random.choice(cornerOptions)
                board[CPUCorner] = "O"
                continue

            # Try to take center
            if 4 in possibleMoves:
                board[4] = "O"
                continue

            # Try to take one of the edges
            edgeOptions = []
            for i in possibleMoves:
                if i in [1, 3, 5, 7]:
                    edgeOptions.append(i)
            if len(edgeOptions) > 0:
                CPUEdge = random.choice(edgeOptions)
                board[CPUEdge] = "O"
                continue

        if roundsPlayed < CPUScore + p1Score:
            if p1Score == scoreTo or CPUScore == scoreTo:
                break
            else:
                print("SCORE = CPU:", CPUScore, " YOU:", p1Score)
                roundsPlayed += 1
                continue

        if turnsPlayed == 9 and roundsPlayed == p1Score + CPUScore:
            print("It's a Draw! Time to restart.")
            print("SCORE = CPU:", CPUScore, " YOU:", p1Score)
            continue

    print("GAME OVER")
    print("The CPU won the series!") if CPUScore == scoreTo else print("You won the series!")
    print("FINAL SCORE = CPU:", CPUScore, " YOU ", p1Score)


while True:
    gameModeSelect = input("Would you like to play multiplayer or single player? (M/S) ").upper()
    score = int(input("What score would you like to play up to? "))

    if gameModeSelect == "M":
        multiplayer(score)
    elif gameModeSelect == "S":
        singlePlayer(score)

    playAgain = input("Would you like to play again? ").lower()
    if playAgain != "yes" and playAgain != "y":
        quit()
