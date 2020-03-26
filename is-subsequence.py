#https://leetcode.com/problems/is-subsequence/submissions/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        searchPosition=0
        result=True
        for letter in s:
            result=False
            for char in range(searchPosition, len(t)):
                    if letter==t[char]:
                        result=True
                        searchPosition=char+1
                        break
            if result==False:
                break
        
        return result   
