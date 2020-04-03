//https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3285/- leetcode challenge day3 
//Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum=0
        maxSum=nums[0]
        
        
        for number in nums:
            
            currentSum+=number
            if currentSum>=maxSum:
                maxSum=currentSum
                
            if currentSum<0:
                currentSum=0
                
                
        return maxSum
