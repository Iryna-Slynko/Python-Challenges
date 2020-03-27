https://leetcode.com/problems/robot-return-to-origin/submissions/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        counterX=0
        counterY=0
        for step in moves:
            if step=="U":
                counterY+=1
            elif step=="D":
                counterY-=1
            if step=="R":
                counterX+=1
            elif step=="L":
                counterX-=1
        return counterX==0 and counterY==0
