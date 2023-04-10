import copy
import numpy as np
def __deepcopy__(board):
    newBoard = [row[:] for row in board]
    return newBoard

class State:
    def __init__(self,coin,board,captures,parent,isTerminal):
        self.coin = coin
        self.board = board
        self.captures = captures
        self.parent = parent
        self.isTerminal = isTerminal
        self.selfPosition = ()
        self.childPosition = ()

    def Captures(self,board,parent_captures,current_coin,coin_row,coin_col):
        newCaptures = [parent_captures[0],parent_captures[1]]
        if current_coin == 'w':
            opponent_coin = 'b'
            #Checking right side of the coin
            if coin_col+3 < 19:
                if(board[coin_row][coin_col+3] == current_coin and board[coin_row][coin_col+1] == opponent_coin and board[coin_row][coin_col+2] == opponent_coin):
                    board[coin_row][coin_col+1],board[coin_row][coin_col+2] = '.','.'
                    newCaptures = [newCaptures[0]+2,newCaptures[1]]
            #Checking left side of the coin
            if coin_col-3 >= 0:
                if(board[coin_row][coin_col-3] == current_coin and board[coin_row][coin_col-1] == opponent_coin and board[coin_row][coin_col-2] == opponent_coin):
                    board[coin_row][coin_col-1],board[coin_row][coin_col-2] = '.','.'
                    newCaptures = [newCaptures[0]+2,newCaptures[1]]
            #Checking top of the coin
            if coin_row-3 >= 0:
                if(board[coin_row-3][coin_col] == current_coin and board[coin_row-1][coin_col] == opponent_coin and board[coin_row-2][coin_col] == opponent_coin):
                    board[coin_row-1][coin_col],board[coin_row-2][coin_col] = '.','.'
                    newCaptures = [newCaptures[0]+2,newCaptures[1]]
            #Checking down of the coin
            if coin_row+3 < 19:
                if(board[coin_row+3][coin_col] == current_coin and board[coin_row+1][coin_col] == opponent_coin and board[coin_row+2][coin_col] == opponent_coin):
                    board[coin_row+1][coin_col],board[coin_row+2][coin_col] = '.','.'
                    newCaptures = [newCaptures[0]+2,newCaptures[1]]
            #Checking Top-left diagonal of the coin
            if coin_row-3>=0 and coin_col-3>=0:
                if(board[coin_row-3][coin_col-3] == current_coin and board[coin_row-1][coin_col-1] == opponent_coin and board[coin_row-2][coin_col-2] == opponent_coin):
                    board[coin_row-1][coin_col-1],board[coin_row-2][coin_col-2] = '.','.'
                    newCaptures = [newCaptures[0]+2,newCaptures[1]]
            #Checking Top-right diagonal of the coin
            if coin_row-3>=0 and coin_col+3 < 19:
                if(board[coin_row-3][coin_col+3] == current_coin and board[coin_row-1][coin_col+1] == opponent_coin and board[coin_row-2][coin_col+2] == opponent_coin):
                    board[coin_row-1][coin_col+1],board[coin_row-2][coin_col+2] = '.','.'
                    newCaptures = [newCaptures[0]+2,newCaptures[1]]
            #Checking Down-left diagonal of the coin
            if coin_row+3 < 19 and coin_col-3 >= 0:
                if(board[coin_row+3][coin_col-3] == current_coin and board[coin_row+1][coin_col-1] == opponent_coin and board[coin_row+2][coin_col-2] == opponent_coin):
                    board[coin_row+1][coin_col-1],board[coin_row+2][coin_col-2] = '.','.'
                    newCaptures = [newCaptures[0]+2,newCaptures[1]]
            #Checking Down-right diagonal of the coin
            if coin_row+3 < 19 and coin_col+3 < 19:
                if(board[coin_row+3][coin_col+3] == current_coin and board[coin_row+1][coin_col+1] == opponent_coin and board[coin_row+2][coin_col+2] == opponent_coin):
                    board[coin_row+1][coin_col+1],board[coin_row+2][coin_col+2] = '.','.'
                    newCaptures = [newCaptures[0]+2,newCaptures[1]]
        else:
            opponent_coin = 'w'
            #Checking right side of the coin
            if coin_col+3 < 19:
                if(board[coin_row][coin_col+3] == current_coin and board[coin_row][coin_col+1] == opponent_coin and board[coin_row][coin_col+2] == opponent_coin):
                    board[coin_row][coin_col+1],board[coin_row][coin_col+2] = '.','.'
                    newCaptures = [newCaptures[0],newCaptures[1]+2]
            #Checking left side of the coin
            if coin_col-3 >= 0:
                if(board[coin_row][coin_col-3] == current_coin and board[coin_row][coin_col-1] == opponent_coin and board[coin_row][coin_col-2] == opponent_coin):
                    board[coin_row][coin_col-1],board[coin_row][coin_col-2] = '.','.'
                    newCaptures = [newCaptures[0],newCaptures[1]+2]
            #Checking top of the coin
            if coin_row-3 >= 0:
                if(board[coin_row-3][coin_col] == current_coin and board[coin_row-1][coin_col] == opponent_coin and board[coin_row-2][coin_col] == opponent_coin):
                    board[coin_row-1][coin_col],board[coin_row-2][coin_col] = '.','.'
                    newCaptures = [newCaptures[0],newCaptures[1]+2]
            #Checking down of the coin
            if coin_row+3 < 19:
                if(board[coin_row+3][coin_col] == current_coin and board[coin_row+1][coin_col] == opponent_coin and board[coin_row+2][coin_col] == opponent_coin):
                    board[coin_row+1][coin_col],board[coin_row+2][coin_col] = '.','.'
                    newCaptures = [newCaptures[0],newCaptures[1]+2]
            #Checking Top-left diagonal of the coin
            if coin_row-3>=0 and coin_col-3>=0:
                if(board[coin_row-3][coin_col-3] == current_coin and board[coin_row-1][coin_col-1] == opponent_coin and board[coin_row-2][coin_col-2] == opponent_coin):
                    board[coin_row-1][coin_col-1],board[coin_row-2][coin_col-2] = '.','.'
                    newCaptures = [newCaptures[0],newCaptures[1]+2]
            #Checking Top-right diagonal of the coin
            if coin_row-3>=0 and coin_col+3 < 19:
                if(board[coin_row-3][coin_col+3] == current_coin and board[coin_row-1][coin_col+1] == opponent_coin and board[coin_row-2][coin_col+2] == opponent_coin):
                    board[coin_row-1][coin_col+1],board[coin_row-2][coin_col+2] = '.','.'
                    newCaptures = [newCaptures[0],newCaptures[1]+2]
            #Checking Down-left diagonal of the coin
            if coin_row+3 < 19 and coin_col-3 >= 0:
                if(board[coin_row+3][coin_col-3] == current_coin and board[coin_row+1][coin_col-1] == opponent_coin and board[coin_row+2][coin_col-2] == opponent_coin):
                    board[coin_row+1][coin_col-1],board[coin_row+2][coin_col-2] = '.','.'
                    newCaptures = [newCaptures[0],newCaptures[1]+2]
            #Checking Down-right diagonal of the coin
            if coin_row+3 < 19 and coin_col+3 < 19:
                if(board[coin_row+3][coin_col+3] == current_coin and board[coin_row+1][coin_col+1] == opponent_coin and board[coin_row+2][coin_col+2] == opponent_coin):
                    board[coin_row+1][coin_col+1],board[coin_row+2][coin_col+2] = '.','.'
                    newCaptures = [newCaptures[0],newCaptures[1]+2]
                
        return newCaptures

    #Check if game is over
    def gameOver(self,newBoard,row,col,coin):

        #If Coin is WHITE
        if(coin == 'w'):
            # Check if 5 consecutive w's in a row
            for k in range(max(0, col - 4), min(col + 1, 15)):
                if all(newBoard[row][k + l] == 'w' for l in range(5)):
                    return True
            # Check if 5 consecutive w's in a column
            for k in range(max(0,row-4),min(row+1,15)):
                if all(newBoard[k+l][col] =='w' for l in range(5)):
                    return True
            
            # Check diagonal going upwards on right and downwards on left
            count = 1  # Initialize count to 1 for the new 'w' placed at (row, col)
            r, c = row - 1, col + 1
            while r >= 0 and c < 19 and newBoard[r][c] == 'w':
                count += 1
                r -= 1
                c += 1
            r, c = row + 1, col - 1
            while r < 19 and c >= 0 and newBoard[r][c] == 'w':
                count += 1
                r += 1
                c -= 1
            if count == 5:
                return True
            # Check diagonal going upwards on left and downwards on right
            count = 1
            r, c = row - 1, col - 1
            while r >= 0 and c >= 0 and newBoard[r][c] == 'w':
                count += 1
                r -= 1
                c -= 1
            r, c = row + 1, col + 1
            while r < 19 and c < 19 and newBoard[r][c] == 'w':
                count += 1
                r += 1
                c += 1
            if count == 5:
                    return True
            return False

        #If coin is BLACK
        else:
            # Check if 5 consecutive b's in a row
            for k in range(max(0, col - 4), min(col + 1, 15)):
                if all(newBoard[row][k + l] == 'b' for l in range(5)):
                    return True
            # Check if 5 consecutive b's in a column
            for k in range(max(0,row-4),min(row+1,15)):
                if all(newBoard[k+l][col] =='b' for l in range(5)):
                    return True

            # Check diagonal going upwards on right and downwards on left
            count = 1  # Initialize count to 1 for the new 'b' placed at (row, col)
            r, c = row - 1, col + 1
            while r >= 0 and c < 19 and newBoard[r][c] == 'b':
                count += 1
                r -= 1
                c += 1
            r, c = row + 1, col - 1
            while r < 19 and c >= 0 and newBoard[r][c] == 'b':
                count += 1
                r += 1
                c -= 1
            if count == 5:
                return True

            # Check diagonal going upwards on left and downwards on right
            count = 1
            r, c = row - 1, col - 1
            while r >= 0 and c >= 0 and newBoard[r][c] == 'b':
                count += 1
                r -= 1
                c -= 1
            r, c = row + 1, col + 1
            while r < 19 and c < 19 and newBoard[r][c] == 'b':
                count += 1
                r += 1
                c += 1
            if count == 5:
                return True
            return False
        #iterate over rows
        # for row in range(len(self.board)):
        #     count_b =0
        #     count_w = 0
        #     for col in range(len(self.board)):
        #         if self.board[row][col] == 'b':
        #             count_b+=1
        #             count_w = 0
        #             if count_b == 5:
        #                 return 'b'
        #         elif self.board[row][col] == 'w':
        #             count_w+=1
        #             count_b=0
        #             if count_w == 5:
        #                 return 'w'
        #         else:
        #             count_b=0
        #             count_w=0


        # iterate over columns
        # for col in range(len(self.board)):
        #     count_b = 0
        #     count_w = 0
        #     for row in range(len(self.board)):
        #         if self.board[row][col] == 'b':
        #             count_b += 1
        #             count_w = 0
        #             if count_b == 5:
        #                 return 'b'
        #         elif self.board[row][col] == 'w':
        #             count_w += 1
        #             count_b = 0
        #             if count_w == 5:
        #                 return 'w'
        #         else:
        #             count_b = 0
        #             count_w = 0
        
        # iterate over diagonals from top left to bottom right
        # for row in range(len(self.board)-4):
        #     for col in range(len(self.board)-4):
        #         color = self.board[row][col]
        #         if color == '.':
        #             continue
        #         if self.board[row+1][col+1] == color and self.board[row+2][col+2] == color and self.board[row+3][col+3] == color and self.board[row+4][col+4] == color:
        #             return color
        # no winner found
                    
        # iterate over diagonals from top right to bottom left
        # for row in range(4,len(self.board)):
        #     for col in range(len(self.board)-4):
        #         color = self.board[row][col]
        #         if color == '.':
        #             continue
        #         if self.board[row-1][col+1] == color and self.board[row-2][col+2] == color and self.board[row-3][col+3] == color and self.board[row-4][col+4] == color:
        #             return color
        # # no winner found
        # return None

    #Evaluation Function
    def evaluation(self,toWin):
        current_board = self.board
        if toWin == 'w':
            toLose = 'b'
            toWin_capture,toLose_capture = self.captures[0],self.captures[1]
        else:
            toLose = 'w'
            toWin_capture,toLose_capture = self.captures[1],self.captures[0]
        
        toWin_4,toLose_4 = 0,0
        toWin_3,toLose_3 = 0,0
        toWin_2,toLose_2 = 0,0
        

        for i in range (19):
            for j in range (19):
                #If the current coin is the to be winner coin
                if(current_board[i][j] == toWin):

                    #Top-Left to Bottom Right diagonal check 
                    if(i-1>=0 and j-1>=0 and current_board[i-1][j-1] == toWin):
                        if(i+1<19 and j+1<19 and current_board[i+1][j+1] != toWin):
                            count = 1
                            x,y=i-1,j-1
                            while(x>=0 and y>=0 and current_board[x][y]==toWin):
                                count+=1
                                x-=1
                                y-=1
                            if count == 4:
                                toWin_4 += 1
                            elif count == 3:
                                toWin_3 +=1
                            else:
                                toWin_2 +=1
                    
                    #Top-Right to Bottom Left diagonal check 
                    if(i-1>=0 and j+1<19 and current_board[i-1][j+1] == toWin):
                        if(i+1<19 and j-1>=0 and current_board[i+1][j-1] != toWin):
                            count = 1
                            x,y=i-1,j+1
                            while(x>=0 and y<19 and current_board[x][y]==toWin):
                                count+=1
                                x-=1
                                y-=1
                            if count == 4:
                                toWin_4 += 1
                            elif count == 3:
                                toWin_3 +=1
                            else:
                                toWin_2 +=1
                    
                    #Top to Bottom column
                    if(i-1>=0 and current_board[i-1][j] == toWin):
                        if(i+1 < 19 and current_board[i+1][j] != toWin):
                            count = 1
                            x,y = i-1,j
                            while(x>=0 and current_board[x][y] == toWin):
                                count+=1
                                x-=1
                            if count == 4:
                                toWin_4 += 1
                            elif count == 3:
                                toWin_3 += 1
                            else:
                                toWin_2 +=1
                    
                    #Left to Right Row
                    if(j-1>=0 and current_board[i][j-1] == toWin):
                        if(j+1 < 19 and current_board[i][j+1] != toWin):
                            count = 1
                            x,y = i,j-1
                            while(y>=0 and current_board[x][y] == toWin):
                                count+=1
                                y-=1
                            if count == 4:
                                toWin_4 += 1
                            elif count == 3:
                                toWin_3 += 1
                            else:
                                toWin_2 +=1
                
                #If the current coin is the to be Loser coin
                elif current_board[i][j] == toLose:
                    
                    #Top-Left to Bottom Right diagonal check 
                    if(i-1>=0 and j-1>=0 and current_board[i-1][j-1] == toLose):
                        if(i+1<19 and j+1<19 and current_board[i+1][j+1] != toLose):
                            count = 1
                            x,y=i-1,j-1
                            while(x>=0 and y>=0 and current_board[x][y]==toLose):
                                count+=1
                                x-=1
                                y-=1
                            if count == 4:
                                toLose_4 += 1
                            elif count == 3:
                                toLose_3 +=1
                            else:
                                toLose_2 +=1
                    
                    #Top-Right to Bottom Left diagonal check 
                    if(i-1>=0 and j+1<19 and current_board[i-1][j+1] == toLose):
                        if(i+1<19 and j-1>=0 and current_board[i+1][j-1] != toLose):
                            count = 1
                            x,y=i-1,j+1
                            while(x>=0 and y<19 and current_board[x][y]==toLose):
                                count+=1
                                x-=1
                                y-=1
                            if count == 4:
                                toLose_4 += 1
                            elif count == 3:
                                toLose_3 +=1
                            else:
                                toLose_2 +=1
                    
                    #Top to Bottom column
                    if(i-1>=0 and current_board[i-1][j] == toLose):
                        if(i+1 < 19 and current_board[i+1][j] != toLose):
                            count = 1
                            x,y = i-1,j
                            while(x>=0 and current_board[x][y] == toLose):
                                count+=1
                                x-=1
                            if count == 4:
                                toLose_4 += 1
                            elif count == 3:
                                toLose_3 +=1
                            else:
                                toLose_2 +=1
                    
                    #Left to Right Row
                    if(j-1>=0 and current_board[i][j-1] == toLose):
                        if(j+1 < 19 and current_board[i][j+1] != toLose):
                            count = 1
                            x,y = i,j-1
                            while(y>=0 and current_board[x][y] == toLose):
                                count+=1
                                y-=1
                            if count == 4:
                                toLose_4 += 1
                            elif count == 3:
                                toLose_3 +=1
                            else:
                                toLose_2 +=1
                else:
                    continue
        
        val = 100.0*(toWin_capture) + 10.0*(toWin_2) - 80.0*(toLose_capture) + 50.0*(toWin_3) - 20.0*(toLose_2) + 100.0*(toWin_4) - 75.0*(toLose_3) - 500.0*(toLose_4) 
        return val

    #Minimax function
    def minimax(self, depth, alpha, beta,maximizingPlayer,toWin):
        if(depth == 0 or self.isTerminal):
            if(self.isTerminal == True and self.coin != toWin):
                return 10000 
            elif(self.isTerminal == True and self.coin == toWin):
                return -10000
            return self.evaluation(toWin)

        if(maximizingPlayer):
            maxEval = -9999999999999999999
            children = self.generateChildren1()
            for child in children:
                eval= child.minimax(depth-1,alpha,beta,False,toWin)
                if eval > maxEval:
                    maxEval = eval
                    self.childPosition = child.selfPosition
                alpha = max(alpha,eval)
                if beta <= alpha:
                    break
            return maxEval
        else:
            minEval = 9999999999999999999
            children = self.generateChildren1()
            for child in children:
                eval = child.minimax(depth-1,alpha,beta,True,toWin)
                if eval < minEval:
                    minEval = eval
                    self.childPosition = child.selfPosition
                beta = min(beta,eval)
                if beta <= alpha:
                    break
            return minEval

    #New Generate Kids
    def generateChildren1(self):
        #List of Children
        children = []

        #Number of [white,black] coins
        numOfCoins = count_coins(self.board)

        #Check if the count is [1,1] and capture is [0,0]
        if(numOfCoins == (1,1) and self.captures == [0,0]):
            #make a copy of the parent board
            newBoard = copy.deepcopy(self.board)
            #Place the coin in all the empty positions which are more that 3 distance away from the center
            for i in range(6,13):
                for j in range(6,13):
                    #Check condition for being at 3 distance away from the center
                    if((i>=7 and i<=11) and (j>=7 and j<=11)):
                        continue
                    #If the cell is not empty skip that cell
                    if(newBoard[i][j] != '.'):
                        continue
                    #else place the coin in that cell
                    newBoard[i][j] = self.coin
                    #Check Game conditions
                    isOver = False
                    #No new captures are done in the second move
                    newCaptures = copy.deepcopy(self.captures)
                    #if the coin placed is WHITE then the next coin to be placed will be BLACK
                    if self.coin == 'w':
                        newCoin = 'b'
                        #Make a state and save it in the list of children
                        child = State(newCoin, copy.deepcopy(newBoard), newCaptures, self,isOver)
                        child.selfPosition = (i,j)
                        children.append(child)
                    #if the coin placed is BLACK then the next coin to be placed will be WHITE
                    else:
                        newCoin = 'w'
                        #Make a state and save it in the list of children
                        child = State(newCoin, copy.deepcopy(newBoard), newCaptures, self,isOver)
                        child.selfPosition = (i,j)
                        children.append(child)
                    #Undo changes for further iterations
                    newBoard[i][j] = '.'
            #return the list of children
            return children
            #If it's not the second move then generate children 
        else:
            #set of positions of exisiting coins
            exisitingCoinsPos = existingCoins(self.board)

            #set of positions of newly placed coins
            placed = set()

            # Make a copy of exisiting board
            newBoard = copy.deepcopy(self.board)

            #Check all the 8 directions of the exisiting coin and if any cell is empty then place the coin there, make it a child and undo the placing.
            for pos in exisitingCoinsPos:
                r,c = pos[0],pos[1]

                #Check Down
                if(r+1 <19 and ((r+1,c) not in placed) and ((r+1,c) not in exisitingCoinsPos)):
                    #Place the coin on the board
                    newBoard[r+1][c] = self.coin
                    placed.add((r+1,c))
                    #Check if the game is over
                    isOver = self.gameOver(newBoard,r+1,c,self.coin)
                    #if the Game is over then there is no new captures so set it same as parents capture
                    if(isOver):
                        newCaptures = copy.deepcopy(self.captures)
                    #else check for new Captures
                    else:
                        newCaptures = self.Captures(newBoard,copy.deepcopy(self.captures),self.coin,r+1,c)
                        if(newCaptures[0] >= 10 or newCaptures[1]>=10):
                            isOver = True
                    
                    #If the placed coin is WHITE then new coin will be BLACK
                    if self.coin == 'w':
                        newCoin = 'b'
                        child = State(newCoin, copy.deepcopy(newBoard), newCaptures, self,isOver)
                        child.selfPosition = (r+1,c)
                        children.append(child)
                    #Else if the placed coin is BLACK then the new coin will be WHITE
                    else:
                        newCoin = 'w'
                        child = State(newCoin, copy.deepcopy(newBoard), newCaptures, self,isOver)
                        child.selfPosition = (r+1,c)
                        children.append(child)
                    #Undo the changes
                    newBoard[r+1][c] = '.'

                #Check Up
                if(r-1 >=0 and ((r-1,c) not in placed) and ((r-1,c) not in exisitingCoinsPos)):
                    #Place the coin on the board
                    newBoard[r-1][c] = self.coin
                    placed.add((r-1,c))
                    #Check if the game is over
                    isOver = self.gameOver(newBoard,r-1,c,self.coin)
                    #if the Game is over then there is no new captures so set it same as parents capture
                    if(isOver):
                        newCaptures = copy.deepcopy(self.captures)
                    #else check for new Captures
                    else:
                        newCaptures = self.Captures(newBoard,copy.deepcopy(self.captures),self.coin,r-1,c)
                        if(newCaptures[0] >= 10 or newCaptures[1]>=10):
                            isOver = True
                    
                    #If the placed coin is WHITE then new coin will be BLACK
                    if self.coin == 'w':
                        newCoin = 'b'
                        child = State(newCoin, copy.deepcopy(newBoard), newCaptures, self,isOver)
                        child.selfPosition = (r-1,c)
                        children.append(child)
                    #Else if the placed coin is BLACK then the new coin will be WHITE
                    else:
                        newCoin = 'w'
                        child = State(newCoin, copy.deepcopy(newBoard), newCaptures, self,isOver)
                        child.selfPosition = (r-1,c)
                        children.append(child)
                    #Undo the changes
                    newBoard[r-1][c] = '.'

                #Check left
                if((c-1 >=0) and ((r,c-1) not in placed) and ((r,c-1) not in exisitingCoinsPos)):
                    #Place the coin on the board
                    newBoard[r][c-1] = self.coin
                    placed.add((r,c-1))
                    #Check if the game is over
                    isOver = self.gameOver(newBoard,r,c-1,self.coin)
                    #if the Game is over then there is no new captures so set it same as parents capture
                    if(isOver):
                        newCaptures = copy.deepcopy(self.captures)
                    #else check for new Captures
                    else:
                        newCaptures = self.Captures(newBoard,copy.deepcopy(self.captures),self.coin,r,c-1)
                        if(newCaptures[0] >= 10 or newCaptures[1]>=10):
                            isOver = True
                    
                    #If the placed coin is WHITE then new coin will be BLACK
                    if self.coin == 'w':
                        newCoin = 'b'
                        child = State(newCoin, copy.deepcopy(newBoard), newCaptures, self,isOver)
                        child.selfPosition = (r,c-1)
                        children.append(child)
                    #Else if the placed coin is BLACK then the new coin will be WHITE
                    else:
                        newCoin = 'w'
                        child = State(newCoin, copy.deepcopy(newBoard), newCaptures, self,isOver)
                        child.selfPosition = (r,c-1)
                        children.append(child)
                    #Undo the changes
                    newBoard[r][c-1] = '.'

                #Check Right
                if((c+1<19) and ((r,c+1) not in placed) and ((r,c+1) not in exisitingCoinsPos)):
                    #Place the coin on the board
                    newBoard[r][c+1] = self.coin
                    placed.add((r,c+1))
                    #Check if the game is over
                    isOver = self.gameOver(newBoard,r,c+1,self.coin)
                    #if the Game is over then there is no new captures so set it same as parents capture
                    if(isOver):
                        newCaptures = copy.deepcopy(self.captures)
                    #else check for new Captures
                    else:
                        newCaptures = self.Captures(newBoard,copy.deepcopy(self.captures),self.coin,r,c+1)
                        if(newCaptures[0] >= 10 or newCaptures[1]>=10):
                            isOver = True
                    
                    #If the placed coin is WHITE then new coin will be BLACK
                    if self.coin == 'w':
                        newCoin = 'b'
                        child = State(newCoin, copy.deepcopy(newBoard), newCaptures, self,isOver)
                        child.selfPosition = (r,c+1)
                        children.append(child)
                    #Else if the placed coin is BLACK then the new coin will be WHITE
                    else:
                        newCoin = 'w'
                        child = State(newCoin, copy.deepcopy(newBoard), newCaptures, self,isOver)
                        child.selfPosition = (r,c+1)
                        children.append(child)
                    #Undo the changes
                    newBoard[r][c+1] = '.'
                
                #Check Down Left
                if((r+1<19 and c-1 >= 0) and ((r+1,c-1) not in placed) and ((r+1,c-1) not in exisitingCoinsPos)):
                    #Place the coin on the board
                    newBoard[r+1][c-1] = self.coin
                    placed.add((r+1,c-1))
                    #Check if the game is over
                    isOver = self.gameOver(newBoard,r+1,c-1,self.coin)
                    #if the Game is over then there is no new captures so set it same as parents capture
                    if(isOver):
                        newCaptures = copy.deepcopy(self.captures)
                    #else check for new Captures
                    else:
                        newCaptures = self.Captures(newBoard,copy.deepcopy(self.captures),self.coin,r+1,c-1)
                        if(newCaptures[0] >= 10 or newCaptures[1]>=10):
                            isOver = True
                    
                    #If the placed coin is WHITE then new coin will be BLACK
                    if self.coin == 'w':
                        newCoin = 'b'
                        child = State(newCoin, copy.deepcopy(newBoard), newCaptures, self,isOver)
                        child.selfPosition = (r+1,c-1)
                        children.append(child)
                    #Else if the placed coin is BLACK then the new coin will be WHITE
                    else:
                        newCoin = 'w'
                        child = State(newCoin, copy.deepcopy(newBoard), newCaptures, self,isOver)
                        child.selfPosition = (r+1,c-1)
                        children.append(child)
                    #Undo the changes
                    newBoard[r+1][c-1] = '.'
                
                #Check Down Right
                if((r+1 <19 and c+1 < 19) and ((r+1,c+1) not in placed) and ((r+1,c+1) not in exisitingCoinsPos)):
                    #Place the coin on the board
                    newBoard[r+1][c+1] = self.coin
                    placed.add((r+1,c+1))
                    #Check if the game is over
                    isOver = self.gameOver(newBoard,r+1,c+1,self.coin)
                    #if the Game is over then there is no new captures so set it same as parents capture
                    if(isOver):
                        newCaptures = copy.deepcopy(self.captures)
                    #else check for new Captures
                    else:
                        newCaptures = self.Captures(newBoard,copy.deepcopy(self.captures),self.coin,r+1,c+1)
                        if(newCaptures[0] >= 10 or newCaptures[1]>=10):
                            isOver = True
                    
                    #If the placed coin is WHITE then new coin will be BLACK
                    if self.coin == 'w':
                        newCoin = 'b'
                        child = State(newCoin, copy.deepcopy(newBoard), newCaptures, self,isOver)
                        child.selfPosition = (r+1,c+1)
                        children.append(child)
                    #Else if the placed coin is BLACK then the new coin will be WHITE
                    else:
                        newCoin = 'w'
                        child = State(newCoin, copy.deepcopy(newBoard), newCaptures, self,isOver)
                        child.selfPosition = (r+1,c+1)
                        children.append(child)
                    #Undo the changes
                    newBoard[r+1][c+1] = '.'

                #Check Up Left
                if((r-1 >= 0 and c-1 >=0) and ((r-1,c-1) not in placed) and ((r-1,c-1) not in exisitingCoinsPos)):
                    #Place the coin on the board
                    newBoard[r-1][c-1] = self.coin
                    placed.add((r-1,c-1))
                    #Check if the game is over
                    isOver = self.gameOver(newBoard,r-1,c-1,self.coin)
                    #if the Game is over then there is no new captures so set it same as parents capture
                    if(isOver):
                        newCaptures = copy.deepcopy(self.captures)
                    #else check for new Captures
                    else:
                        newCaptures = self.Captures(newBoard,copy.deepcopy(self.captures),self.coin,r-1,c-1)
                        if(newCaptures[0] >= 10 or newCaptures[1]>=10):
                            isOver = True
                    
                    #If the placed coin is WHITE then new coin will be BLACK
                    if self.coin == 'w':
                        newCoin = 'b'
                        child = State(newCoin, copy.deepcopy(newBoard), newCaptures, self,isOver)
                        child.selfPosition = (r-1,c-1)
                        children.append(child)
                    #Else if the placed coin is BLACK then the new coin will be WHITE
                    else:
                        newCoin = 'w'
                        child = State(newCoin, copy.deepcopy(newBoard), newCaptures, self,isOver)
                        child.selfPosition = (r-1,c-1)
                        children.append(child)
                    #Undo the changes
                    newBoard[r-1][c-1] = '.'
                
                #Check Up Right
                if((r-1 >= 0 and c+1 <19) and ((r-1,c+1) not in placed) and ((r-1,c+1) not in exisitingCoinsPos)):
                    #Place the coin on the board
                    newBoard[r-1][c+1] = self.coin
                    placed.add((r-1,c+1))
                    #Check if the game is over
                    isOver = self.gameOver(newBoard,r-1,c+1,self.coin)
                    #if the Game is over then there is no new captures so set it same as parents capture
                    if(isOver):
                        newCaptures = copy.deepcopy(self.captures)
                    #else check for new Captures
                    else:
                        newCaptures = self.Captures(newBoard,copy.deepcopy(self.captures),self.coin,r-1,c+1)
                        if(newCaptures[0] >= 10 or newCaptures[1]>=10):
                            isOver = True
                    
                    #If the placed coin is WHITE then new coin will be BLACK
                    if self.coin == 'w':
                        newCoin = 'b'
                        child = State(newCoin, copy.deepcopy(newBoard), newCaptures, self,isOver)
                        child.selfPosition = (r-1,c+1)
                        children.append(child)
                    #Else if the placed coin is BLACK then the new coin will be WHITE
                    else:
                        newCoin = 'w'
                        child = State(newCoin, copy.deepcopy(newBoard), newCaptures, self,isOver)
                        child.selfPosition = (r-1,c+1)
                        children.append(child)
                    #Undo the changes
                    newBoard[r-1][c+1] = '.'
            return children
  
def count_coins(grid):
    # b_count = 0
    # w_count = 0
    # dot_count = 0

    board = np.array(grid)

    # Fill the board with values (e.g. 'b', 'w', or '.')

    b = np.sum(board == 'b')
    w = np.sum(board == 'w')
    # e = np.sum(board == '.')

    # for row in range(19):
    #     for col in range(19):
    #         char = grid[row][col]
    #         if char == 'b':
    #             b_count += 1
    #         elif char == 'w':
    #             w_count += 1
    #         elif char == '.':
    #             dot_count += 1

    # Print the counts for each character
    return (w,b)

def existingCoins(grid):
    pos = []
    for i in range (19):
        for j in range (19):
            if (grid[i][j] != '.'):
                pos.append((i,j))
    return pos

#Main Function 
def main():
    with open('input.txt','r') as fp:
        #color of your chance
        coin = fp.readline().strip()
        #time left for the game
        time_left = float(fp.readline().strip())
        #It is the list captures made by white which is index 0 and black is at index 1
        captures = list(map(int,fp.readline().strip().split(',')))
        #Character grid 
        board = []
        for line in fp:
            board.append(list(line.strip()))
        
        if(coin == 'WHITE'):
            coin = 'w'
        else:
            coin = 'b'
            
        w_count,b_count = count_coins(board)
        if(w_count == 0 and b_count == 0 and captures == [0,0]):
            #return coin is placed on 10J
            with open('output.txt', 'w') as f:
                # Write the value associated with key 2 to the file
                f.write(str(10)+'K')
            return
        
        toWin = coin #coin to win
        currentState = State(coin,board,captures,None,False) #('w' or 'b' to be placed, board, [white_captures,black_captures], parent , isTerminal=> True/False)
   
    if(time_left >= 50.0):
        depth = 3
    elif time_left<50 and time_left>=5: 
        depth = 2
    else:
        depth = 1

    currentState.minimax(depth,-9999999999999999999,9999999999999999999,True,toWin) #(depth,alpha,beta, maximizer,coin to win)
    (x,y) = currentState.childPosition
    col_axis = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'J',9:'K',10:'L',11:'M',12:'N',13:'O',14:'P',15:'Q',16:'R',17:'S',18:'T'}

    with open('output.txt', 'w') as f:
        f.write(str(19-x)+col_axis[y])
        return
if __name__ == "__main__":
    main()