import sys; args = sys.argv[1:]
import re


height = 0
width = 0

BLOCKCHAR = "#"
OPENCHAR = "-"
PROTECTEDCHAR = "~"
NUMBLOCKS = 0
NUMBLOCKS2 = NUMBLOCKS
FILE = ""
#Remember to Comment out test cases#
def readIn():
    global NUMBLOCKS2
    sorted = [] 
    # import sys;args = sys.argv[1:] # read in arguments from cmd
    # args = ["7x7", "0","V0x0come", "v0x1here", "h0x2ERS"]
    # args = ["6x7", "2", "V0x0Pollen", "V0x4Ballad"]
    args = ["9x9", "12", "V0x1I"]
    # args = ["3x3", "9"]
    # args = ["9x11","34", "V0x1Ate",]
    # args = ["9x11", "13", "V0x1Fpo"]
    # args = "someDct.txt 14x16 102 v3x2 V2x4 h4x5 h7x5 H9x7 H9x5".split(" ")
    # args = "15x15 39 H0x0Mute V0x0mule V10x13Didnt H7x5# V3x4# H6x7# V11x3#".split()
    # args = "13x13 27 H6x4no#on v5x5ton v0x0ankles h0x4Trot H0x9arch V0x12heel".split()
    # args = ['myDct.txt', '7x7', '11']
    # args = ['15x15', '37', 'H0x4#', 'v4x0#', 'h8x8a']
    # Find board size
    pattern = "^\d+x\d+$"
    hi = 1
    for i in range(hi):
        for arg in args:
            if re.search(pattern, arg) != None:
                sorted.append(arg.lower())
                args.remove(arg)
                break
        #Find dictionary file
        for arg in args:
            if '.txt' in arg:
                global FILE
                args.remove(arg)
                FILE = arg
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

def pArgs(sortedArgs):
    t = sortedArgs[0]
    height = t[:t.index('x')]
    width = t[t.index('x')+1:]
    height = int(height)
    width = int(width)
    block_count = int(sortedArgs[1])
    words = []
    wordu = sortedArgs[2:]
    for word in wordu:
        dirt = word[0].upper() #Actually directions but AI Grader is Pain and uses my shortend things
        if ".txt" in word:
            continue
        tword = word[1:]
        pattern = "^\d+x\d+"
        start = re.search(pattern, tword).group() # Find Part of the word with the cords
        #Split into Y,X portions
        xIndex = start.find("x") # location of character 'x'
        row = int(start[:xIndex])
        col = int(start[xIndex+1:])
        tword = tword[len(start):].upper() #Actual Word (Make Uppercase)
        words.append((dirt, row, col, tword)) #Format in correct way in list/tuple
    return width, height, block_count, words

def makeBoard(width, height, block_count, words):
    board = OPENCHAR * width * height # make initial board
    for word in words: # Put words in either as blocks or protected depending on character
        ind  = width * word[1] + word[2]
        for l in word[3]:
            if l == BLOCKCHAR:
                ch = BLOCKCHAR
            else:
                ch = PROTECTEDCHAR
            board = board[:ind] + ch + board[ind+1:]
            board = board[:(len(board) - 1) - ind] + ch + board[len(board) - ind:]
            if word[0] == 'H':
                ind += 1
            else:
                ind += width
            
    # block_count -= board.count(BLOCKCHAR)
    display(board, width, height)
    print()
    board = addBorder(board, width)
    height += 2
    width += 2
    board = pushP(board, width, height) #pushP Protect at all costs

    return board, width, height, block_count

def addBorder(board, width): # Ms.Kim given addBorder Method
    xw = BLOCKCHAR*(width+3)
    xw +=(BLOCKCHAR*2).join([board[p:p+width] for p in range(0,len(board),width)])
    xw += BLOCKCHAR*(width+3)
    return xw


def pushP(board, width, height):
    rl = "(#(\w|~)(\w|~))-" #right
    ll = "-((\w|~)(\w|~)#)" #left
    for i in range(2):
        board = re.sub(ll, r"~\1", board) #REGEX!!!!! ***WORKS*** Whoo hooo!!!!
        board = re.sub(rl, r"\1~", board)
        display(board, width, height)
        board = transpose(board, width) # Fixed transpose method, pass in the width
        # update width and height
        t = width 
        width = height
        height = t
        print()
        display(board, width, height)
    return board

def transpose(board, width):
    return ''.join([board[col::width] for col in range(width)]) # Fixed Transpose method changed from height to width
                                                                # Same as originial transpose method given by Ms.Kim


def display(board, width, height): #Displays the board with spaces between each character
                                   #Done Line by line
    for i in range(height):
        ln = "" #ln == line not natural log lol maths
        for l in range(width):
            ln += (board[(i*width)+l]+" ")
        print(ln)


def addBlocks(board, width, height, block_count):
    if board.count("-") == block_count: # check if just need to fill all
        return len(board) * "#"
    
    elif block_count == 0: # check if need to fill no more
        return board
    
    elif block_count %2 == 1:
        if height % 2 == 1 and width % 2 == 1:
            board = board[: len(board) // 2] + BLOCKCHAR + board[(len(board) // 2) + 1 :]
            #  block_count -= 1
        else:
            print("Whoopsie Daisy") # Not possible to have this condition, something def went wrong if you get to here
    
    #More complicated version of what Ms.Kim had on the board ****If not work try using Kim's board code and find how to use re.compile****
    if re.search("#[~-]{1,2}#", board) or re.search("#[~-]{1,2}#", transpose(board, width)):

        for i in range(2):
            # ps = board.count("#")
            board = re.sub("#([~-]#)*", lambda x: BLOCKCHAR * len(x.group()), board)
            board = re.sub("#([~-][~-]#)*", lambda x: len(x.group())* BLOCKCHAR, board) # lambda function is essentially lets me use re.compile() without having to say re.compile
            
            #block_count = board.count("#") - ps
            board = transpose(board,width)
            width, height = height, width
        block_count = block_count - (board.count("#") - ((2*height) + (2*(width-2))))
        posList = findPosList1(board)
        # display(board, width, height)
        f = {} #Area filling stuff
        for i in posList:
            f[i] = afill(board, width, i)
        fc = {}
        for z in f.keys():
            c = f[z].count("+")
            if c not in fc.values():
                fc[z] = c
        
        fc = {key: value for key, value in sorted(fc.items(), key=lambda item: item[1])} # Reorder dictionary // Get better dude
        for c in fc:
            if fc[c] < (width-2) * (height-2) - (board.count("~") + board.count("-")):
                board = afill(board, width, len(board)-1-c, ch="#")
                board = afill(board, width, c, ch="#")
                block_count -= (2* fc[c])
                break
    posList = findPosList(board)
    # display(board, width, height)
    return recursiveBlocks(board, width, height, block_count, posList) #recursive backtracking instead of while loop ***Works***

def findPosList(board):
    posList = []
    for i in range(len(board)): #PosList finding
        if board[i] == board[(len(board)-1)-i]:
            if board[i] == "-":
                posList.append(i)
    return posList

def findPosList1(board):
    posList = [] #Possible positions to place a block
    for i in range(len(board)):
            if board[i] != BLOCKCHAR and board[i] != PROTECTEDCHAR:
                posList.append(i)
    return posList

def recursiveBlocks(board, width, height, block_count, posList):
    if block_count == 0:
        return board #Base Case 1
    elif len(posList) == 0: #Base Case 2
        return board
    
    for pos in posList:
        if isLegal(board, width, pos):
            cboard = board[:pos] + "#" + board[pos+1:] # insert at pos
            cboard = cboard[:(len(cboard)-(pos+1))] + "#" + cboard[len(cboard)-pos:] #Pallindrom PushinP
            # display(board, width, height)
            # print()
            uposList = [] # Update list
            for i in posList:
                if i != pos:
                    uposList.append(i)
            rboard = recursiveBlocks(cboard, width, height, block_count-2, uposList) # Call method again
            if rboard != "Fail": # bad job me, why does this always happen ***Problem Fixed***
                return rboard
            
    return "Fail"


def isLegal(board, width, pos): #Checks legality of a position
    if board[pos] != "-":
        return False
    tboard = board[:pos] + "#" + board[pos+1:]
    tboard = tboard[:len(tboard)-(pos+1)] + "#" + tboard[len(tboard)-pos:]

    illegalRegex = "[#](.?(~|-)|(~|-).?)[#]"
    if re.search(illegalRegex, tboard) != None:
        return False
    # if isConnected(tboard, width, height) == False:
    #     return False
    tboard = transpose(tboard, width)
    if re.search(illegalRegex, tboard) != None:
        return False
    
    return True

def isConnected(board, width, height):
    total = board.count(OPENCHAR) + board.count(PROTECTEDCHAR)
    pos  = min(board.find(PROTECTEDCHAR), board.find(OPENCHAR))
    print(board.find(PROTECTEDCHAR))
    print(board.find(OPENCHAR))
    found = checkConnectedHelper(board, width, height, pos)
    return total == found

def checkConnectedHelper(board, width, height, pos):
    if board[pos] == BLOCKCHAR:
        return 0
    else:
        count = 0

        temp  = checkConnectedHelper(board, width, height, pos + width)
        count += temp

        temp  = checkConnectedHelper(board, width, height, pos + 1)
        count += temp

        temp  = checkConnectedHelper(board, width, height, pos - 1)
        count += temp

        temp  = checkConnectedHelper(board, width, height, pos - width)
        count += temp

        return 1+count




def afill(board, width, p, ch='+'): #Premature fill method to get possible fillings
    dirs = [width, -1, 1, -1*width]
    if p < 0 or p > len(board):
        return board
    if board[p] in ["-", "~"]:
        board = board[:p] + ch + board[p+1:]
        for d in dirs:
            if (d == -1 and p% width == 0) or (d == 1 and (p+1) % width == 0):
                continue
            board = afill(board, width, p+d,ch)
    return board

def furnish(board, width, height, words): #Move in everything and furnish the board with all the letters
                                          #Remove the wrappings on the board
    board, width, height = remove_border(board, width, height) #Remove block border
    for word in words:
        ind = word[1] * width + word[2]
        for l in word[3]:
            board = board[:ind] + l + board[ind+1:]
            if word[0] == "V":
                ind += width
            else:
                ind += 1
    board = board.replace("~", "-")
    return board, width, height

def remove_border(board, width, height): #Remove border ***Works***
    new_board = ""
    for i in range(len(board)):
        if ((i+1)%width!= 0) and (i%width!=0) and (width <= i < (width * (height-1))):
                new_board += board[i]
    return new_board, width-2, height-2

def main():
    sortedArgs = readIn() #***Wordle 3/16/2022 is CATER***
    width, height, block_count, words = pArgs(sortedArgs)
    board, width, height, block_count = makeBoard(width, height, block_count, words)
    board = addBlocks(board, width, height, block_count)
    if board == "Fail":
        print("Failure!!!!") #Reminds me of this lab before I fixed it
        return
    if height*width != block_count:
        board, width, height = furnish(board, width, height, words)
    display(board, width, height)

main() #Last Line of Code, screw AI Grader, AI Grader give Pain, Pain is AI Grader
# Satvik Matta, P5, 2023