# https://leetcode.com/problems/bitwise-and-of-numbers-range/
"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
"""

class Solution:
        
    def toBitwise(self, num):
        result=num
        templist=[]
        while result!=0:
            bitnum=result%2
            result=result//2
            templist.insert(0,bitnum)
        return templist
   
        
    def bitwiseAnd(self,list1, list2):
        if len(list1)!=len(list2):
            return [0]
        result=[]
        for index in range(len(list2)):
            if list1[index] ==1 and list2[index]==1:
                result.append(1)
            else:
                result.append(0)
        return result
        
        
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        bitlist=[]
        result=self.toBitwise(n)
        for i in range (m,n):
            y=self.toBitwise(i)
            result=self.bitwiseAnd(result, y)
            if result==[0]:
                return 0

        num=0
        for digit in result:
            num*=2
            num+=digit
        return num


    """def toBitwise(self, num):
        result=num
        templist=[]
        while result!=0:
            bitnum=result%2
            result=result//2
            templist.insert(0,bitnum)
        return templist
        
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        bitlist=[]
        nBit=self.toBitwise(n)
        mBit=self.toBitwise(m)
        if len(nBit)!=len(mBit):
            return 0
        result=0
        diff=False
        for i in range(len(nBit)):
            result*=2
            if not diff:
                if nBit[i]==mBit[i]:
                    result+=nBit[i]
                else:
                    diff=True
        return result"""
