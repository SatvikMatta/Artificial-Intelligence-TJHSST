# Name: Satvik Matta
# Date: January 1st 2022

import random
import math
import copy
class RandomBot:
   def __init__(self):
      self.white = "O"
      self.black = "@"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = None
      self.y_max = None

   def best_strategy(self, board, color):
      # returns best move
      self.x_max = len(board)
      self.y_max = len(board[0])
      if color == "#000000":
         color = "@"
      else:
         color = "O"
      
      ''' Your code goes here ''' 
      moves = list(self.find_moves(board,color).keys())
      move = random.choice(moves)
      best_move = [move[0], move[1]]
      return best_move, 0

   def stones_left(self, board):
    # returns number of stones that can still be placed (empty spots)
      count = 0
      for i in len(board):
         for j in len(board[i]):
            if board[i][j] == ".":
               count+=1
      return count

   def find_moves(self, board, color):
    # finds all possible moves
    moves_found = {}
    for i in range(len(board)):
        for j in range(len(board[i])):
            flipped_stones = self.find_flipped(board, i, j, color)
            if len(flipped_stones) > 0:
                moves_found.update({(i,j): flipped_stones})
    return moves_found

   def find_flipped(self, board, x, y, color):
    # finds which chips would be flipped given a move and color
    if board[x][y] != ".":
        return []
    if color == self.black:
        my_color = "@"
    else:
        my_color = "O"
    flipped_stones = []
    for incr in self.directions:
        temp_flip = []
        x_pos = x + incr[0]
        y_pos = y + incr[1]
        while 0 <= x_pos < self.x_max and 0 <= y_pos < self.y_max:
            if board[x_pos][y_pos] == ".":
                break
            if board[x_pos][y_pos] == my_color:
                flipped_stones += temp_flip
                break
            temp_flip.append([x_pos, y_pos])
            x_pos += incr[0]
            y_pos += incr[1]
    return flipped_stones

class Best_AI_bot:

   def __init__(self):
      self.white = "O"
      self.black = "@"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = None
      self.y_max = None

   def best_strategy(self, board, color):
    # returns best move
      self.x_max = len(board)
      self.y_max = len(board[0])
      self.current = color
      if color == "#000000":
         color = "@"
      else:
         color = "O"
      self.current = color
      
      ''' Your code goes here ''' 
      best_move, v = self.alphabeta(board, color, 50, math.inf, -math.inf)
      if best_move == [-1,-1]:
          moves = list(self.find_moves(board,color).keys())
          move = random.choice(moves)
          best_move = [move[0], move[1]]
          return best_move, 0
      else:
          return best_move, v


   def minimax(self, board, color, search_depth):
    # returns best "value"
    if search_depth <= 0:
         return [-1,-1], self.evaluate(board,color,self.find_moves(board,color).keys())
    if len(self.find_moves(board,color)) == 0:
         self.current = self.opposite_color[self.current]
         return self.minimax(board,color,search_depth-1)
    #else:
    #    v = -math.inf
    #    if self.current != color:
    #        v = math.inf
    #    moves = self.find_moves(board,self.current)
    #    for move in moves:
    #        tempb = self.make_move(board,self.current,move,self.find_flipped(board,move[0],move[1],self.current))
    #        self.current = self.opposite_color[self.current]
    #        a = self.minimax(tempb,color,search_depth-1)[1]

    #        if color == self.current:
    #            if a > v:
    #                v  = a
    #                if search_depth == 3:
    #                    self.best_move = move
    #        else:
    #            if a < v:
    #                v = a
    #                if search_depth == 3:
    #                    self.best_move = move
    #    return self.best_move, v
    #return (-1,-1)

    best_move = 0

    if color == self.current:
          self.current = self.opposite_color[self.current]
          v = -math.inf
          moves = self.find_moves(board,color)
          for m in moves:
              b = self.make_move(board,color,m,self.find_flipped(board,m[0],m[1],color))
              #b = board
              t = self.minimax(b,color,search_depth-1)[1]
              if t > v:
                  v = t
                  best_move = m
          return (best_move, v)
    else:
        self.current = self.opposite_color[self.current]
        v = math.inf
        moves = self.find_moves(board,self.opposite_color[color])
        for m in moves:
            b = self.make_move(board,color,m,self.find_flipped(board,m[0],m[1],color))
            #b = board
            t = self.minimax(b,color,search_depth-1)[1]
            if v > t:
                v = t
                best_move = m
        return (best_move, v)


   def negamax(self, board, color, search_depth):
    # returns best "value"
      return 1
      
   def alphabeta(self, board, color, search_depth, alpha, beta):
    # returns best "value" while also pruning\
    best_move = [-1,-1]
    if search_depth <= 0:
         return best_move, self.evaluate(board,color,self.find_moves(board,color).keys())
    if len(self.find_moves(board,color)) == 0:
         self.current = self.opposite_color[self.current]
         return self.alphabeta(board,color,search_depth-1, alpha, beta)
    best_move = 0

    if color == self.current:
          self.current = self.opposite_color[self.current]
          v = -math.inf
          moves = self.find_moves(board,color)
          for m in moves:
              b = self.make_move(board,color,m,self.find_flipped(board,m[0],m[1],color))
              t = self.alphabeta(b,color,search_depth-1, alpha, beta)[1]
              if t > v:
                  v = t
                  best_move = m
              alpha = max(alpha,v)
              if v >= beta:
                      break
          return (best_move, v)
    else:
        self.current = self.opposite_color[self.current]
        v = math.inf
        moves = self.find_moves(board,self.opposite_color[color])
        for m in moves:
            b = self.make_move(board,self.opposite_color[color],m,self.find_flipped(board,m[0],m[1],self.opposite_color[color]))
            t = self.alphabeta(b,color,search_depth-1, alpha, beta)[1]
            if v > t:
                v = t
                best_move = m
            beta = min(beta,v)
            if v <= alpha:
                break
        return (best_move, v)

   def make_key(self, board, color):
    # hashes the board
      return 1

   def stones_left(self, board):
    # returns number of stones that can still be placed
    count = 0
    for c in board:
        count += c.count(".")
    return count

   def make_move(self, board, color, move, flipped):
    # returns board that has been updated
      nb = copy.deepcopy(board)
      nb[move[0]][move[1]] = color
      for b in flipped:
          nb[b[0]][b[1]] = color
      return nb

   def evaluate(self, board, color, possible_moves):
    # returns the utility value
      c = len(possible_moves)
      if color == self.white:
          oc = len(self.find_moves(board,self.black).keys())
      else:
          oc = len(self.find_moves(board,self.white).keys())
      return c - oc

   def score(self, board, color):
    # returns the score of the board 
      wcount = 0
      bcount = 0
      for b in board:
          wcount += b.count(self.white)
          bcount += b.count(self.black)
      
      if color == self.white:
          return wcount - bcount
      else:
          return bcount - wcount

   def find_moves(self, board, color):
    moves_found = {}
    for i in range(len(board)):
        for j in range(len(board[i])):
            flipped_stones = self.find_flipped(board, i, j, color)
            if len(flipped_stones) > 0:
                moves_found.update({(i,j): flipped_stones})
    return moves_found

   def find_flipped(self, board, x, y, color):
    # finds which chips would be flipped given a move and color
    if board[x][y] != ".":
        return []
    if color == self.black:
        my_color = "@"
    else:
        my_color = "O"
    flipped_stones = []
    for incr in self.directions:
        temp_flip = []
        x_pos = x + incr[0]
        y_pos = y + incr[1]
        while 0 <= x_pos < self.x_max and 0 <= y_pos < self.y_max:
            if board[x_pos][y_pos] == ".":
                break
            if board[x_pos][y_pos] == my_color:
                flipped_stones += temp_flip
                break
            temp_flip.append([x_pos, y_pos])
            x_pos += incr[0]
            y_pos += incr[1]
    return flipped_stones
