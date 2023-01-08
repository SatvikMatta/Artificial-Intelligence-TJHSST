# Name: Satvik Matta
# Date: September 10,2021
# Do not forget to change the file name -> Save as
import math
import string
import PIL
from PIL import Image
''' Tasks '''
# 1. Given an input of a space-separated list of any length of integers, output the sum of them.
# 2. Output the list of those integers (from #1) that are divisible by three.
msg = input("list of numbers: ")
print("1. sum  = ", end = " ")
h = msg.strip().split()
print(sum(int(x) for x in h))
print("2. list of multiples of 3: ", end= " ")
print([int(x) for x in h if int(x) % 3 == 0])

# 3. Given an integer input, print the first n Fibonacci numbers. eg. n=6: 1, 1, 2, 3, 5, 8
def fibonacci(n):
    if n == 1 or n==0:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
msg = input("Type n for Fibonacci sequence: ")
print("3. fibonacci: ", end = " ")
for i in range(1,int(msg)+1):
    print(fibonacci(i), end = " ")
print()
# 4. Given an input, output a string composed of every other character. eg. Aardvark -> Arvr
msg = input("Type a string: ")
print("4. every other str:  " + msg[::2])
# 5. Given a positive integer input, check whether the number is prime or not.
msg = input("Type a number to check prime: ")
i = True
for k in range(1,int(msg)//2):
    if int(msg)%2 == 0:
        i = False
        print("5. Is prime? False")
if i:
    print("5. Is prime? True")
# 6. Calculate the area of a triangle given three side lengths.  eg. 13 14 15 -> 84
msg = input("Type three sides of a triangle: ")
h = [int(x) for x in msg.strip().split()]
s = sum(h)/2
print("6. The area of " + str(h[0]) + " " + str(h[1]) + " " + str(h[2]) + " is", end = " ")
print(math.sqrt(s*(s-h[0])*(s-h[1])*(s-h[2])))

# 7. Given a input of a string, remove all punctuation from the string. 
# eg. "Don't quote me," she said. -> Dontquotemeshesaid
# 8. Check whether the input string (from #7, lower cased, with punctuation removed) is a palindrome.
# 9. Count the number of each vowel in the input string (from #7).
msg = input("Type a sentence: ")
for i in msg:
    if i in string.punctuation:
        msg  = msg.replace(i,'')
msg = msg.replace(" ",'')
print("7. Punct removed: " + msg)
print("8. Is palindrome? " + str(msg.lower()==msg[::-1].lower()))
vcount = {'a': msg.count('a'),'e': msg.count('e'),'i': msg.count('i'),'o': msg.count('o'),'u': msg.count('u')}
print("9. Count each vovel: ", end = " ")
print(vcount)
 
# 10. Given two integers as input, print the value of f\left(k\right)=k^2-3k+2 for each integer between the two inputs.  
# eg. 2 5 -> 0, 2, 6, 12
msg = input("Type two integers (lower bound and upper bound): ")
h = [int(x) for x in msg.strip().split()]
print("10. Evaluate f(k)=k^2 - 3k + 2 from 2 to 5:", end = " ")
for i in range(h[0],h[1]+1):
    print(i**2 -3*i + 2,end = " ")
print()

# 11. Given an input of a string, determines a character with the most number of occurrences.
# 12. With the input string from #11, output a list of all the words that start and end in a vowel.
# 13. With the input string from #11, capitalizes the starting letter of every word of the string and print it.
# 14. With the input string from #11, prints out the string with each word in the string reversed.
# 15. With the input string from #11, treats the first word of the input as a search string to be found in the rest 
# of the string, treats the second word as a replacement for the first, and treats the rest of the input as the string to be searched.
# 	eg.    b Ba baby boy ->  BaaBay Baoy
t = {}
msg = input("Type a string: ")
for i in msg:
    if i in t.keys():
        t[i] = t[i]+1
    else:
        t[i] = 0
print("11. Most occurred char: ", end = "")
for i in t.keys():
    if t[i] == max(list(t.values())):
        print(i, end = " ")
print()
print("12. List of words starting and ending with vowels: ", end = "")
print([x for x in msg.strip().split() if x[0] in "aeiou"])
print("13. Capitalize starting letter of every word: " +msg.title())
print("14. Reverse every word: ", end = "")
print(" ".join([x[::-1] for x in msg.strip().split()]))
print("15. Find the first and replace with the second:", end = " ")
f,s = msg.strip().split()[0],msg.strip().split()[1]
y = msg.strip().split()
for i in range(2,len(msg.strip().split())):
    if y[i].startswith(f):
        print(y[i].replace(f,s), end = " ")
    else:
        print(y[i], end = " ")
print()



 
# 16. With an input of a string, removes all duplicate characters from a string.  Eg. detection -> detcion
msg = input("Type a string to remove all duplicate chars: ")
msg = msg[::-1]
for i in msg:
    if msg.count(i) > 1:
        msg = msg.replace(i,"",1)
print("16. Remove all duplicat chars: " + msg[::-1])


# 17. Given an input of a string, determines whether the string contains only digits.
# 18. If #17 prints True, determines whether the string contains only 0 and 1 characters, and if so assumes it is a binary string, 
# converts it to a number, and prints out the decimal value.
msg = input("Type a string to check if it has only digits or not: ")
k=True
b = True
for i in msg:
    if i not in string.digits:
        k = False
if k:
    print("17. Is a number?: True")
else:
    print("17. Is a number?: False")

for i in msg:
    if i not in ['0','1']:
        b = False
if k and b:
    o = int(msg,2)
    print("18. It is a binary number: " + str(o))
 
# 19. Write a script that accepts two strings as input and determines whether the two strings are anagrams of each other.
msg = input("Type the first string to check anagram: ")
msg1 = input("Type the second string to check anagram: ")
print("19. Are " + msg + " and " + msg1 + " anagram?: " + str(sorted(list(msg))==sorted(list(msg1))))


# 20. Given an input filename, if the file exists and is an image, find the dimensions of the image.
msg = input("Type the image file name: ")
f= msg
img = Image.open(f)
print("20. Image dimension: " + str(img.width) + " by " + str(img.height))

# 21. Given an input of a string, find the longest palindrome within the string.
def pal(s):
    longest = ""
    for i in range(len(s)):
        for j in reversed(range(len(s)-1)):
            if s[i:j+1] == s[i:j+1][::-1]:
                if len(s[i:j+1]) > len(longest):
                    longest = s[i:j+1]
    return longest
msg = input("Type a string to find the longest palindrome: ")
print("21. Longest palindrome within the string: ", end  = pal(msg.replace(" ","")))
print()

 
# 22. Given an input of a string, find all the permutations of a string.
# 23. Given the input string from #22, find all the unique permutations of a string.
h = []
def sw(w,i,j):
    ca = list(w)
    temp = ca[i]
    ca[i] = ca[j]
    ca[j] = temp
    return "".join(ca)

def perm(s,l,r):
    if l==r:
        h.append(s)
    else:
        for i in range(l,r+1):
            s = sw(s,l,i)
            perm(s,l+1,r)
            str = sw(s,l,i)

msg = input("Type a string to do permutation: ")
n = len(msg)
perm(msg,0,n-1)
print("22. all permutations:",end = " ")
print(h)
print("23. all unique permutations: ",end ="")
print(({*h}))

# 24. Given an input of a string, find a longest non-decreasing subsequence within the string (according to ascii value).
msg = input("Type a string to find the longest non-decreasing sub: ")
longest = ""
long = 0
curr = 1
start = 0
msg  = msg.replace(" ",'')
for i in range(len(msg)-1):
    if ord(msg[i]) <= ord(msg[i+1]):
        curr+=1
    else:
        if curr > long:
            long = curr
            curr = 1
            longest = msg[start+2:i]
            start = i
print(longest)
