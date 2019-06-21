#Bryan Perez
#email: perezjbryan@gmail.com
# This file contains the player model


class BotModel:
    
    # constructor:
    # initializes player's Name, score, last stone postions variables
    def __init__(self, playerName, diff=None):
        self.playerName = playerName
        self.boardSize = 14
        if(diff == 1):
            self.maxDepth = 7
        else:
            self.maxDepth = 3
            
    
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

        
#    Move to next Hole
    def NextPit(self, hole):
        if hole == (self.boardSize - 1):
            return 0
        
        return (hole + 1) 
      
#    Move back one hole
    def PreviousPit(self, hole):
        if hole == 0:
            return (self.boardSize - 1)
        
        return (hole-1)   
    
#    Find index for occupied hole
    def GetMaxOccupiedCells(self, board):
        list = [i for i, x in enumerate(board[7:14]) if x != 0];
        return [x + 7 for x in list]
    
    def GetMinOccupiedCells(self, board):
        return [i for i, x in enumerate(board[0:7]) if x != 0];
    
#    Get score for move selected 
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

#    Called from controller to return best move using minimax + ab pruning
    def GetMove(self, board):
        
        occupiedCells = self.GetMaxOccupiedCells(board)
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
        
        return bestMove
        
    
#    Evaluate leaf node and move
    def HeuristicFunction(self, maxPlayerScore, minPlayerScore):
        return (maxPlayerScore - minPlayerScore)
    
#    Perform minimax and ad pruning
    def iterative_minimax(self, move, maxPlayerScore, minPlayerScore, board, depth, alpha, beta, isMaximizingPlayer):
        if depth == 1:
            bestMove = -1
            
        if depth == self.maxDepth:
            return move, self.HeuristicFunction(maxPlayerScore, minPlayerScore)
        

        if isMaximizingPlayer: 
            maxEval = float('-inf');
            occupiedCells = self.GetMaxOccupiedCells(board);
            if not occupiedCells:
               return move, self.HeuristicFunction(maxPlayerScore, minPlayerScore)
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
            occupiedCells = self.GetMinOccupiedCells(board);
            if not occupiedCells:
               return move, self.HeuristicFunction(maxPlayerScore, minPlayerScore)
            for i in occupiedCells:

                newBoard, score = self.EvaluateMove(i, board)
                
                move, evalValue = self.iterative_minimax(move, maxPlayerScore, minPlayerScore + score, newBoard, depth + 1, alpha, beta, True);
                minEval = min(minEval, evalValue);
                bestMove = move if evalValue == minEval else bestMove;
                beta = min(beta, evalValue)
                if(beta <= alpha):
                    break;
            return bestMove, minEval     





            

   