class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        windowSize=len(p)
        srcSize=len(s)
        if windowSize>srcSize:
            return[]
        iterSize=srcSize-windowSize+1
        i=0
        p=sorted(p)
        res=[]
        while iterSize:
            x=s[i:windowSize+i]
            x=sorted(x)
            if x==p:
                res.append(i)
            iterSize-=1
            i+=1
        return res
