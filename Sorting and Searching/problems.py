# Problem 10.1: Merge sorted array b into sorted array a which has enough buffer for b
def mergeBintoA(a,b):
  if len(b) == 0: return a
  lengthof_filledA = 0
  for i in range(len(a)):
    if a[i] != None:
      lengthof_filledA = i
    else: break

  idx = len(a) - 1
  print(lengthof_filledA,idx)
  while len(b) > 0:
    if a[lengthof_filledA] > b[-1]:
      a[idx] = a[lengthof_filledA]
      a[lengthof_filledA] = None
      idx -= 1
      lengthof_filledA -= 1
    else:
      to_add = b.pop()
      a[idx] = to_add
      idx -= 1
  return a

print(mergeBintoA([1,3,5,7,None, None,None], [2,4,6]))

# Problem 10.2: Search for num in rotated sorted array
def find_num_in_rotated(arr,num):
  print(arr)
  if len(arr)==0: return -1
  mid = int(len(arr)/2)
  if arr[mid] == num:
    return mid
  elif arr[0] < arr[mid]:
    if num >= arr[0] and num < arr[mid]:
      return find_num_in_rotated(arr[:mid],num)
    else:
      res = find_num_in_rotated(arr[mid+1:],num)
      if res != -1:
        return res + mid + 1
      else: return res
  else:
    if num > arr[mid] and num <= arr[-1]:
      res = find_num_in_rotated(arr[mid+1:],num)
      if res != -1:
        return res + mid + 1
      else: return res
    else:
      return find_num_in_rotated(arr[:mid],num)

print(find_num_in_rotated([10,15,20,0,5],5))
print(find_num_in_rotated([50,5,20,30,40],5))

# Problem: Implement quicksort
def quicksort(arr):
  if len(arr) <= 1: return arr
  left = 0
  right = len(arr) - 2
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

  return quicksort(arr[:left]) + [pivot]+ quicksort(arr[left+1:])

print("result is:",quicksort([2,6,5,0,7,8,3]))

# Problem 10.10: Rank from Stream
def getRankOfNumber(nums, target):
  if len(nums) == 0: return -1
  if len(nums) == 1 and nums[0] == target: return 0
  left = 0
  right = len(nums)-2
  last = nums[len(nums)-1]
  while left <= right:
    print(left, right, nums, nums[left])
    while nums[left] <= last and left < len(nums)-1: left += 1
    while nums[right] > last: right -= 1

    if left < right:
      temp = nums[left]
      nums[left] = nums[right]
      nums[right] = temp
      left += 1
      right -= 1
  nums[len(nums)-1] = nums[left]
  nums[left] = last
  if nums[left] == target: return left
  elif nums[left] > target: return getRankOfNumber(nums[:left], target)
  else: return left + 1 + getRankOfNumber(nums[left+1:],target)

print(getRankOfNumber([5,1,4,4,5,9,7,13,3], 4))

