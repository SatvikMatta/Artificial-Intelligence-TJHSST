import sys; args = sys.argv[1:]
import re
import random


height = 0
width = 0

BLOCKCHAR = "#"
OPENCHAR = "-"
PROTECTEDCHAR = "~"
NUMBLOCKS = 0

def readIn():
    sorted = [] 
    # import sys;args = sys.argv[1:] # read in arguments from cmd
    # args = ["Test.txt", "7x7", "2","V0x0come", "v0x1here", "h0x2ERS"]
    # args = ["6x5", "0", "V0x0Pollen", "V0x4Ballad"]
    # args = ["9x9", "12", "V0x1Idc"]
    # args = ["3x3", "9"]
    # args = ["9x11","16", "V0x1Ate", "V0x3#"]
    args = ["7x9", "10", "v0x1Fpo"]
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

#Makes board same after roating 180 degrees
def makePalindrome(board):
    global NUMBLOCKS
    board = list(board) # board into list
    #Make protected char for all blocks filled with words
    for i in range(len(board)):
        if board[i] != "#" and board[i] != "-":
            board[i]  = "~"
    board = "".join(board) # make board back into a string

    nboard = "" #New board
    board = list(board)

    #Rotate board
    for i in range(len(board)):
           board[-(i+1)] = board[i]

    #for i in range(len(board)//2):
    #    if board[i] == "#":
    #        board[-(i+1)] = "#"
    #    if board[i] == "~":
    #        board[-(i+1)] = "~"
    
    if width%2 == 1 and height%2 == 1:
        if NUMBLOCKS%2 == 0:
            board[len(board)//2] = "~"
        else:
            if NUMBLOCKS > 0:
                board[len(board)//2] = "#"
            else:
                board[len(board)//2] = "~"
    board = "".join(board) # make board back into a string
    
    
    return board

#Check if board is a valid board
#does not check for number of blocks
def isLegal(board):
    bboard = addBorder(board)
    pattern = "#~~?#"
    if re.search(pattern, bboard) != None:
       return False
    # print(bboard)
    bboard = transpose(board, height)
    # print(board)
    bboard = addBorder(bboard)
    # print()
    # print(bboard)
    if re.search(pattern, bboard) != None:
       return False
    return True
    

def transpose(board, newWidth):
     return "".join(board[col::newWidth] for col in range(height))

def addBlockHelper(board, pos):
    global NUMBLOCKS
    oboard = board
    board = list(board)
    board[pos] = BLOCKCHAR
    board[-(pos+1)] = BLOCKCHAR
    NUMBLOCKS -= 2
    board = "".join(board)
    if isLegal(board):
        pattern = "#-#"
        if addBorder(board).count(pattern) > NUMBLOCKS:
            NUMBLOCKS += 2
            return oboard
        else:
            NUMBLOCKS -= addBorder(board).count(pattern)
            bboard = addBorder(board).replace("#-#", "###")
            board = ""
            for i in range(1,height+1):
                board += bboard[i*(width+2)+1:i*(width+2)+1+width]
        pattern = "#--#"
        if addBorder(board).count(pattern)*2 > NUMBLOCKS:
            NUMBLOCKS += 2
            return oboard
        else:
            NUMBLOCKS -= addBorder(board).count(pattern)*2 
            bboard = addBorder(board).replace("#--#", "####")
            board = ""
            for i in range(1,height+1):
                board += bboard[i*(width+2)+1:i*(width+2)+1+width]
    else:
        NUMBLOCKS += 2
        return oboard
    return board

def addBlocks(board):
    alreadyBlocks = board.count(BLOCKCHAR)
    global NUMBLOCKS
    NUMBLOCKS -= alreadyBlocks
    if NUMBLOCKS <= -1:
        print("Number of valid blocks exceeded")
        return board
    else:
        validPos = set()
        for i in range(len(board)//2):
            if board[i] == '-':
                validPos.add(i)
        while NUMBLOCKS > 0 and len(validPos) > 0:
            pos  = validPos.pop()
            board  = addBlockHelper(board, pos)
        
    return board

def main():
    sortedArgs = readIn()
    # print(sortedArgs)
    board = make_board(sortedArgs[0])
    # display(board)
    board = fillGivenWords(board, sortedArgs[2:])
    boardw = addBorder(board)
    #print(boardw)
    # print()
    # display(board)
    # print()
    board = makePalindrome(board)
    # display(board)
    # print()
    display(board)
    print(isLegal(board))
    if NUMBLOCKS == height*width:
        board = "#"*height*width
        display(board)
        return
    if NUMBLOCKS > 0:
        board = addBlocks(board)
    board = fillGivenWords(board, sortedArgs[2:])
    board = board.replace("~","-")
    display(board)

main()
# Satvik Matta, 5, 2023