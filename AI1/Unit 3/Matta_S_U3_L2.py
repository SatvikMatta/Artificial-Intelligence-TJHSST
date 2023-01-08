# Name:
# Date:
import random
import math
import copy

from Matta_S_U3_L1 import minimax
class RandomPlayer:
   def __init__(self):
      self.white = "#ffffff" #"O"
      self.black = "#000000" #"X"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = None
      self.y_max = None
      self.first_turn = True
      
   def best_strategy(self, board, color):
      # Terminal test: when there's no more possible move
      #                return (-1, -1), 0
      moves = self.find_moves(board,color)
      if len(moves) == 0:
          return (-1,-1), 0

      # returns best move
      # (column num, row num), 0
      m  = random.sample(moves,1)
      row = m[0]%5
      col = m[0]//5
      return (col,row), 0
      
     
   def find_moves(self, board, color):
      # finds all possible moves
      # returns a set, e.g., {0, 1, 2, 3, ...., 24} 
      # 0 5 10 15 20
      # 1 6 11 16 21
      # 2 7 12 17 22
      # 3 8 13 18 23
      # 4 9 14 19 24
      # if 2 has 'X', board = [['.', '.', 'X', '.', '.'], [col 2], .... ]
      row  = -1
      col = -1
      if color  == self.white:
          turn = "O"
      else:
          turn  = "X"

      if turn  == "X":
          empty = True
          for b in board:
              if "O" in b:
                  empty = False
          if empty:
              return set(range(25))
          else:
              for i in range(len(board)):
                  if "X" in board[i]:
                      col = i
                      for j in range(len(board[i])):
                          if board[i][j] == "X":
                              row = j
              
              moves = set()
              for d in self.directions:
                  for j in range(1,5):
                         nc = col+j*d[1]
                         nr = row + j*d[0]
                         if nc >= 0 and nc < 5 and nr >=0 and nr<5:
                             if board[nc][nr] != ".":
                                 break
                             m = nc*5+nr
                             if m in set(range(25)):
                                moves.add(m)
              return moves
      else:
        for i in range(len(board)):
                  if "O" in board[i]:
                      col = i
                      for j in range(len(board[i])):
                          if board[i][j] == "O":
                              row = j
              
        moves = set()
        for d in self.directions:
            for j in range(1,5):
                    nc = col+j*d[1]
                    nr = row + j*d[0]
                    if nc >= 0 and nc < 5 and nr >=0 and nr<5:
                        if board[nc][nr] != ".":
                            break
                        m = nc*5+nr
                        if m in set(range(25)):
                            moves.add(m)
        return moves

      #row = -1
      #col = -1
      #t = ""
      #if color  == self.white:
      #    turn = "O"
      #else:
      #    turn  = "X"
      #for i in range(len(board)):
      #    if board[i].count(turn) == 1:
      #        col = i
      #        for j in range(len(board[i])):
      #            if j == board[i][j]:
      #                row = j
      #if row == -1 or col == -1:
      #    if turn == "X":
      #      ro = -1
      #      co = -1
      #      for i in range(len(board)):
      #         if board[i].count("X") == 1:
      #          col = i
      #          for j in range(len(board[i])):
      #              if board[i][j] == "X":
      #                  row = j
      #moves = set()
      #for d in self.directions:
      #    for j in range(4 - max(int(row),int(col))):
      #           nc = col+j*d[1]
      #           nr = row + j*d[0]
      #           if board[nc][nr] != ".":
      #               break
      #           m = nc*5+nr
      #           moves.add(m)
      #return moves
      pass

class CustomPlayer:

   def __init__(self):
      self.white = "#ffffff" #"O"
      self.black = "#000000" #"X"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = None
      self.y_max = None
      self.first_turn = True

   def best_strategy(self, board, color):

       m,v = self.minimax(board,color,2)
       if m != None:
        row = m%5
        col = m//5
        return (col,row), v
       else:
            moves = self.find_moves(board,color)
            if len(moves) == 0:
                moves = set(range(1,25))
            # returns best move
            # # (column num, row num), 0
            m  = random.sample(moves,1)
            row = m[0]%5
            col = m[0]//5
            return (col,row), 1


      # returns best move
            # moves = self.find_moves(board,color)
            # if len(moves) == 0:
            #     return (-1,-1), 0

            # # returns best move
            # # (column num, row num), 0
            # m  = random.sample(moves,1)
            # row = m[0]%5
            # col = m[0]//5
            # return (col,row), 0
    
      #return best_move, 0

   def suc(self,board, color):
        if color  == self.white:
          turn = "O"
        else:
          turn  = "X"
        moves = self.find_moves(board,color)
        if len(moves) == 0:
            return []
        j = []
        for m in moves:
            row = m%5
            col = m//5
            b = copy.deepcopy(board)
            b[col][row] = turn
            j.append((b,m))
        return j
   def minimax(self, board, color, search_depth):
       return self.minimax1(board,color,2,False)

   def minimax1(self, board, color, search_depth, other, best_move = None):
      # search_depth: start from 2
      # returns best "value"
      if self.find_moves(board,color) == 0 or self.find_moves(board,self.opposite_color) == 0 or search_depth == 0:
          return best_move, self.evaluate(board, color, self.find_moves(board,color))
      elif other:
          a = math.inf
          for c,m in self.suc(board, color):
              temp = self.minimax1(c,color,search_depth-1,False, best_move=m)[1]
              if temp < a:
                  a = temp
                  best_move = m
            #   a = min(a, self.minimax(c,color,search_depth-1,False))
      else:
          a = -math.inf
          for c,m in self.suc(board,color):
              temp = -1* self.minimax1(c,self.opposite_color[color],search_depth-1,True, best_move=m)[1]
              if a < temp:
                a=temp
                best_move = m
            #   a = max(a,self.minimax(c,color,search_depth-1,True))
      return best_move, a
   #def minimax(self, board, color, search_depth):
   #    return self.max_value(board,color,search_depth,n=None)
   #def max_value(board,color,search_depth,n):
   #    if search_depth == 0 or self.find_moves(board,color) == 0 or self.find_moves(board,self.opposite_color) == 0:
   #        return n,self.evaluate(board,color,self.find_moves(color))
   #    v = -math.inf
   #    opt = ""
   #    if turn == "O":
   #                opt = "X"
   #    else:
   #                opt = "O"
   #    for a in suc(board,color):
   #        m = min_value(board,color,search_depth)[1]
   #        if v < m:
   #         v = m
   #         n = a
   #    return (a[0],a[1])
   
   #def min_value(board,color,search_depth,n):
   #    # return value and state: (val, state)
   #    if search_depth == 0 or self.find_moves(board,color) == 0 or self.find_moves(board,self.opposite_color) == 0:
   #        return utility(turn,tc,state), state
   #    v = math.inf
   #    opt = ""
   #    if turn == "O":
   #                opt = "X"
   #    else:
   #                opt = "O"
   #    for a,s in successors(state,opt):
   #        m = max_value(s, turn, tc)[0]
   #        if v > m:
   #         v = m
   #         state = s
   #    return (v, state)

   def negamax(self, board, color, search_depth):
      # returns best "value"
      return 1
      
   def alphabeta(self, board, color, search_depth, alpha, beta):
      # returns best "value" while also pruning
      pass

   def make_move(self, board, color, move):
      # returns board that has been updated
      return board

   def evaluate(self, board, color, possible_moves):
      # returns the utility value
      # count possible_moves (len(possible_moves)) of my turn at current board
      # opponent's possible_moves: self.find_moves(board, self.opposite_color(color))
      return len(possible_moves) - len(self.find_moves(board,self.opposite_color))

   def find_moves(self, board, color):
      # finds all possible moves
      row  = -1
      col = -1
      if color  == self.white:
          turn = "O"
      else:
          turn  = "X"

      if turn  == "X":
          empty = True
          for b in board:
              if "O" in b:
                  empty = False
          if empty:
              return set(range(25))
          else:
              row_op = -1
              col_op = -1
              for i in range(len(board)):
                  if "O" in board[i]:
                      col_op = i
                      for j in range(len(board[i])):
                          if board[i][j] == "O":
                              row_op = j

              for i in range(len(board)):
                  if "X" in board[i]:
                      col = i
                      for j in range(len(board[i])):
                          if board[i][j] == "X":
                              row = j
              
              moves = set()
              for d in self.directions:
                  for j in range(1,5):
                         nc = col+j*d[1]
                         nr = row + j*d[0]
                         if nc >= 0 and nc < 5 and nr >=0 and nr<5:
                             if board[nc][nr] != ".":
                                 break
                             m = nc*5+nr
                             if m in set(range(25)):
                                moves.add(m)
              return moves
      else:
        for i in range(len(board)):
                  if "O" in board[i]:
                      col = i
                      for j in range(len(board[i])):
                          if board[i][j] == "O":
                              row = j
              
        moves = set()
        for d in self.directions:
            for j in range(1,5):
                    nc = col+j*d[1]
                    nr = row + j*d[0]
                    if nc >= 0 and nc < 5 and nr >=0 and nr<5:
                        if board[nc][nr] != ".":
                            break
                        m = nc*5+nr
                        if m in set(range(25)):
                            moves.add(m)
        return moves

