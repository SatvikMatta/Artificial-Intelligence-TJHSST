#Satvik Matta
#August 31, 2021



def string_times(str, n):
  return str*n
def front_times(s, n):
  return s[:3]*n
def string_bits(s):
  return s[::2]
def string_splosion(str):
  return ''.join([str[:i] for i in range(len(str)+1)])
def last2(str):
  return sum(1 for i in range(len(str)-2) if str[i:i+2] == str[-2:])
def array_count9(nums):
  return nums.count(9)
def array_front9(nums):
  return 9 in nums[:4]
def array123(nums):
  return (1,2,3) in zip(nums,nums[1:],nums[2:])
def string_match(a, b):
   return sum(1 for i in range(len(a)-1) if a[i:i+2] == b[i:i+2])
def make_bricks(small, big, goal):
  return goal - min(int(goal/5), big)*5 <= small
def lone_sum(a, b, c):
  return sum(n for n in [a,b,c] if [a,b,c].count(n) < 2)
def no_teen_sum(a, b, c):
  return sum(x for x in [a,b,c] if x not in (13,14,17,18,19))
def round_sum(a, b, c):
  return sum((x+5)//10*10 for x in [a,b,c])
def close_far(a, b, c):
  return (abs(a-b)<2 and abs(a-c)>1 and abs(b-c)>1) or (abs(a-c)<2 and abs(a-b)>1 and abs(b-c)>1)
def make_chocolate(s, b, g):
  return [-1,g - min(int(g/5), b)*5][g - min(int(g/5), b)*5 <= s]
def double_char(str):
  return "".join([str[i:i+1]*2 for i in range(len(str))])
def count_hi(str):
  return str.count('hi')
def cat_dog(str):
  return str.count('cat') == str.count('dog')
def count_code(str):
  return len([i for i in range(len(str)-3) if str[i:i+2]== 'co' and str[i+3] == 'e'])
def end_other(a, b):
  return a.lower().endswith(b.lower()) or b.lower().endswith(a.lower())
def xyz_there(str):
  return str.count('xyz') != str.count('.xyz')
def count_evens(nums):
  return len([i for i in nums if i % 2==0])
def big_diff(nums):
  return max(nums) - min(nums)
def centered_average(nums):
  return sum(sorted(nums)[1:-1])//(len(nums)-2)
def sum13(nums):
  return sum(nums[x] for x in range(len(nums)) if nums[x]!=13 and nums[max(0,x-1)]!=13)
def has22(nums):
  return (2,2) in zip(nums,nums[1:])
def lucky_sum(a, b, c):
   return [0,a,a+b,a+b+c][[a,b,c,13].index(13)]
def sum67(nums):
    return sum(nums[i] for i in range(len(nums)) if nums[i]!=6 and (6 not in nums[:i] or (7 in nums[:i] and nums[i-1::-1].index(6)>nums[i-1::-1].index(7)))) 
