"""Most common word in the text excluding banned words"""

import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        d={}
        max,most_fr=0,0
        p=re.sub(r'[^\w\s]', ' ', paragraph)
        p=p.lower().replace(",.","")
        paragraph_list=p.split()
        for word in paragraph_list:
            if word not in banned:
                d[word]=d.get(word,0)+1
        print(d)
        for i in d:
            if d[i]>max:
                max, most_fr=(d[i],i)
        return most_fr
