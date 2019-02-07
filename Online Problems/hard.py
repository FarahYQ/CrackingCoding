# Jump Game II: Given an array of non-negtive ints, 
# determine the min jumps to reach to last index. Ex: [2,3,1,1,4] --> 2
def jump(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) <= 1: return 0
    self.minJumps = float("inf")
    
    def findPaths(nums, count, pos):
        if pos == len(nums)-1:
            self.minJumps = min(self.minJumps, count)
            return
        for j in range(1,nums[pos]+1):
            if pos+j > len(nums) - 1: break
            else: findPaths(nums,count+1,pos+j)
    findPaths(nums, 0,0)
    if self.minJumps == float("inf"): return 0
    return self.minJumps

def jump(self, nums):
    if len(nums) <= 1: return 0
    l, r = 0, nums[0]
    times = 1
    while r < len(nums) - 1:
        times += 1
        nxt = max(i + nums[i] for i in range(l, r + 1))
        l, r = r, nxt
    return times