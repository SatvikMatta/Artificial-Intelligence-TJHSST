import math
"""   
    +--------- PYTHON BIT OPERATORS, FUNCTIONS, AND TRICKS ----------------+
    |  operator          meaning                  examples                 |
    |   &          and                     1010 & 1100 = 1000              |
    |   |          non-exclusive or        1010 | 1100 = 1110              |
    |   ^          exclusive or            1010 ^ 1100 = 0100              |
    |   ~          not (flip all bits)    ~1010        = ????              |
    |              flip all bits           0x1F-(0b11010) = 101            |
    |   <<         shift left  n bits      101    << 3 = 101000            |
    |   >>         shift right n bits      101000 >> 3 = 101               |
    +----------------------------------------------------------------------+
    |   0b or 0B   interpret as binary      0b10101    = 21                |
    |   bin()      express as binary        bin(21)    = 10101             |
    +----------------------------------------------------------------------+
    |  turn ON  nth bit from right: num |=  (1 << n)                       |
    |  turn OFF nth bit from right: num &= ~(1 << n)                       |
    |  flip     nth bit from right: num ^=  (1 << n)                       |
    |  test     nth bit from right: if (num & (1 << n))  > 0: ...          |
    |                               if (num & (1 << n)) == 0: ...          |
    |  clear the right-most bit:    num = num & (num-1)                    |
    |  smear right-most 1 to right: num | (num-1)                          |
    |  extract right-most 1:        num = num & -num (e.g., 101100 ->10)   |
    |  extract nth bit from left:   bit = (num >> n) & 1                   |
    |  mod 2**n:                    x mod 2**n = x &(2**n - 1)             |
    +----------------------------------------------------------------------+
    |  Below, the 0 is a zero, not a letter in 0b (= 0B).                  |
    |  print (0b10101)           # = 21                                    |
    |  print ( int("10101", 2) ) # = 21 (string to binary integer)         |
    |  print(bin(21))            # = 0b10101                               |
    |  print(bin(21)[2:])        # =   10101                               |
    |  n = 0b1001                                                          |
    |  print(n.bit_length())     # = 4                                     |
    +----------------------------------------------------------------------+
"""



# Question 1: What is the 4-bit binary representation of number?
def fourBitBinaryRep(number):
   """ Write your code here """
   return bin((0b1111 ^ int(bin(number)[-4:],2)) + 1)[2:].zfill(4)

# Question 2: # Create a binary number of max bits. Initially set every bit to 1. By the sieve method
# of Eratosthenes, set to zero any bit whose position number is not a prime number.

def sieveOfEratosthenesUsingBits(max):     # max = the number of bits
   """ Write your code here """
   seive = 2**(max) - 1
   p = int("1"*max,2)
   pList = []
   for i in range(2,int(math.sqrt(max))+1):
       for n in range(i+1,max):
           if n%i == 0:
               p&= ~(1 << max-n-1)
   for i in range(2,max):
       if (p & (1 << max-i-1)) > 0:
           print(i, end = " ")
   print()
  
  
def main():
   number = -13    
   print(fourBitBinaryRep(number))  # -13 (= -0b1101) is 0011
   sieveOfEratosthenesUsingBits(100)   # total 25 prime numbers should be printed
   
if __name__ == '__main__':  main()
