import string
#make graph
def mgraph():
   graph = {}
   wordset = set()
   with open('words.txt') as infile:
       for word in infile:
           wordset.add(word.strip())
   for word in wordset:
       graph[word] = set()
       for i in range(len(word)):
        alphabets = string.ascii_lowercase.replace(word[i],'')
        for a in alphabets:
            s= word[:i] + a + word[i+1:]
            if s in wordset:
                graph[word].add(s)
   return graph
#return set
def generate_adjacents(current, word_list):
    adj_list = set()
    adj_list = word_list
    return adj_list

#BFS display path
def display_path(start, n, explored): 
   l = []
   while explored[n] != "s": 
      l.append(n)
      n = explored[n]
   l.append(start)
   l = l[::-1]
   return l

#BFS
def BFS(start,end,word_dict):
   explored = {start: "s"}
   q = [start]
   while(len(q) > 0):
       c = q.pop(0)
       if c == end:
           a = display_path(start,c,explored)
           return a,len(a)
       else:
            if c in word_dict.keys():
                for a in generate_adjacents(c,word_dict[c]):
                    if a not in explored:
                        q.append(a)
                        explored[a] = c
   return "FAIL","FAIL"

def recur(start,end,word_dict,explored,limit):
    if start == end:
        return [start]
    elif limit == 0:
        return None
    else:
        for a in generate_adjacents(start,word_dict[start]):
            if a not in explored:
                explored[a] = start
                result  = recur(a,end,word_dict,explored,limit-1)
                if result != None:
                    return [start] + result
                del explored[a]
    return None

def DLS(start,end,word_dict,limit):
    explored = {start:"s"}
    a = recur(start,end,word_dict,explored,limit-1)
    if(a == None):
        return "FAIL",-1
    return a,len(a)
    

def main():
    start = input("Type the starting word: ")
    end = input("Type the goal word: ")
    graph = mgraph()
    path,steps = BFS(start,end,graph)
    print(path)
    print("The number of steps: " + str(steps))
    limit = input("Type the limit (1 - 20): ")
    start = input("Type the starting word: ")
    end = input("Type the goal word: ")
    f,steps = DLS(start,end,graph,int(limit))
    print(f)
    print("Steps within " + limit + " limit: ", end = "")
    print(len(f))
    limit = 1
    while DLS(start,end,graph,limit) == ("FAIL",-1):
        limit+=1
    path,steps = DLS(start,end,graph,limit)
    print("Shortest Path: " + str(path))
    print("Steps: " + str(steps))

    

main()