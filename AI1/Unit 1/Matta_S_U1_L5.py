# Name: Satvik Matta         Date: October 6,2021
import time
import copy
import string
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

# Lab starts here


def generate_adjacents(current, words_set):
   ''' words_set is a set which has all words.
   By comparing current and words in the words_set,
   generate adjacents set of current and return it'''
   adj_set = set()
   for i in range(len(current)):
        alphabets = string.ascii_lowercase.replace(current[i],'')
        for a in alphabets:
            s= current[:i] + a + current[i+1:]
            if s in words_set:
                adj_set.add(s)
   return adj_set

def check_adj(words_set):
   # This check method is written for words_6_longer.txt
   adj = generate_adjacents('listen', words_set)
   target =  {'listee', 'listel', 'litten', 'lister', 'listed'}
   return (adj == target)

def genpath(start, n, explored):
   l = []
   while explored[n] != "": 
      l.append(n)
      n = explored[n]
   l.append(start)
   l = l[::-1]
   return l

def bi_bfs(start, goal, words_set):
   '''The idea of bi-directional search is to run two simultaneous searches--
   one forward from the initial state and the other backward from the goal--
   hoping that the two searches meet in the middle. 
   '''
   if start == goal: return []
   f1 = [start]
   f2 = [goal]
   e1 = {start: ""}
   e2 = {goal: ""}
   while len(f1) >= 1 and len(f2) >= 1: 
       t = copy.deepcopy(f1)
       f1 = []
       while len(t) > 0:
           s = t.pop(0)
           if s in f2:
               u = genpath(start,s,e1)[:-1] + list(reversed(genpath(start,s,e2)))
               u[-1] = goal
               return u
           for a in generate_adjacents(s,words_set):
               if a not in e1:
                   f1.append(a)
                   e1[a] = s
       t = copy.deepcopy(f2)
       f2 = []
       while len(t) > 0:
           s = t.pop(0)
           if s in f1:
               u = genpath(start,s,e1)[:-1] + list(reversed(genpath(start,s,e2)))
               u[-1] = goal
               return u
           for a in generate_adjacents(s,words_set):
               if a not in e2:
                   f2.append(a)
                   e2[a] = s
   return None
def dist_heuristic(start,goal):
   count = 0
   for i in range(len(goal)):
      if goal[i] != start[i]:
          count += 1
   return count

def a_star(start,goal,words):
   frontier = HeapPriorityQueue()
   if start == goal: return []
   htic = dist_heuristic(start,goal)
   explored = set()
   frontier.push((htic,start,[start]))
   while not frontier.isEmpty():
       m = frontier.pop()
       if m[1] == goal:
           return m[2]
       else:
           for a in generate_adjacents(m[1], words):
               if not (a in explored):
                   f = dist_heuristic(a,goal) + len(m[2]) + 1
                   frontier.push((f,a,m[2]+[a]))
                   explored.add(a)
   return None

def main():
   filename = input("Type the word file: ")
   words_set = set()
   file = open(filename, "r")
   for word in file.readlines():
      words_set.add(word.rstrip('\n'))
   #print ("Check generate_adjacents():", check_adj(words_set))
   initial = input("Type the starting word: ")
   goal = input("Type the goal word: ")
   cur_time = time.time()
   #path = (bi_bfs(initial, goal, words_set))
   path = (a_star(initial, goal, words_set))
   if path != None:
      print (path)
      print ("The number of steps: ", len(path))
      print ("Duration: ", time.time() - cur_time)
   else:
      print ("There's no path")
 
if __name__ == '__main__':
   main()

'''
Sample output 1
Type the word file: words.txt
Type the starting word: listen
Type the goal word: beaker
['listen', 'listed', 'fisted', 'fitted', 'fitter', 'bitter', 'better', 'beater', 'beaker']
The number of steps:  9
Duration: 0.0

Sample output 2
Type the word file: words_6_longer.txt
Type the starting word: listen
Type the goal word: beaker
['listen', 'lister', 'bister', 'bitter', 'better', 'beater', 'beaker']
The number of steps:  7
Duration: 0.000997304916381836

Sample output 3
Type the word file: words_6_longer.txt
Type the starting word: vaguer
Type the goal word: drifts
['vaguer', 'vagues', 'values', 'valves', 'calves', 'cauves', 'cruves', 'cruses', 'crusts', 'crufts', 'crafts', 'drafts', 'drifts']
The number of steps:  13
Duration: 0.0408782958984375

Sample output 4
Type the word file: words_6_longer.txt
Type the starting word: klatch
Type the goal word: giggle
['klatch', 'clatch', 'clutch', 'clunch', 'glunch', 'gaunch', 'paunch', 'paunce', 'pawnce', 'pawnee', 'pawned', 'panned', 'panged', 'ranged', 'ragged', 'raggee', 'raggle', 'gaggle', 'giggle']
The number of steps:  19
Duration:  0.0867915153503418
'''


