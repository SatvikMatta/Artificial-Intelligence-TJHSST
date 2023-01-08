# Name: Satvik Matta
# Period: 5

from tkinter import *
from graphics import *
import random

def check_complete(assignment, vars, adjs):
   # check if assignment is complete or not. Goal_Test
    return len(assignment.keys()) == len(vars)

def select_unassigned_var(assignment, vars, adjs):
   # Select an unassigned variable - forward checking, MRV, or LCV
   # returns a variable
   t = []
   for i in vars.keys():
       if i not in assignment.keys():
           t.append(i)
   return random.choice(t)

   
def isValid(value, var, assignment, variables, adjs):
   # value is consistent with assignment
   # check adjacents to check 'var' is working or not.
   for i in assignment.keys():
      if i in adjs.keys():
        for j in adjs[i]:
          if j in assignment.keys():
            if assignment[i] == assignment[j]:
               return False
   return True

def backtracking_search(variables, adjs, shapes, frame): 
   return recursive_backtracking({}, variables, adjs, shapes, frame)

def recursive_backtracking(assignment, variables, adjs, shapes, frame):
   if check_complete(assignment, variables,adjs):
       return assignment
   v = select_unassigned_var(assignment,variables,adjs)
   for i in variables[v]:
       assignment[v] = i
       if isValid(i, v, assignment,variables, adjs) == False:
           del assignment[v]
       else:
           result = recursive_backtracking(assignment,variables,adjs,shapes,frame)
           if result != None:
               draw_shape(shapes[v],frame,i)
               return result
           del assignment[v]
   return None

# return shapes as {region:[points], ...} form
def read_shape(filename):
   infile = open(filename)
   region, points, shapes = "", [], {}
   for line in infile.readlines():
      line = line.strip()
      if line.isalpha():
         if region != "": shapes[region] = points
         region, points = line, []
      else:
         x, y = line.split(" ")
         points.append(Point(int(x), 300-int(y)))
   shapes[region] = points
   return shapes

# fill the shape
def draw_shape(points, frame, color):
   shape = Polygon(points)
   shape.setFill(color)
   shape.setOutline("black")
   shape.draw(frame)
   space = [x for x in range(9999999)] # give some pause
   
def main():
   regions, variables, adjacents  = [], {}, {}
   # Read mcNodes.txt and store all regions in regions list
   with open("mcNodes.txt") as infile:
       lines = infile.readlines()
       for l in lines:
           regions.append(l.strip())
   
   # Fill variables by using regions list -- no additional code for this part
   for r in regions: variables[r] = {'red', 'green', 'blue'}

   # Read mcEdges.txt and fill the adjacents. Edges are bi-directional.
   with open("mcEdges.txt") as infile:
       lines = infile.readlines()
       for l in lines:
           a = l.strip().split(" ")
           if a[0] in adjacents.keys():
               adjacents[a[0]].add(a[1])
           else:
               adjacents[a[0]] = set()
               adjacents[a[0]].add(a[1])

           if a[1] in adjacents.keys():
               adjacents[a[1]].add(a[0])
           else:
               adjacents[a[1]] = set()
               adjacents[a[1]].add(a[0])


   # Set graphics -- no additional code for this part
   frame = GraphWin('Map', 300, 300)
   frame.setCoords(0, 0, 299, 299)
   shapes = read_shape("mcPoints.txt")
   for s, points in shapes.items():
      draw_shape(points, frame, 'white')
  
   # solve the map coloring problem by using backtracking_search -- no additional code for this part  
   solution = backtracking_search(variables, adjacents, shapes, frame)
   print (solution)
   
   mainloop()

if __name__ == '__main__':
   main()
   
''' Sample output:
{'WA': 'red', 'NT': 'green', 'SA': 'blue', 'Q': 'red', 'NSW': 'green', 'V': 'red', 'T': 'red'}
By using graphics functions, visualize the map.
'''