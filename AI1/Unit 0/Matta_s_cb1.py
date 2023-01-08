#Satvik Matta
#August 25, 2021


def sleep_in(weekday, vacation):
  return not weekday or vacation

def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile

def sum_double(a, b):
  return a+b if (a != b) else (a+b)*2

def diff21(n):
  return abs(21-n) if(n <=21) else abs(21-n)*2

def parrot_trouble(talking, hour):
  return talking and (hour<7 or hour>20)

def makes10(a, b):
  return a+b==10 or a==10 or b==10

def near_hundred(n):
  return abs(100-n) <=10 or abs(200-n) <=10

def pos_neg(a, b, negative):
  return True if((a*b <0 and not negative) or (a<0 and b<0 and negative)) else False

def hello_name(name):
  return 'Hello ' + name + '!'

def make_abba(a, b):
  return a+b+b+a

def make_tags(tag, word):
  return '<' + tag + '>' + word + '<' + '/' + tag + '>'

def make_out_word(out, word):
  return out[0:int(len(out)/2)] + word + out[int(len(out)/2) :]

def extra_end(str):
  return str[len(str)-2:] + str[len(str)-2:] + str[len(str)-2:]

def first_two(str):
  return str[0:2] if(len(str) > 2) else str

def first_half(str):
  return str[0:int(len(str)/2)]

def without_end(str):
  return str[1:len(str)-1]

def first_last6(nums):
  return nums[0] == 6 or nums[len(nums)-1] == 6

def same_first_last(nums):
  return len(nums) > 0 and nums[0]==nums[len(nums)-1]

def make_pi(i):
  return [3,1,4,1,5,9,2,6,5,3,5,8,9,7][:i]

def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]

def sum3(nums):
  return sum(nums)

def rotate_left3(nums):
  return nums[1:] + nums[0:1]

def reverse3(nums):
  return nums[::-1]

def max_end3(nums):
  return [max(nums[0],nums[-1])] * len(nums)

def cigar_party(cigars, is_weekend):
  return cigars>=40 and ((cigars<=60 and not is_weekend) or (is_weekend))

def date_fashion(you, date):
  return 0 if (you<=2 or date<=2) else 2 if(you >=8 or date>=8) else 1

def squirrel_play(temp, is_summer):
  return True if((temp>=60 and temp<=90 and not is_summer) or (temp>=60 and temp<=100 and is_summer)) else False

def caught_speeding(speed, is_birthday):
  return 0 if(speed <= 60 or (speed<=65 and is_birthday)) else 1 if((speed > 60 and speed <=80) or (speed >65 and speed <=85 and is_birthday)) else 2

def sorta_sum(a, b):
  return a+b if(not (10<=a+b<=19)) else 20

def alarm_clock(day, vacation):
  return '7:00' if (day<6 and day!=0 and not vacation) else '10:00' if((vacation and day<6 and day!=0) or (not vacation and (day== 6 or day==0))) else 'off'

def love6(a, b):
  return True if a==6 or b==6 or abs(a-b)==6 or a+b==6 else False

def in1to10(n, outside_mode):
  return True if ((outside_mode and (n<=1 or n>=10)) or (outside_mode == False and n>=1 and n<=10)) else False