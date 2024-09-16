def sum67(nums):
  stopCount = False
  count = 0
  for i in range(len(nums)):
    if((stopCount)):
      if(nums[i] == 7):
        stopCount = False
      else:
        continue
    else:
      if(nums[i] == 6):
        stopCount = True
        continue
      else:
        count += nums[i]
  return count
