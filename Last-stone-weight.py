#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3297/

class Solution:
"""We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)"""

    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort()
            last=stones.pop()
            second_last=stones.pop()
            new_number=last-second_last
            stones.append(new_number)
        return stones[0]
