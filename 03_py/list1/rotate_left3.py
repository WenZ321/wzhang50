def rotate_left3(nums):
  monke=[]
  for i in range(1,len(nums)):
    monke.append(nums[i])
  monke.append(nums[0])
  return monke
