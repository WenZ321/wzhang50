def reverse3(nums):
  temp = []
  for i in range(1, len(nums) + 1):
    temp.append(nums[-1 * i])
    
  return temp