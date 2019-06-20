#Bryan Perez
#email: perezjbryan@gmail.com
# This file contains Mancala Board and functions for using it
import array
import time
class MancalaBoardModel:
    
    # constructor:
    # initializes board
    #
    #
    #                        player1                    player2
    def __init__(self, boardsize = 14): #[ 0, 1, 2, 3, 4, 5 ,6    7, 8, 9, 10, 11, 12, 13]
#        self.boardgame = [ 4, 4, 4, 4, 4, 4, 4,      4, 4, 4, 4,  4,  4, 4]
        self.boardgame =array.array('i', (4 for i in range(boardsize)))
        self.tempboardgame = [ 4, 4, 4, 4, 4, 4, 4 ,      4, 4, 4,  4,  4,  4, 4]
    
    #Function Boardgame(self)
    #Returns the board game array
    def Boardgame(self):
        return self.boardgame
        
    #Function ReturnHoleValue(self, hole)
    #returns value of specific hole
    def ReturnHoleValue(self, hole):
        if hole < 7:
            return self.boardgame[hole-1]
        if hole >6:
            return self.boardgame[hole-1]
        
    
    #Function Last_stone_position(self)
    # return the last stone position
    def Last_stone_position(self):
        
        return self.Last_stone_position
              
##
    def MoveSelected(self, HoleNumber, playerName, continueMove = False):
      
        
        currentHole = self.PreviousPit(HoleNumber - 1 )
#        On the first move, if the hole is empty, return 0
        if self.boardgame[self.NextPit(currentHole)] == 0:
            return 0
        
#        Loop using number of stone in hand
        while True:
            if self.boardgame[self.NextPit(currentHole)] == 0:
                score =  self.boardgame[self.NextPit(self.NextPit(currentHole))]
                self.boardgame[self.NextPit(self.NextPit(currentHole))] = 0
                return score
            currentHole = self.NextPit(currentHole)
            stones = self.boardgame[currentHole]
            self.boardgame[currentHole] = 0

            while stones != 0:
    #            Go to next hole
                currentHole = self.NextPit(currentHole);
    #            Add to to current(previously next) hole
                self.boardgame[currentHole] += 1
                stones -= 1 
                
    #            Check if next hole is empty

            
                    
    

    def NextPit(self, hole):
        if hole == (len(self.boardgame)- 1):
            return 0
        
        return (hole + 1) 
      
    def PreviousPit(self, hole):
        if hole == 0:
            return (len(self.boardgame)- 1)
        
        return (hole-1)
        
    
    def moveCheck(self, Player, HoleNumber):
        if Player == "Player 1" and HoleNumber in range (1,7) and self.boardgame[HoleNumber] != 0:
            return True
        elif Player == "Player 2" and HoleNumber in range (1,7) and self.boardgame[HoleNumber] != 0:
            return True
        else:
            return False
    
    
    # Function HasStonesLeft(self, Player)
    # Takes in players name checks to see if player has any stones left in his row            
    def HasStonesLeft(self, Player):
        StonesLeft = False;
        total = 0
        
        if Player == "Player 1":
            x=0 
            while x < 7:
                total = total + self.boardgame[x]
                x=x+1
                
            if total > 0:
                StonesLeft = True
        
        if Player == "Player 2":
            x=7 
            while x < 14:
                total = total + self.boardgame[x]
                x=x+1
                
            if total > 0:
                StonesLeft = True
                
        return StonesLeft
    
   

   
    ###################################################################################################################
    #debug functions
    def printb(self):    
        print ("[14][13][12][11][10][9][8]")
        print (self.boardgame[13],self.boardgame[12], self.boardgame[11], self.boardgame[10], self.boardgame[9], self.boardgame[8], self.boardgame[7])
        print (self.boardgame[0], self.boardgame[1], self.boardgame[2], self.boardgame[3], self.boardgame[4], self.boardgame[5],self.boardgame[6])
        print ("[1][2][3][4][5][6][7]")
        print ("player 1 store: ", self.boardgame[0])
        print ("player 2 store: ", self.boardgame[1])
        print (" ")
        
#    def printt(self):
#        print (" PREVIOUS BOARD#################################")
#        print (self.tempboardgame[13],self.tempboardgame[12], self.tempboardgame[11], self.tempboardgame[10], self.tempboardgame[9], self.tempboardgame[8], self.tempboardgame[7])
#        print (self.tempboardgame[0], self.tempboardgame[1], self.tempboardgame[2], self.tempboardgame[3], self.tempboardgame[4], self.tempboardgame[5],self.boardgame[6])
#        print ("player 1 store: ", self.tempboardgame[0])
#        print ("player 2 store: ", self.tempboardgame[1])
#        print (" PREVIOUS BOARD#################################")