import sys; args = sys.argv[1:]
infile = open(args[0], 'r')
#infile = open("/Volumes/GoogleDrive-114227365021912664420/My Drive/11th Grade/AI2/Neural Networks/x_gate.txt", 'r')
import math, random
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

#####################################################

def backpropigation(x_vals, expected, negative_grad, weights, learning_rate):
   starting = expected[0] - x_vals[-1][0]
   negative_grad[-1][0] = starting * x_vals[-2][0]
   s2 = weights[-1][0] * starting * x_vals[-2][0] * (1-x_vals[-2][0])
   negative_grad[-2][0] = s2 * x_vals[-3][0]
   negative_grad[-2][1] = s2 * x_vals[-3][1]
   s3 = weights[-2][0] * s2 * x_vals[-3][0] * (1-x_vals[-3][0])
   negative_grad[-3][0] = s3 * x_vals[-4][0]
   negative_grad[-3][1] = s3 * x_vals[-4][1]
   negative_grad[-3][2] = s3 * x_vals[-4][2]
   s4 = weights[-2][1] * s2 * x_vals[-3][1] * (1-x_vals[-3][1])
   negative_grad[-3][3] = s4 * x_vals[-4][0]
   negative_grad[-3][4] = s4 * x_vals[-4][1]
   negative_grad[-3][5] = s4 * x_vals[-4][2]
   update_weights(weights, negative_grad, learning_rate)
   return weights
   
def backprop2(x_vals, expected, negative_grad, weights, learning_rate):
   starting = expected[0] - x_vals[-1][0]
   negative_grad[-1][0] = starting * x_vals[-2][0]
   s2 = weights[-1][0] * starting * x_vals[-2][0] * (1-x_vals[-2][0])
   negative_grad[-2][0] = s2 * x_vals[-3][0]
   negative_grad[-2][1] = s2 * x_vals[-3][1]
   s3 = weights[-2][0] * s2 * x_vals[-3][0] * (1-x_vals[-3][0])
   negative_grad[-3][0] = s3 * x_vals[-4][0]
   negative_grad[-3][1] = s3 * x_vals[-4][1]
   s4 = weights[-2][1] * s2 * x_vals[-3][1] * (1-x_vals[-3][1])
   negative_grad[-3][2] = s4 * x_vals[-4][0]
   negative_grad[-3][3] = s4 * x_vals[-4][1]
   update_weights(weights, negative_grad, learning_rate)
   return weights

def backprop4(x_vals, expected, negative_grad, weights, learning_rate):
   # starting = expected[0] - x_vals[-1][0]
   # negative_grad[-1][0] = starting * x_vals[-2][0]
   # s2 = weights[-1][0] * starting * x_vals[-2][0] * (1-x_vals[-2][0])
   # negative_grad[-2][0] = s2 * x_vals[-3][0]
   # negative_grad[-2][1] = s2 * x_vals[-3][1]
   # s3 = weights[-2][0] * s2 * x_vals[-3][0] * (1-x_vals[-3][0])
   # negative_grad[-3][0] = s3 * x_vals[-4][0]
   # negative_grad[-3][1] = s3 * x_vals[-4][1]
   # negative_grad[-3][2] = s3 * x_vals[-4][2]
   # negative_grad[-3][3] = s3 * x_vals[-4][3]
   # s4 = weights[-2][1] * s2 * x_vals[-3][1] * (1-x_vals[-3][1])
   # negative_grad[-3][4] = s4 * x_vals[-4][0]
   # negative_grad[-3][5] = s4 * x_vals[-4][1]
   # negative_grad[-3][6] = s4 * x_vals[-4][2]
   # negative_grad[-3][7] = s4 * x_vals[-4][3]
   # update_weights(weights, negative_grad, learning_rate)
   # return weights
    ev = [[*i] for i in x_vals]
    starting = expected[0] - x_vals[-1][0]
    ev[-1][0] = starting
    # i is each layer in the xvals
    negative_grad[-1][0] = negative_grad[-1][0] = starting * x_vals[-2][0]

    for i in range(2,len(negative_grad)+1):
        for j in range(len(x_vals[-i])):
            temp  = weights[-(i-1)][j] * ev[-(i-1)][j] * x_vals[-i][j] * (1 - x_vals[-i][j])
            ev[-i][j] = temp
            for k in range(len(x_vals[-(i+1)])):
                negative_grad[-i][k] = temp * x_vals[-(i+1)][k]
    update_weights(weights, negative_grad, learning_rate)
    return weights

def backprop42(x_vals, expected, negative_grad, weights, learning_rate):
   starting  = expected[0] - x_vals[-1][0]
   starting2 = expected[1] - x_vals[-1][1]
   negative_grad[-1][0] = starting * x_vals[-2][0]
   negative_grad[-1][1] = starting2 * x_vals[-2][1]
   s21 = weights[-1][0] * starting * x_vals[-2][0] * (1-x_vals[-2][0])
   s22 = weights[-1][1] * starting2 * x_vals[-2][1] * (1-x_vals[-2][1])
   negative_grad[-2][0] = s21 * x_vals[-3][0]
   negative_grad[-2][1] = s21 * x_vals[-3][1]
   negative_grad[-2][2] = s21 * x_vals[-3][2]
   negative_grad[-2][3] = s22 * x_vals[-3][0]
   negative_grad[-2][4] = s22 * x_vals[-3][1]
   negative_grad[-2][5] = s22 * x_vals[-3][2]
   s31 = (weights[-2][0] * s21 + weights[-2][3] *s22) * x_vals[-3][0] * (1-x_vals[-3][0])
   s32 = (weights[-2][1] * s21 + weights[-2][4] *s22) * x_vals[-3][1] * (1-x_vals[-3][1])
   s33 = (weights[-2][2] * s21 + weights[-2][5] *s22) * x_vals[-3][2] * (1-x_vals[-3][2])
   negative_grad[-3][0] = s31 * x_vals[-4][0]
   negative_grad[-3][1] = s31 * x_vals[-4][1]
   negative_grad[-3][2] = s31 * x_vals[-4][2]
   negative_grad[-3][3] = s31 * x_vals[-4][3]
   negative_grad[-3][4] = s32 * x_vals[-4][0]
   negative_grad[-3][5] = s32 * x_vals[-4][1]
   negative_grad[-3][6] = s32 * x_vals[-4][2]
   negative_grad[-3][7] = s32 * x_vals[-4][3]
   negative_grad[-3][8] = s33 * x_vals[-4][0]
   negative_grad[-3][9] = s33 * x_vals[-4][1]
   negative_grad[-3][10] = s33 * x_vals[-4][2]
   negative_grad[-3][11] = s33 * x_vals[-4][3]
   update_weights(weights, negative_grad, learning_rate)
   return weights



def update_weights(weights, negative_grad, learning_rate):
   for i in range(len(weights)):
      for j in range(len(weights[i])):
         weights[i][j] = weights[i][j] + learning_rate * negative_grad[i][j]


#####################################################

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
   # print(training_set)
   # print(expected_set)
   layer_count = [len(training_set[0]),2,len(expected_set[0]),len(expected_set[0])] # set the number of layers
   if len(expected_set[0]) == 1:
      layer_count[1] = 2
   else:
      layer_count[1] = 3
   # print(layer_count)

   #build NN: x nodes and weights
   x_vals = [[temp[0:len(temp)-1]] for temp in training_set] # x_vals starts with first input values
   # print(x_vals)
   for i in range(len(training_set)):
      for j in range(len(layer_count)):
         if j == 0: x_vals[i][j].append(1.0)
         else: x_vals[i].append([0 for temp in range(layer_count[j])])
   # print(x_vals)
   # generate weights
   print("weights:", end = " ")
   weights = [[round(random.uniform(-2.0, 2.0), 2) for j in range(layer_count[i]*layer_count[i+1])]  for i in range(len(layer_count)-1)]
   
   if len(expected_set[0]) == 2:
      weights[-1] = [round(random.uniform(-2.0, 2.0), 2), round(random.uniform(-2.0, 2.0), 2)]
   
   print(weights)
   # build the structure of BP NN: E nodes and negative_gradients 
   E_vals = [[*i] for i in x_vals]  #copy elements from x_vals, E_vals has the same structures with x_vals
   negative_grad = [[*i] for i in weights]  #copy elements from weights, negative gradients has the same structures with weights
   errors = [10]*len(training_set)  # Whenever FF is done once, error will be updated. Start with 10 (a big num)
   count = 1  # count how many times you trained the network, this can be used for index calc or for decision making of 'restart'
   alpha = 0.01
   # print("negative gradient:", end = " ")
   # print(negative_grad)
   res = []
   for k in range(len(training_set)):
      ffres = forward_feed(training_set[k], weights, 'T3',x_vals, k)
      res.append(ffres)
      for i in range(len(ffres)):
         err = math.pow((expected_set[k][i] - ffres[i]),2)/2
         errors[k] = err



   # print("Forward Feed errors:", end = " ")
   # print(errors)
   print("Layer count:", end = " ")
   print(layer_count)
   # while sum(errors) > 2:
   #    weights = [[round(random.uniform(-2.0, 2.0), 2) for j in range(layer_count[i]*layer_count[i+1])]  for i in range(len(layer_count)-1)]
   #    res = []
   #    for k in range(len(training_set)):
   #       ffres = forward_feed(training_set[k], weights, 'T3',x_vals, k)
   #       res.append(ffres)
   #       for i in range(len(ffres)):
   #          err = math.pow((expected_set[k][i] - ffres[i]),2)/2
   #          errors[k] = err
   
   if sum(errors) <= 0.01:
         for we in weights:
            for w in we:
               print(w, end = " ")
            print()
         return

   if len(training_set[0]) == 2:
      bestw = weights
      beste = sum(errors)
      while True:
         for k in range(len(training_set)):
            ffres = forward_feed(training_set[k], weights, 'T3',x_vals, k)
            current_x_vals = x_vals[k]
            weights = backprop2(current_x_vals, expected_set[k], negative_grad, weights, alpha)
            # print(weights)
         res = []
         for k in range(len(training_set)):
            ffres = forward_feed(training_set[k], weights, 'T3',x_vals, k)
            res.append(ffres)
            for i in range(len(ffres)):
               err = math.pow((expected_set[k][i] - ffres[i]),2)/2
               errors[k] = err
         # print("Error: ", end = str(sum(errors)))
         # print()
         e = sum(errors)
         result = ""
         if e < beste:
            bestw = weights
            beste = e
         else:
            weights = bestw
         for we in bestw:
                     for w in we:
                        result += str(w) + " "
                     result += "\n"
         print(result)
         if beste <= 0.01:
            return
   elif len(expected_set[0]) == 2:
      bestw = weights
      beste = sum(errors)
      alpha = 0.5
      while True:
         for k in range(len(training_set)):
            ffres = forward_feed(training_set[k], weights, 'T3',x_vals, k)
            current_x_vals = x_vals[k]
            weights = backprop42(current_x_vals, expected_set[k], negative_grad, weights, alpha)
            # print(weights)
         res = []
         for k in range(len(training_set)):
            ffres = forward_feed(training_set[k], weights, 'T3',x_vals, k)
            res.append(ffres)
            for i in range(len(ffres)):
               err = math.pow((expected_set[k][i] - ffres[i]),2)/2
               errors[k] = err
         # print("Error: ", end = str(sum(errors)))
         # print()
         e = sum(errors)
         result = ""
         if e < beste:
            bestw = weights
            beste = e
         # elif count > 200000:
         #    count = 0
         #    weights = [[round(random.uniform(-2.0, 2.0), 2) for j in range(layer_count[i]*layer_count[i+1])]  for i in range(len(layer_count)-1)]
         for we in bestw:
                     for w in we:
                        result += str(w) + " "
                     result += "\n"
         print(result)
         count += 1
         if beste <= 0.01:
            return
   elif len(training_set[0]) == 4:
      bestw = weights
      beste = sum(errors)
      while True:
         for k in range(len(training_set)):
            ffres = forward_feed(training_set[k], weights, 'T3',x_vals, k)
            current_x_vals = x_vals[k]
            weights = backprop4(current_x_vals, expected_set[k], negative_grad, weights, alpha)
            # print(weights)
         res = []
         for k in range(len(training_set)):
            ffres = forward_feed(training_set[k], weights, 'T3',x_vals, k)
            res.append(ffres)
            for i in range(len(ffres)):
               err = math.pow((expected_set[k][i] - ffres[i]),2)/2
               errors[k] = err
         # print("Error: ", end = str(sum(errors)))
         # print()
         e = sum(errors)
         result = ""
         if e < beste:
            bestw = weights
            beste = e
         else:
            weights = bestw
         for we in bestw:
                     for w in we:
                        result += str(w) + " "
                     result += "\n"
         print(result)
         if beste <= 0.01:
            return
   else:
      bestw = weights
      beste = sum(errors)
      while True:
         for k in range(len(training_set)):
            ffres = forward_feed(training_set[k], weights, 'T3',x_vals, k)
            current_x_vals = x_vals[k]
            weights = backpropigation(current_x_vals, expected_set[k], negative_grad, weights, alpha)
            # print(weights)
         res = []
         for k in range(len(training_set)):
            ffres = forward_feed(training_set[k], weights, 'T3',x_vals, k)
            res.append(ffres)
            for i in range(len(ffres)):
               err = math.pow((expected_set[k][i] - ffres[i]),2)/2
               errors[k] = err
         # print("Error: ", end = str(sum(errors)))
         # print()
         e = sum(errors)
         result = ""
         if e < beste:
            bestw = weights
            beste = e
         # elif count > 200000:
         #    count = 0
         #    weights = [[round(random.uniform(-2.0, 2.0), 2) for j in range(layer_count[i]*layer_count[i+1])]  for i in range(len(layer_count)-1)]
         for we in bestw:
                     for w in we:
                        result += str(w) + " "
                     result += "\n"
         print(result)
         count += 1
         if beste <= 0.01:
            return
   
#####################################################
   




main()
#Satvik Matta, 5, 2023
