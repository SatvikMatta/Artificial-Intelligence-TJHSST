import sys; args = sys.argv[1:]
# myFile = open(args[0], "r")
myFile = open("/Volumes/GoogleDrive-114227365021912664420/My Drive/11th Grade/AI2/Neural Networks/weights.txt", "r")
import math
#Feed Forward Neural Network
def transfer(t_funct, x):
    if t_funct == 'T1':
        return x
    elif t_funct == 'T2':
        if x <= 0:
            return 0
        else:
            return x
    elif t_funct == 'T3':
        return 1.0 / (1.0 + math.exp(-x))
    elif t_funct == 'T4':
        return (2.0 / (1.0 + math.exp(-x))) - 1.0
    else:
        return x

def dot_product(x, y):
    return sum(a * b for a, b in zip(x, y))
    

def evaluate(myFile , input_vals, transferfunc):
    weights = []
    inputLength = len(input_vals)
    lines = myFile.readlines()
    for line in lines:
        weights.append(line.split())
    
    weights = [['0.5', '0', '0', '3', '-.25', '0', '0', '-2'], ['.6', '2', '-3', '-1.5']]
    
    for i in range(len(weights)):
        for j in range(len(weights[i])):
            weights[i][j] = float(weights[i][j])

    while len(weights) > 1:
        res = []
        for i in range(len(weights[0])//inputLength):
            res.append(dot_product(input_vals, weights[0][i*inputLength:(i+1)*inputLength]))
        input_vals = [transfer(transferfunc, x) for x in res]
        weights.pop(0)
        inputLength = len(input_vals)
    fres = []
    for i in range(len(weights[0])):
        fres.append(weights[0][i]*input_vals[i])
    return fres

def main():
    # inputs, t_funct, transfer_found = [], 'T1', False
    # for arg in args[1:]:
    #     if not transfer_found:
    #         t_funct, transfer_found = arg, True
    #     else:
    #         inputs.append(float (arg))
    inputs, t_funct = [-1.3,-1.9], 'T3'
    li = (evaluate(myFile, inputs, t_funct))
    print(li)




main()
#Satvik Matta, P5, 2023