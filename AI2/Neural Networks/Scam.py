import sys; args = sys.argv[1:]
infile = open(args[0], 'r')

def main():
   training_set = []  # list of lists
   expected_set = []  # list of lists
   lines = infile.readlines()
   for line in lines:
        index = line.find('=')
        templ = line[:index].split(' ')
        expected = line[index+2:].split(' ')
        tset = [float(x) for x in templ if x != ""] + [1.0]
        expected_set.append([float(x) for x in expected if x != ""])
        training_set.append(tset)
   print("tset:")
   print(training_set)
   print("expected_set:")
   print(expected_set)

main()
#Satvik Matta, 5, 2023