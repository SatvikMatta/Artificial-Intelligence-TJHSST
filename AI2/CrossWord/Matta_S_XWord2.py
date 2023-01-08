import sys; args = sys.argv[1:]
import re
import random


height = 0
width = 0

BLOCKCHAR = "#"
OPENCHAR = "-"
PROTECTEDCHAR = "~"
NUMBLOCKS = 0
NUMBLOCKS2 = NUMBLOCKS

def readIn():
    global NUMBLOCKS2
    sorted = [] 
    # import sys;args = sys.argv[1:] # read in arguments from cmd
    # args = ["7x7", "0","V0x0come", "v0x1here", "h0x2ERS"]
    # args = ["6x5", "0", "V0x0Pollen", "V0x4Ballad"]
    # args = ["9x9", "12", "V0x1Idc"]
    # args = ["3x3", "9"]
    # args = ["9x11","16", "V0x1Ate", "V0x3#"]
    args = ["9x9", "12", "V0x1Fpo"]
    # Find board size
    pattern = "^\d+x\d+$"
    for arg in args:
        if re.search(pattern, arg) != None:
            sorted.append(arg.lower())
            args.remove(arg)
            break
    #Find dictionary file
    for arg in args:
        if '.txt' in args:
            sorted.append(arg)
            args.remove(arg)
            break
    #Find number of blocks
    pattern = "^\d+$"
    for arg in args:
        if re.search(pattern, arg) != None:
            sorted.append(arg)
            global NUMBLOCKS
            NUMBLOCKS = int(arg)
            NUMBLOCKS2 = NUMBLOCKS
            args.remove(arg)
            break
    #args should only contain prefilled words, add to end of sorted list
    for arg in args:
        sorted.append(arg.lower())
    return sorted # return sorted list of arguments

def vWord(board, word):
    # Find Y,X of the start of the word
    word = word[1:]
    pattern = "^\d+x\d+"
    start = re.search(pattern, word).group() # Find Part of the word with the cords
    #Split into Y,X portions
    xIndex = start.find("x") # location of character 'x'
    yVal = int(start[:xIndex])
    xVal = int(start[xIndex+1:])

    word = word[len(start):].upper() #Actual Word (Make Uppercase)
    startIndex = (yVal * width) + xVal #Corresponding Index in board

    #Input Word into board
    board = list(board) # make board a list
    for i in range(len(word)):
        board[startIndex + (i*width)] = word[i]
    board = "".join(board) # make board back into a string
    return board

def hWord(board, word):
    # Find Y,X of the start of the word
    word = word[1:]
    pattern = "^\d+x\d+"
    start = re.search(pattern, word).group() # Find Part of the word with the cords
    #Split into Y,X portions
    xIndex = start.find("x") # location of character 'x'
    yVal = int(start[:xIndex])
    xVal = int(start[xIndex+1:])

    word = word[len(start):].upper() #Actual Word (Make Uppercase)
    startIndex = (yVal * width) + xVal #Corresponding Index in board
    
    #Input Word into board
    board = list(board) # make board a list
    for i in range(len(word)):
        board[startIndex+i] = word[i]
    board = "".join(board) # make board back into a string
    return board

def fillGivenWords(board, words):
    global NUMBLOCKS
    for word in words:
        if word[0] == "h": # if horizontal word
            board = hWord(board, word)
        elif word[0] == "v": # if vertical word
            board = vWord(board, word)
    # NUMBLOCKS -= board.count("#")
    return board

def addBorder(board):
    boardw = BLOCKCHAR*(width+3)
    boardw += (BLOCKCHAR*2).join([board[p:p+width] for p in range(0,len(board), width)])
    boardw += BLOCKCHAR*(width+3)
    return boardw

def make_board(size):
    xIndex = size.find("x") #Find Index of 'x' char
    global height
    height = int(size[:xIndex]) #Get Height
    global width
    width = int(size[xIndex+1:]) #Get Width

    board = "-" * (height*width) # Make Empty Board
    
    return board # return board

#Displays board in right format
def display(board):
    c = 0
    for i in range(height):
        for j in range(width):
            print(board[c], end = ' ')
            c+=1
        print()
    return

def transpose(board, newHeight):
     return "".join([board[col::newHeight] for col in range(newHeight)])

#Pallindrome
def pushP(board):
    global NUMBLOCKS
    pattern = "\w"
    board = re.sub(pattern, "~", board)
    board = list(board)

    for i in range(len(board)):
        if board[i] != "-":
            board[-(i+1)] = board[i]
        else:
            continue

    NUMBLOCKS -= "".join(board).count(BLOCKCHAR)
    return "".join(board)

def isLegal(board):
    bboard = addBorder(board)
    pattern = "#~~?#"
    if re.search(pattern, bboard) != None:
       return False
    # print(bboard)
    if "#-~#" in bboard or "#~-#" in bboard:
        return False
    bboard = transpose(board, height)
    # print(board)
    bboard = addBorder(bboard)
    # print()
    # print(bboard)
    if re.search(pattern, bboard) != None:
       return False
    if "#-~#" in bboard or "#~-#" in bboard:
        return False
    return True

def isLegalPos(board, pos):
    board = list(board)
    board[pos] = BLOCKCHAR
    board[-(pos+1)] = BLOCKCHAR
    board = "".join(board)
    bboard = addBorder(board)
    pattern = "#~~?#"
    if re.search(pattern, bboard) != None:
       return False
    # print(bboard)
    if "#-~#" in bboard or "#~-#" in bboard:
        return False
    bboard = transpose(board, height)
    # print(board)
    bboard = addBorder(bboard)
    # print()
    # print(bboard)
    if re.search(pattern, bboard) != None:
       return False
    if "#-~#" in bboard or "#~-#" in bboard:
        return False
    return True


def fillRequired(board):
    bboard = addBorder(board)
    for i in range(2):
        bboard = re.sub("#--#","####", bboard)
        bboard = re.sub("#-#","###", bboard)
        bboard = re.sub("[#](-~-|--~|~--|~~-|-~~|~-~)(?=[#])","#~~~#", bboard)
    board = ""
    for i in range(1,height+1):
            board += bboard[i*(width+2)+1:i*(width+2)+width+1]
    # display(board)
    bboard = transpose(board, width)
    bboard = addBorder(bboard)
    for i in range(2):
        bboard = re.sub("#--#","####", bboard)
        bboard = re.sub("#-#","###", bboard)
        bboard = re.sub("[#](-~-|--~|~--|~~-|-~~|~-~)(?=[#])","#~~~#", bboard)
    board = ""
    for i in range(1,height+1):
            board += bboard[i*(width+2)+1:i*(width+2)+width+1]
    board = transpose(board, height)
    global NUMBLOCKS
    NUMBLOCKS = NUMBLOCKS2 - board.count(BLOCKCHAR)
    return board


def addBlocks(board):
    global NUMBLOCKS
    if NUMBLOCKS == 0:
        return board

    if board.count(OPENCHAR) == NUMBLOCKS:
        return BLOCKCHAR * len(board)
    
    if NUMBLOCKS % 2 == 1:
        if width * height % 2 == 1:
            board = board[:len(board)//2] + BLOCKCHAR + board[(len(board)//2)+1:]
            NUMBLOCKS -= 1
        else:
            print("This is not possible")
            return board
    elif NUMBLOCKS % 2 == 0 and width * height % 2 == 1:
        board = board[:len(board)//2] + PROTECTEDCHAR + board[(len(board)//2)+1:]
    
    board = fillRequired(board)

    # display(board)
    # print()
    posList = []
    for i in range(len(board)//2):
        if board[i] == board[-(i+1)] == OPENCHAR:
            posList.append(i)
    
    recursiveAddBlocks(board, posList, NUMBLOCKS)

    return board


def recursiveAddBlocks(board,posList, blocks):
    global BLOCKCHAR
    if blocks == 0 or len(posList) == 0:
        return board
    
    for pos in posList:
        if isLegalPos(board, pos):
            print(pos)
            cboard = board[:pos] + BLOCKCHAR + board[pos+1:]
            cboard = cboard[:(len(cboard)-1)-pos] + BLOCKCHAR + cboard[len(cboard)-pos:]
            uPosList = [i for i in posList if i != pos]
            res = recursiveAddBlocks(cboard, uPosList, blocks-2)
            if res != "Fail":
                return res

    return "Fail"

def main():
    global height
    global width

    sortedArgs = readIn()
    # print(sortedArgs)

    board = make_board(sortedArgs[0])
    if NUMBLOCKS == height*width:
        board = BLOCKCHAR*height*width
        display(board)
        return

    board = fillGivenWords(board, sortedArgs[2:])
    board = pushP(board)
    # display(board)
    if NUMBLOCKS > 0:
        board = addBlocks(board)
        board = fillGivenWords(board, sortedArgs[2:])
        board = board.replace("~","-")
        display(board)
        return
    else:
        board = fillGivenWords(board, sortedArgs[2:])
        board = board.replace("~","-")
        display(board)
        return
    display(board)
    

main()
# Satvik Matta, 5, 2023