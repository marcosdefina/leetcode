class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """ 
        # run through the array in two leveled-loop
        # Sum idx0 to idx1, then idx0 to idx2, then idx0 to idxn
        # Until idxi + idxn = target, break when condition met
        # Optimizations could remove diagonal of matrix       
        for idxi in range(len(nums)):
            for idxj in range(len(nums)):
                if nums[idxi] + nums[idxj] == target:
                    return [idxi, idxj]

sol = Solution()
nums = [2,7,11,15]
target = 9

print(sol.twoSum(nums, target))