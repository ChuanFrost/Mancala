#Bryan Perez
#email: perezjbryan@gmail.com
# This file contains Mancala Board and functions for using it
import array
class MancalaBoardModel:
    
    # constructor:
    # initializes board
    #
    #
    #                        player1                    player2
    def __init__(self, boardsize = 14): #[ 0, 1, 2, 3, 4, 5 ,6    7, 8, 9, 10, 11, 12, 13]
#        self.boardgame = [ 4, 4, 4, 4, 4, 4, 4,      4, 4, 4, 4,  4,  4, 4]
        self.boardgame =array.array('i', (4 for i in range(boardsize)))
        self.Last_stone_position = 0
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
        
    #Function ReturnStores(self)
    # return the 2 stores as a tuple player1's is the first the second is player2's
    def ReturnStores(self):
        storeTuple = (self.boardgame[0], self.boardgame[1])
        return storeTuple
        
#     Function MoveSelected(self, HoleNumber):
#     Moves stones according to selected hole 
#    def MoveSelected(self, HoleNumber, playerName, isPlayerMove = False):
#      
#        HoleNumber=HoleNumber-1
#        
#        self.tempboardgame = list(self.boardgame)
#        score = 0
#        next_hole = 0
#        global flag
#        stones = self.boardgame[HoleNumber]
#        self.boardgame[HoleNumber] = 0
#       
#        if playerName == "Player 1":
#            flag = True
#        elif playerName == "Player 2":
#            flag = False
#        
#        while stones != 0:
#               
#            if flag:
#                for index in range(14):
#                    if index > HoleNumber:
#                        if stones > 0:
#                            self.boardgame[index]= self.boardgame[index] + 1
#                            stones = stones - 1
#                            LastPosition = index
#                         
##            
##                for index in range(14):
##                    if stones > 0:
##                        self.boardgame[index]= self.boardgame[index] + 1
##                        stones = stones - 1
##                        LastPosition = index
#                       
#                     
#            
#            
#            else:
#                for index in range(15):
#                    if index > HoleNumber:
#                        if stones > 0:
#                            if index != 6:
#                                self.boardgame[index]= self.boardgame[index] + 1
#                                stones = stones - 1
#                                LastPosition = index
                                
            
#                for index in range(15):
#                    if stones > 0:
#                        if index != 6:
#                            self.boardgame[index]= self.boardgame[index] + 1
#                            stones = stones - 1
#                            LastPosition = index
             
                
#                 #if LastPosition < 6:
#        #    self.Last_stone_position =LastPosition+1
#            if LastPosition == 7:
#                self.Last_stone_position  = 101
#            elif LastPosition == 15:
#                self.Last_stone_position  = 102
#            else:
#                self.Last_stone_position = LastPosition   
                            
#            if self.boardgame[LastPosition+1] == 0:
#                    score_hole = LastPosition + 1
#                    score = self.boardgame[score_hole]
#            else:
#                    score = self.MoveSelected(LastPosition,True)                  
#        
#        return score
                                
                                
       
     
        
#        if self.boardgame[LastPosition+1] == 0:
#            score_hole = LastPosition + 1
#            score = self.boardgame[score_hole]
#        else:
#            score = self.MoveSelected(LastPosition,True)
#        
#        return score
        
        
##
    def MoveSelected(self, HoleNumber, playerName, continueMove = False):
      
        
        currentHole = self.PreviousPit(HoleNumber - 1 )
        self.tempboardgame = list(self.boardgame)
        
        
      
#        Loop using number of stone in hand
        while True:
            if self.boardgame[self.NextPit(currentHole)] == 0:
                score =  self.boardgame[self.NextPit(self.NextPit(currentHole))]
                self.boardgame[self.NextPit(self.NextPit(currentHole))] = 0
                print(score)
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