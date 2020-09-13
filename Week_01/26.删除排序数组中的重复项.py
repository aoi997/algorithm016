#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # l = 0
        # for i, num1 in enumerate(nums):
        #     if l < 1 or num1 != nums[l - 1]:
        #         if i != l:
        #             nums[l] = num1 
        #         l += 1
        i,j = 0,1
        while j < (len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
                j += 1
            else:
                j += 1
        return i+1
# @lc code=end

