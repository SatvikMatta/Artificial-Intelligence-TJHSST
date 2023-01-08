# Name: Satvik Matta
# Date: November 10, 2021
import random
import copy
global finset
finset = []

   
def select_unassigned_var(assignment, csp_table):
   t = []
   for i in range(20):
       if assignment.count(i) == 0:
           t.append(i)
   return t
   
def isValid(v,assignment, csp_table):
   for i in assignment:
       if i in csp_table[v]:
           return False
   return True

def backtracking_search(input, csp_table): 
   return recursive_backtracking(input, csp_table)

def recursive_backtracking(assignment, csp_table):
   v = select_unassigned_var(assignment, csp_table)
   for i in v:
       temp  = assignment
       temp.append(i)
       if isValid(i,temp,csp_table) == False:
        temp.remove(i)
       else:
           finset.append(copy.deepcopy(temp))
           recursive_backtracking(temp, csp_table)


def main():
   csp_table = {0:[10,1,19], 1:[0,8,2], 2:[1,6,3],3:[2,4,19],4:[5,17,3],5:[6,15,4],6:[2,5,7],7:[8,14,6],8:[1,9,7],9:[8,13,10],10:[0,9,11],11:[10,12,18],12:[13,16,11], 13:[9,14,12], 14:[7,13,15], 15:[5,16,14], 16:[15,12,17], 17:[4,18,16], 18:[17,19,11], 19:[0,3,18]} 
   solution = backtracking_search([], csp_table)
   print(finset)

if __name__ == '__main__':
   main()
   
"""
Sample Output 1:
24-char(. and 1-6) input: ........................
  1 2 3 1 2 
1 4 5 6 4 5 1 
2 6 3 1 2 3 6 
  2 4 5 4 6 

123121456451263123624546
True

Sample Output 2:
24-char(. and 1-6) input: 6.....34...1.....2..4...
  6 1 2 1 3 
1 3 4 5 6 4 1 
5 6 2 1 3 2 5 
  3 4 5 4 6 

612131345641562132534546
True
"""

