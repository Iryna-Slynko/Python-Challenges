#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3304/
"""Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n)."""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums==[]:
            return -1
        start=0
        end=len(nums)-1
        if nums[start]>nums[end]:
            while (start+1)<end:
                middle=(start+end)//2
                if nums[start]>nums[middle]:
                    end=middle
                else:
                    start=middle

            pivot=0
            if nums[start]<nums[end]:
                pivot=start
            else:
                pivot=end

            start=0
            end=len(nums)-1
            if target <= nums[end]:
                start=pivot
            else:
                end=pivot-1

        while start<=end:
            middle=(start+end)//2
            if nums[middle]==target:
                return middle
            elif nums[middle]<target:
                start=middle+1
            else:
                end=middle-1
        return -1
