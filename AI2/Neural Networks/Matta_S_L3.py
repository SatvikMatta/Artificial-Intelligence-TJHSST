import sys; args = sys.argv[1:]
import math, random
args = ["x*x + y*y < 1.5"]
#   #FF: feed forward
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
    

def evaluate(weightss, input_vals, transferfunc, x_vals, k):
    weights = [x for x in weightss]
    for i in range(len(weights)):
        for j in range(len(weights[i])):
            weights[i][j] = float(weights[i][j])
    inputLength = len(input_vals)
    count = 1
    while len(weights) > 1:
        res = []
        for i in range(len(weights[0])//inputLength):
            res.append(dot_product(input_vals, weights[0][i*inputLength:(i+1)*inputLength]))
        input_vals = [transfer(transferfunc, x) for x in res]
        weights.pop(0)
        x_vals[k][count] = input_vals
        count += 1
        inputLength = len(input_vals)
    fres = []
    for i in range(len(weights[0])):
        fres.append(weights[0][i]*input_vals[i])
    return fres

def forward_feed(input, weights, transferfunc, x_vals, k):
   li  = evaluate(weights, input, transferfunc, x_vals, k)
   x_vals[k][-1] = li
   # print("Forward Feed Result :", end = str(li) + "\n")
   return li

##################################

def backprop(x_vals, ex, negative_grad, weights, learning_rate):
    #[4,2,1,1]
    # weights = [[-1.4, 0.9, -1.1, 1.5, 0.6, -1.2, -1.5, -0.5], 
    #           [-1.8, 1.6], 
    #           [0.3]]
    # x_vals = [[1, 0, 1, 1], [0.269, 0.198], [0.458], [0.137]]
    # expected = [1.0]
    # negative_grad = [[*i] for i in weights]  #copy elements from weights, negative gradients has the same structures with weights
    # learning_rate = 4
    expected = [ex]
    ev = [[*i] for i in x_vals]
    starting = expected[0] - x_vals[-1][0]
    ev[-1][0] = starting
    # i is each layer in the xvals
    negative_grad[-1][0] = negative_grad[-1][0] = starting * x_vals[-2][0]

    for i in range(2,len(negative_grad)+1):
        for j in range(len(x_vals[-i])):
            for y in range(len(ev[-i+1])):
                temp  = weights[-(i-1)][j] * ev[-(i-1)][y] * x_vals[-i][j] * (1 - x_vals[-i][j])
                ev[-i][j] = temp
            for k in range(len(x_vals[-(i+1)])*j, len(x_vals[-(i+1)])*(j+1)):
                negative_grad[-i][k] = temp * x_vals[-(i+1)][k % len(x_vals[-(i+1)])]
    update_weights(weights, negative_grad, learning_rate)
    return weights





def update_weights(weights, negative_grad, learning_rate):
    for i in range(len(weights)):
      for j in range(len(weights[i])):
         weights[i][j] = weights[i][j] + learning_rate * negative_grad[i][j]

##################################

def make_points(r2, num_points = 100000, t = ">"):
    points = []
    expectected = []
    for i in range(num_points):
        point = [random.uniform(-1.5,1.5), random.uniform(-1.5,1.5)] + [1.0]
        points.append(point)
        if t == ">":
            if point[0]*point[0] + point[1]*point[1] > r2:
                expectected.append(1.0)
            else:
                expectected.append(0.0)
        else:
            if point[0]*point[0] + point[1]*point[1] < r2:
                expectected.append(1.0)
            else:
                expectected.append(0.0)
    return points, expectected


def main():
    if "=" in args[0]:
        args[0]=args[0].replace("=","")
    if ">" in args[0]:
        r2 = args[0][args[0].find(">")+1:]
        r2 = float(r2.strip())
        t = ">"
    elif "<" in args[0]:
        r2 = args[0][args[0].find("<")+1:]
        r2 = float(r2.strip())
        t = "<"
    points, expected = make_points(r2, 100, t)
    layer_count = [3,6,6,4,1,1]
    print("Layer Count: ", end = str(layer_count) + "\n")
    weights = [[round(random.uniform(-2.0, 2.0), 2) for j in range(layer_count[i]*layer_count[i+1])]  for i in range(len(layer_count)-1)]
    x_vals = [[temp[0:len(temp)-1]] for temp in points] # x_vals starts with first input values
    for i in range(len(points)):
      for j in range(len(layer_count)):
         if j == 0: x_vals[i][j].append(1.0)
         else: x_vals[i].append([0 for temp in range(layer_count[j])])

    negative_grad = [[*i] for i in weights]  #copy elements from weights, negative gradients has the same structures with weights
    errors = [10]*len(points)  # Whenever FF is done once, error will be updated. Start with 10 (a big num)
    count = 1  # count how many times you trained the network, this can be used for index calc or for decision making of 'restart'
    alpha = 0.9
    print(expected)
    res = []
    for k in range(len(points)):
        ffres = forward_feed(points[k], weights, 'T3',x_vals, k)
        res.append(ffres)
        for i in range(len(ffres)):
            err = math.pow((expected[k] - ffres[i]),2)/2
            errors[k] = err
    
    # print(sum(errors))

    if sum(errors) <= 8.0:
        for we in weights:
            for w in we:
                print(w, end = " ")
            print()
            return
    
    bestw = weights
    beste = sum(errors)
    ace = 5.5
    while True:
         for k in range(len(points)):
            ffres = forward_feed(points[k], weights, 'T3',x_vals, k)
            current_x_vals = x_vals[k]
            weights = backprop(current_x_vals, expected[k], negative_grad, weights, alpha)
            # print(weights)
         res = []
         for k in range(len(points)):
            ffres = forward_feed(points[k], weights, 'T3',x_vals, k)
            res.append(ffres)
            for i in range(len(ffres)):
               err = math.pow((expected[k] - ffres[i]),2)/2
               errors[k] = err
         # print("Error: ", end = str(sum(errors)))
         # print()
         e = sum(errors)
        #  print("Error: ", end = str(e) + "\n")
         result = ""
         if e <= beste:
            bestw = weights
            beste = e
         else:
            bestw = [[round(random.uniform(-2.0, 2.0), 2) for j in range(layer_count[i]*layer_count[i+1])]  for i in range(len(layer_count)-1)]
            weights = bestw
            ace = beste
            res = []
            for k in range(len(points)):
                ffres = forward_feed(points[k], weights, 'T3',x_vals, k)
                res.append(ffres)
                for i in range(len(ffres)):
                    err = math.pow((expected[k] - ffres[i]),2)/2
                    errors[k] = err
            beste = sum(errors)
         if beste < ace:
            for we in bestw:
                        for w in we:
                            result += str(w) + " "
                        result += "\n"
            print(result)
         if beste <= 1.0:
            return
    
    
    

main()
#Satvik Matta, P5, 2023