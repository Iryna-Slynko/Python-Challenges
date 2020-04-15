#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3299/
"""You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift). 
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.

Example:

Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation: 
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"  """

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        count=0
        for index in range (0,len(shift)):
            if shift[index][0]==1:
                count-=shift[index][1]
            else:
                count+=shift[index][1]
        
        count=count % len(s)
       
        
        return s[count:]+ s[:count]
