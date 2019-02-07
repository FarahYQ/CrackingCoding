# Jump Game II: Given an array of non-negtive ints, 
# determine the min jumps to reach to last index. Ex: [2,3,1,1,4] --> 2
def jump(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
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