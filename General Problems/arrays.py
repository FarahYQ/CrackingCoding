
# Find nth smallest number in given unsorted array:
def nth_smallest(arr,n):
  if len(arr) == 0: return None
  if len(arr) == 1: return arr[0]
  left = 0
  right = len(arr)-2
  pivot = arr[len(arr)-1]
  while left <= right:
    while arr[left] <= pivot: left += 1
    while arr[right] > pivot: right -= 1

    if left < right:
      temp = arr[left]
      arr[left] = arr[right]
      arr[right] = temp
      left += 1
      right -= 1
  temp = arr[left]
  arr[left] = arr[len(arr)-1]
  arr[len(arr)-1] = temp

  if left + 1 == n:
    return arr[left]
  elif left + 1 > n:
    return nth_smallest(arr[:left],n)
  else:
    return nth_smallest(arr[left+1:],n-(left+1))

print(nth_smallest([2,6,5,0,7,8,3],0))

# Given a collection of numbers that might contain duplicates, return all permutations
# [1,1,2] --> [[1,1,2], [1,2,1], [2,1,1]]
def permuteUnique(self, nums):
  """
  :type nums: List[int]
  :rtype: List[List[int]]
  """
  if len(nums) <= 1: return [nums]
  
  prev = self.permuteUnique(nums[:len(nums)-1])
  
  last = nums[len(nums)-1]
  permutations = set()
  for perm in prev:
    perm = list(perm)
    for i in range(len(perm)+1):
      new_perm = perm[i:] + [last] + perm[:i]
      permutations.add(tuple(new_perm))
  return list(permutations)


# Kadane's algorithm
def maxSub(arr):
  lastArr = [arr[0]]
  last = arr[0]
  largest = arr[0]
  largestArr = [arr[0]]
  tracker = {}
  tracker[last] = lastArr
  for i in range(1,len(arr)):
    if last + arr[i] > arr[i]:
      lastArr = lastArr + [arr[i]]
      last += arr[i]
      tracker[last] = lastArr
    else:
      lastArr = [arr[i]]
      last = arr[i]
      tracker[last] = lastArr
  print(tracker)
  for currSum in tracker:
    if currSum > largest:
      largest = currSum
      largestArr = tracker[currSum]
  return largest

print(maxSub([-1,3,2,1,2,-1,-4,-7,-1,-4,4]))
