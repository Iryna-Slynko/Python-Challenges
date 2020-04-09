#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3291/
#Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

class Solution:

    def processWord(self, word: str):
        newChars=[]
        for i in range (0,len(word)):
            if word[i]=="#":
                if newChars!=[]:
                    newChars.pop()
                    
                continue
                
            newChars.append(word[i])
        return newChars
    
    
    def backspaceCompare(self, S: str, T: str) -> bool:
        newS=self.processWord(S)
        newT=self.processWord(T) 
    
        return newS==newT
