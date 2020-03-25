# https://leetcode.com/problems/fibonacci-number

class Solution:
    def fib(self, N: int) -> int:
        if N==0:
            return 0
        f_prev=1
        f_prev_prev=0
        f_current=1
        for i in range (N-1):
            f_current=f_prev+f_prev_prev
            f_prev_prev=f_prev
            f_prev=f_current
            
        return f_current
