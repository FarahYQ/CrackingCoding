
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