    //Given an array of strings, group anagrams together.
    //https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3288/
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        etalons={}
        
        for word in strs:
            lettersSorted="".join(sorted(word))
            if lettersSorted not in etalons:
                etalons[lettersSorted]=[]
            etalons[lettersSorted].append(word)
        
        List=etalons.values()
        return List
