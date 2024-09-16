def centered_average(nums):
  sum = 0
  for i in range(len(nums)):
    sum += nums[i]
  sum -= (min(nums) + max(nums))
  return sum / (len(nums) - 2)
