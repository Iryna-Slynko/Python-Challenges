//leetcode 30-day challenge. Day-2

class Solution:
    def isHappy(self, n: int) -> bool:
        numbers=str(n)
        total=0
        checkList={}
        while True:
            total=0
            
            for number in numbers:
                total=total+int(number)**2
            if total==1:
                return True
            elif total in checkList:
                return False
            else:
                checkList[total]=1
                
                
           
            numbers=str(total)
