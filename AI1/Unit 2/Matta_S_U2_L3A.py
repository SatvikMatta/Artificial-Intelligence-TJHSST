# Name:Satvik Matta
# Date: 11/16/2021

import random
import copy
def check_complete(assignment, csp_table):
   #if "." in assignment: return False
   #for i in csp_table:
   #        x = [assignment[k] for k in i]
   #        if len(x) != len(set(x)):
   #            return False
   #return True
   if assignment.find('.') != -1: return False
   for k in csp_table:
      if len(set([assignment[i] for i in k])) != 9: return False
   return True
   
def select_unassigned_var(assignment, variables, csp_table):
   pv = []
   x = [len(variables[v]) for v in variables]
   m = min(x)
   for v in variables:
       if len(variables[v])== m:
           pv.append(v)
   return random.choice(pv)


def isValid(value, var_index, assignment, variables, csp_table):
   for i in csp_table:
           if var_index in i:
               for k in i:
                   if assignment[k] == value:
                       return False
   return True
   #for k in csp_table:
   #   if var_index in k:
   #       for i in k:
   #           if i != var_index:
   #             if str(value) == assignment[i]:
   #                 return False
   #return True

def ordered_domain(var_index,assignment, variables, csp_table):
   return []

def update_variables(value, var_index, assignment, variables, csp_table):
   vars = copy.deepcopy(variables)
   del[vars[var_index]]
   for i in csp_table:
       if var_index in i:
           for k in i:
               if k in vars:
                   if value in vars[k]:
                    vars[k].remove(value)
   return vars


def backtracking_search(puzzle, variables, csp_table): 
   return recursive_backtracking(puzzle, variables, csp_table)

def recursive_backtracking(assignment, variables, csp_table):
   if check_complete(assignment,csp_table):
       return assignment
   v = select_unassigned_var(assignment,variables, csp_table)
   for i in variables[v]:
       if isValid(i,v,assignment,variables,csp_table) == True:
        #temp  = list(assignment)
        #temp[v] = "."
        #assignment = "".join(temp)

        temp  = list(assignment)
        temp[v] = i
        assignment = "".join(temp)
        vars = update_variables(i,v,assignment,variables,csp_table)
       
        result = recursive_backtracking(assignment,vars,csp_table)
        if result != None:
               display(result)
               return result
        temp  = list(assignment)
        temp[v] = "."
        assignment = "".join(temp)
   return None

def display(solution):
   #print(solution[0:3], end = "\t")
   #print(solution[3:6], end = "\t")
   #print(solution[3:9])
   s = ""
   c = 0
   for j in range(9):
    i = j*9
    s += solution[i:i+3] + "\t"
    s += solution[i+3:i+6] + "\t"
    s += solution[i+6:i+9] + "\n"
    c+=1
    if c %3 == 0:
        s+="\n"
   return s

def sudoku_csp():
   #final = []
   #t = []
   #for i in range(9):
   #    t.append(i)
   #final.append(t)
   #for j in range(8):
   # for i in range(9):
   #     t[i] = t[i]+9
   # final.append(t)
   #for i in range(9):
   #    t= []
   #    for j in range(9):
   #        t.append(j*9+i)
   #    final.append(t)
   #final.append([0,1,2,9,10,11,18,19,20])
   f = [[0, 1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16, 17],[18, 19, 20, 21, 22, 23, 24, 25, 26], [27, 28, 29, 30, 31, 32, 33, 34, 35],[36, 37, 38, 39, 40, 41, 42, 43, 44], [45, 46, 47, 48, 49, 50, 51, 52, 53],[54, 55, 56, 57, 58, 59, 60, 61, 62], [63, 64, 65, 66, 67, 68, 69, 70, 71],[72, 73, 74, 75, 76, 77, 78, 79, 80], [0, 9, 18, 27, 36, 45, 54, 63, 72],[1, 10, 19, 28, 37, 46, 55, 64, 73], [2, 11, 20, 29, 38, 47, 56, 65, 74],[3, 12, 21, 30, 39, 48, 57, 66, 75], [4, 13, 22, 31, 40, 49, 58, 67, 76],[5, 14, 23, 32, 41, 50, 59, 68, 77], [6, 15, 24, 33, 42, 51, 60, 69, 78],[7, 16, 25, 34, 43, 52, 61, 70, 79], [8, 17, 26, 35, 44, 53, 62, 71, 80],[0, 1, 2, 9, 10, 11, 18, 19, 20], [3, 4, 5, 12, 13, 14, 21, 22, 23],[6, 7, 8, 15, 16, 17, 24, 25, 26], [27, 28, 29, 36, 37, 38, 45, 46, 47],[30, 31, 32, 39, 40, 41, 48, 49, 50], [33, 34, 35, 42, 43, 44, 51, 52, 53],[54, 55, 56, 63, 64, 65, 72, 73, 74], [57, 58, 59, 66, 67, 68, 75, 76, 77],[60, 61, 62, 69, 70, 71, 78, 79, 80]]
   return f
   

def initial_variables(puzzle, csp_table):
   vars = {}
   for i in range(len(puzzle)):
       if puzzle[i] == ".":
           vars[i] = {'1','2','3','4','5','6','7','8','9'}
           for j in csp_table:
               if i in j:
                   for k in j:
                       if puzzle[k] != ".":
                           if puzzle[k] in vars[i]:
                            vars[i].remove(puzzle[k])
   return vars
   
def main():
   puzzle = input("Type a 81-char string:") 
   while len(puzzle) != 81:
      print ("Invalid puzzle")
      puzzle = input("Type a 81-char string: ")
   csp_table = sudoku_csp()
   variables = initial_variables(puzzle, csp_table)
   print ("Initial:\n" + display(puzzle))
   solution = backtracking_search(puzzle, variables, csp_table)
   if solution != None: print ("solution\n" + display(solution))
   else: print ("No solution found.\n")
   
if __name__ == '__main__': main()
