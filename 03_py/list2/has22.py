def has22(nums):
  firstTwo = False
  for i in range(len(nums)):
    if(firstTwo):
      if (nums[i] == 2):
        return True
      else:
        firstTwo = False
    else:
      if(nums[i] == 2):
        firstTwo = True
  return False
        
