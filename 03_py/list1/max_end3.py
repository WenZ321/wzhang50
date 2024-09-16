def max_end3(nums):
  m = max(nums[0], nums[2])
  for i in range(0, 3):
    nums[i] = m
  return nums
