#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3303/
'''Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.'''

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        newList=grid[:][:]
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i ==0 and j==0:
                    newList[0][0]=grid[0][0]
                elif i==0:
                    newList[i][j]=newList[i][j-1]+grid[i][j]
                elif j==0:
                    newList[i][j]=newList[i-1][j]+grid[i][j]
                else:
                    newList[i][j]= min(newList[i-1][j],newList[i][j-1])+grid[i][j]
                    
        return newList[-1][-1]

'''
        m=len(grid)
        if m==0:
            return 0
        n=len(grid[0])
        if n==0:
            return 0
            
        res=grid[:][:]
        res[0][0]=grid[0][0]
        for i in range(1,m):
            res[i][0]=res[i-1][0]+grid[i][0]
        for j in range(1,n):
            res[0][j]=res[0][j-1]+grid[0][j]
        for i in range(1,m):
            for j in range(1,n):
                res[i][j]=min(res[i][j-1],res[i-1][j])+grid[i][j]
        return res[m-1][n-1] '''
