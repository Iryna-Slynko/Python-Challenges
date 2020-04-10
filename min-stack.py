#Min Stack
#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3292/

class MinStack:

    def __init__(self):
        self.elements=[]
        self.min_elements=[]
        

    def push(self, x: int) -> None:
        self.elements.append(x)
        if self.min_elements != []:
            prev_min=self.getMin()
            new_min=prev_min
            if new_min > x:
                new_min=x
            self.min_elements.append(new_min)
        else:
            self.min_elements.append(x)
        

    def pop(self) -> None:
        self.elements.pop()
        self.min_elements.pop()
        

    def top(self) -> int:
        last=len(self.elements)-1
        return self.elements[last]
        

    def getMin(self) -> int:
        last=len(self.min_elements)-1
        return self.min_elements[last]
