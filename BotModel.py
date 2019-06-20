#Bryan Perez
#email: perezjbryan@gmail.com
# This file contains the player model


class BotModel:
    
    # constructor:
    # initializes player's Name, score, last stone postions variables
    def __init__(self, playerName):
        self.playerName = playerName
        self.score = 0
        self.Last_stone_position = 0
        self.maxDepth = 1
        self.boardSize = 14
#        self.halfSize = int(self.boardSize/2)
        self.halfSize = 0
    
    #Function: playerName(self)
    #returns player name
    def PlayerName(self):
        return self.playerName
        
    #Function: score(self)
    #returns player's score
    def Score(self):
        return self.score
        
    #Function: setScore(self)
    # sets players score
    def SetScore(self, score):
        self.score = score

    def SetBoardSize(self, boardSize):
        self.boardSize = boardSize
        self.halfSize = int(boardSize/2)
        
    def NextPit(self, hole):
        if hole == (self.boardSize - 1):
            return 0
        
        return (hole + 1) 
      
    def PreviousPit(self, hole):
        if hole == 0:
            return (self.boardSize - 1)
        
        return (hole-1)   
    
#    Find index for occupied hole
    def GetOccupiedCells(self, board):
        return [i for i, x in enumerate(board[7:14]) if x != 0];
    
    def EvaluateMove(self, hole, board):
        
        currentHole = self.PreviousPit(hole)
        copyBoard = board.copy()
        if(copyBoard[self.NextPit(currentHole)] == 0):
            return copyBoard, 0


        while True:
            if copyBoard[self.NextPit(currentHole)] == 0:
                score =  copyBoard[self.NextPit(self.NextPit(currentHole))]
                copyBoard[self.NextPit(self.NextPit(currentHole))] = 0
                return copyBoard, score
            currentHole = self.NextPit(currentHole)
            stones = copyBoard[currentHole]
            copyBoard[currentHole] = 0

            while stones != 0:
                currentHole = self.NextPit(currentHole);
                copyBoard[currentHole] += 1
                stones -= 1 

    
    def GetMove(self, board):
        
        occupiedCells = self.GetOccupiedCells(board)
        if not occupiedCells:
           return 7
      
        bestMove = -1
        alpha = maxEval = float('-inf')
        beta = float('inf')
        for i in occupiedCells:
            
            newBoard, score = self.EvaluateMove(i, board)
            move, evalValue = self.iterative_minimax(i, score, 0, newBoard, 1, alpha, beta, False)
#            print(evalValue)
            maxEval = max(maxEval, evalValue)
            bestMove = move if evalValue == maxEval else bestMove;
        
        return bestMove+7
        
    
    def HeuristicFunction(self, maxPlayerScore, minPlayerScore):
        return (maxPlayerScore - minPlayerScore)
    
    def iterative_minimax(self, move, maxPlayerScore, minPlayerScore, board, depth, alpha, beta, isMaximizingPlayer):
        if depth == 1:
            bestMove = -1
            
        if depth == self.maxDepth:
            return move, self.HeuristicFunction(maxPlayerScore, minPlayerScore)
        
        occupiedCells = self.GetOccupiedCells(board);
        if not occupiedCells:
           return move, self.HeuristicFunction(maxPlayerScore, minPlayerScore)
        if isMaximizingPlayer: 
            maxEval = float('-inf');
            for i in occupiedCells:
                

                newBoard, score = self.EvaluateMove(i, board)

                move, evalValue = self.iterative_minimax(move, maxPlayerScore + score, minPlayerScore, newBoard, depth + 1, alpha, beta, False);
                maxEval = max(maxEval, evalValue);
                bestMove = move if evalValue == maxEval else bestMove;
                alpha = max(alpha, evalValue)
                if(beta <= alpha):
                    break;
            return bestMove, maxEval;
        
        else:
            minEval = float('inf')
            for i in occupiedCells:

                newBoard, score = self.EvaluateMove(i, board)
                
                move, evalValue = self.iterative_minimax(move, maxPlayerScore, minPlayerScore - score, newBoard, depth + 1, alpha, beta, True);
                minEval = min(minEval, evalValue);
                bestMove = move if evalValue == minEval else bestMove;
                beta = min(beta, evalValue)
                if(beta <= alpha):
                    break;
            return bestMove, minEval     


#board1 = [2,1,7,7,7,0,7,0,0,6,1,6,6,0]   
#board2 = [6,5,1,2,12,1,12,0,0,0,3,0,3,1]
#board3 = [0,2,1,7,7,7,0,7,0,0,6,1,6,6]  
#
#p = BotModel("dumb")
#print(p.GetMove(board3))
#print(p.EvaluateMove(6,board1))

#print(p.GetOccupiedCells(board1))
#if not p.GetOccupiedCells(board1):
#    print("yes")


            

   
