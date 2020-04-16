#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3300/

"""Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_list=[]
        total=1
        for i in range(len(nums)):
            new_list.append(total)
            total*=nums[i]#multiply([:i]) and add it at the next step
            
        total=1
        for i in range(len(nums)-1, -1, -1):
            new_list[i]*=total
            total*=nums[i]#multiply(nums[i:])

        return new_list
