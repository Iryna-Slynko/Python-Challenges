#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3301/

"""Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid."""

class Solution:
    def checkValidString(self, s: str) -> bool:
        
        count_minus=0
        count_add=0
        for char in s:
            if char=="(":
                count_minus+=1
                count_add+=1
            if char=="*":
                count_add+=1
                count_minus-=1
            if char==")":
                count_minus-=1
                count_add-=1
            if count_add<0:
                return False
            if count_minus<0:
                count_minus=0
        
        return count_minus==0
