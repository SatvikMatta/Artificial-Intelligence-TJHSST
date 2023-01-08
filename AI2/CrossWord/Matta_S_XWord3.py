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
    # args = ["6x7", "2", "V0x0Pollen", "V0x4Ballad"]
    # args = ["9x9", "12", "V0x1Idc"]
    # args = ["3x3", "9"]
    args = ["9x11","16", "V0x1Ate",]
    # args = ["9x11", "13", "V0x1Fpo"]
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

    # NUMBLOCKS -= "".join(board).count(BLOCKCHAR)
    return "".join(board)


def fillRequired(board):
    global height
    global width
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
    return board


def addBlocks(board):
    global NUMBLOCKS
    global NUMBLOCKS2
    if NUMBLOCKS == 0:
        return board
    
    if NUMBLOCKS2 == height*width:
        return BLOCKCHAR * len(board)
    
    if height %2 == 1 and width%2 == 1:
        if NUMBLOCKS % 2 == 1:
            board = board[:len(board)//2] + BLOCKCHAR + board[(len(board)//2)+1:]
        else:
            board = board[:len(board)//2] + PROTECTEDCHAR + board[(len(board)//2)+1:]

    board = fillRequired(board)

    # display(board)
    # print()

    posList = []
    for i in range(len(board)//2):
        if board[i] == board[-(i+1)] == OPENCHAR:
            posList.append(i)

    NUMBLOCKS -= board.count(BLOCKCHAR)

    board = recursiveAddBlocks(board,posList, NUMBLOCKS)

    return board

def recursiveAddBlocks(board, posList, blockCount):
    if blockCount == 0:
        return board
    if len(posList) == 0:
        return BLOCKCHAR * (height*width)
    else:
        pos  = random.choice(posList)
        # pos = 17
        # posList.remove(pos)
        uPosList = [i for i in posList if i != pos]
        if isLegalPos(board,pos, blockCount-2):
            cboard = list(board)
            cboard[pos] = BLOCKCHAR
            cboard[-(pos+1)] = BLOCKCHAR
            cboard = "".join(cboard)
            blockCount -= 2
        else:
            cboard = board
        return recursiveAddBlocks(cboard, uPosList, blockCount)

def isLegalPos(board, pos, blockCount):
    global width
    global height
    board = list(board)
    board[pos] = BLOCKCHAR
    board[-(pos+1)] = BLOCKCHAR
    board = "".join(board)
    display(board)
    print()
    bboard = addBorder(board)
    pattern = "#~~?#"
    if re.search(pattern, bboard) != None:
       return False
    # print(bboard)
    if "#-~#" in bboard or "#~-#" in bboard:
        return False
    if bboard.count("#--#") > blockCount:
        return False
    if bboard.count("#-#") > blockCount:
        return False
    bboard = transpose(board, width)
    t = height
    height = width
    width = t
    # print(board)
    bboard = addBorder(bboard)
    t = height
    height = width
    width = t
    # print()
    # print(bboard)
    if re.search(pattern, bboard) != None:
       return False
    if "#-~#" in bboard or "#~-#" in bboard:
        return False
    if bboard.count("#--#")*2 > blockCount:
        return False
    if bboard.count("#-#") > blockCount:
        return False
    return True

def main():
    sortedArgs = readIn()
    # print(sortedArgs)
    board = make_board(sortedArgs[0])
    # display(board)
    print()
    board = fillGivenWords(board,sortedArgs[2:])
    board = pushP(board)
    display(board)
    print()
    if NUMBLOCKS > 0:
        board = addBlocks(board)
        board = fillGivenWords(board,sortedArgs[2:])
        board = board.replace("~","-")
        display(board)
    else:
        board = fillGivenWords(board,sortedArgs[2:])
        board = board.replace("~","-")
        display(board)

main()
# Satvik Matta, 5, 2023
