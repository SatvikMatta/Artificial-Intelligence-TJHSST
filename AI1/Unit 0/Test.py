def make_bricks(small, big, goal):
  return goal - min(int(goal/5), big)*5 <= small
  
print(make_bricks(1,3,8))