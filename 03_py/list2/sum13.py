def sum13(nums):
  if len(nums) == 0:
      return 0
  count = 0
  skip_next = False 
  
  for i in range(len(nums)):
    if skip_next:
      skip_next = False  
      continue
    
    if nums[i] == 13:
        skip_next = True  
    else:
        count += nums[i]  

  return count