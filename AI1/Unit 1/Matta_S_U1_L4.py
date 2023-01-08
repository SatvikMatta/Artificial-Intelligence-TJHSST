# Satvik Matta
# October 1,2021
import random
import collections
from collections import deque
import time
import copy

class HeapPriorityQueue():
   
   def __init__(self):
      self.queue = ["dummy"]  # we do not use index 0 for easy index calulation
      self.current = 1        # to make this object iterable

   def next(self):            # define what __next__ does
      if self.current >=len(self.queue):
         self.current = 1     # to restart iteration later
         raise StopIteration
    
      out = self.queue[self.current]
      self.current += 1
   
      return out

   def __iter__(self):
      return self

   __next__ = next

   def isEmpty(self):
      return len(self.queue) == 1    # b/c index 0 is dummy

   def swap(self, a, b):
      self.queue[a], self.queue[b] = self.queue[b], self.queue[a]

   # Add a value to the heap_pq
   def push(self, value):
      self.queue.append(value)
      self.heapUp(len(self.queue)-1) 

   # helper method for push      
   def heapUp(self, k):
      if k//2 == 0:
          return
      else:
        if self.queue[k//2] == None:
            return
        if self.queue[k] < self.queue[k//2]:
            self.swap(k,k//2)
            self.heapUp(k//2)
      return
               
   # helper method for reheap and pop
   def heapDown(self, k, size):
      i = 2*k
      j = i+1

      if i >= size:
          return
      minChild = i
      if j<size and self.queue[j] < self.queue[minChild]:
          minChild = j
      if self.queue[k] > self.queue[minChild]:
          self.swap(k,minChild)
          self.heapDown(minChild,size)
   
   # make the queue as a min-heap            
   def reheap(self):
      for i in (range(1,len(self.queue))):
          self.heapDown(i,len(self.queue))
   
   # remove the min value (root of the heap)
   # return the removed value            
   def pop(self):
      self.swap(1,len(self.queue)-1)
      i = self.queue.pop()
      self.heapDown(1,len(self.queue))
      return i # change this
      
   # remove a value at the given index (assume index 0 is the root)
   # return the removed value   
   def remove(self, index):
      self.swap(index+1,len(self.queue)-1)
      i = self.queue.pop()
      self.reheap()
      return i

  #Lab starts here

def inversion_count(new_state, width = 4, N = 4):
   ''' 
   Depends on the size(width, N) of the puzzle, 
   we can decide if the puzzle is solvable or not by counting inversions.
   If N is odd, then puzzle instance is solvable if number of inversions is even in the input state.
   If N is even, puzzle instance is solvable if
      the blank is on an even row counting from the bottom (second-last, fourth-last, etc.) and number of inversions is even.
      the blank is on an odd row counting from the bottom (last, third-last, fifth-last, etc.) and number of inversions is odd.
   ''' 
   b = new_state.find("_")
   nob_state = new_state.replace("_","")
   r = b//N
   c=0

   for i in nob_state:
       for j in nob_state[nob_state.index(i):]:
           if i >j:
               c+=1

   if N%2 == 1:
       if c%2==0:
           return True
   else:
       if r%2 ==0 and c%2 ==0:
           return True
       if r%2 ==1 and c%2 ==1:
           return True

   return False

def check_inversion():
   t1 = inversion_count("_42135678", 3, 3)  # N=3
   f1 = inversion_count("21345678_", 3, 3)
   t2 = inversion_count("4123C98BDA765_EF", 4) # N is default, N=4
   f2 = inversion_count("4123C98BDA765_FE", 4)
   return t1 and t2 and not (f1 or f2)


def getInitialState(sample, size):
   sample_list = list(sample)
   random.shuffle(sample_list)
   new_state = ''.join(sample_list)
   while not inversion_count(new_state, size, size): 
      random.shuffle(sample_list)
      new_state = ''.join(sample_list)
   return new_state
   
def swap(n, i, j):
   # Your code goes here
   return n[:i] + n[j] + n[i+1:j] + n[i] + n[j+1:]
      
'''Generate a list which hold all children of the current state
   and return the list'''
def generate_children(state, N=4):
   i = state.find('_')
   moves  = []
   if i//N - 1 >= 0:
        moves.append(swap(state, i-N, i))
   if i%N +1 <=N-1 :
        moves.append(swap(state,i,i+1))
   if i%N -1 >= 0:
       moves.append(swap(state,i-1,i))
   if i//N + 1 <= N-1:
       moves.append(swap(state, i, i+N))

   return moves

def display_path(path_list, size):
   for n in range(size):
      for path in path_list:
         print (path[n*size:(n+1)*size], end = " "*size)
      print ()
   print ("\nThe shortest path length is :", len(path_list))
   return ""

''' You can make multiple heuristic functions '''
def dist_heuristic(state, goal = "_123456789ABCDEF", size=4):
   count = 0
   for i in range(size*size):
      if state[i] != "_":
          start = state.index(state[i])
          finish = goal.index(state[i])
          count += abs(start%size - finish%size) + abs(start//size - finish//size)
   return count

def check_heuristic():
   a = dist_heuristic("152349678_ABCDEF", "_123456789ABCDEF", 4)
   b = dist_heuristic("8936C_24A71FDB5E", "_123456789ABCDEF", 4)
   return (a < b) 

def a_star(start, goal="_123456789ABCDEF", heuristic=dist_heuristic, size = 4):
   frontier = HeapPriorityQueue()
   if start == goal: return []
   htic = dist_heuristic(start)
   explored = set()
   frontier.push((htic,start,[start]))
   while not frontier.isEmpty():
       m = frontier.pop()
       if m[1] == goal:
           return m[2]
       else:
           for a in generate_children(m[1]):
               if not (a in explored):
                   f = dist_heuristic(a) + len(m[2]) + 1
                   frontier.push((f,a,m[2]+[a]))
                   explored.add(a)
   return None

def combine_path(start,goal,path,n,e1,e2):
    final= []
    if path[0] == start:
        final = path + e2[:-1][::-1]
    elif path[0] == goal:
        final = e1[:-1] + path[::-1]
    return final

def solve(start, goal="_123456789ABCDEF", heuristic=dist_heuristic, size = 4):
   f1 = HeapPriorityQueue()
   e1 = {start:[start]}
   f2 = HeapPriorityQueue()
   e2 = {goal:[goal]}
   f1.push((dist_heuristic(start),start,[start]))
   f2.push((dist_heuristic(goal,start),goal,[goal]))
   
   while not (f1.isEmpty() and f2.isEmpty()):
       s = f1.pop()
       g= f2.pop()

       if s[1] in e2.keys():
           return combine_path(start,goal,s[2],s[1],e1,e2[s[1]])
       if g[1] in e1.keys():
           return combine_path(start,goal,g[2],g[1],e1[g[1]],e2)

       for a in generate_children(s[1]):
               if not (a in e1):
                   temp = s[2]+[a]
                   f = dist_heuristic(a) + len(s[2]) + 1
                   f1.push((f,a,temp))
                   e1[a] = temp

       for a in generate_children(g[1]):
               if not (a in e2):
                   f = dist_heuristic(a,start) + len(g[2]) + 1
                   f2.push((f,a,g[2]+[a]))
                   e2[a] = g[2]+[a]

   return None




def main():
    # A star
   print ("Inversion works?:", check_inversion())
   print ("Heuristic works?:", check_heuristic())
   #initial_state = getInitialState("_123456789ABCDEF", 4)
   initial_state = input("Type initial state: ")
   #initial_state = "2A8956C341FED_7B"
   if inversion_count(initial_state) or True:
      cur_time = time.time()
      #path = (a_star(initial_state))
      path  = solve(initial_state)
      if path != None: display_path(path, 4)
      else: print ("No Path Found.")
      print ("Duration: ", (time.time() - cur_time))
   else: print ("{} did not pass inversion test.".format(initial_state))
   
if __name__ == '__main__':
   main()
