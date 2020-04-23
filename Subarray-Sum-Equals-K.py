#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3307/
#Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # [  1, 1,1  ,-1,1,-1,1]
        
        sum_dict={0: 1}
        sum=0
        result=0
        for num in nums:
            sum+=num
            diff=sum-k 
            if diff in sum_dict:
                result+=sum_dict[diff]
                
            if sum not in sum_dict:
                sum_dict[sum]=0
            sum_dict[sum]+=1
            print(sum_dict)
        
        return result
