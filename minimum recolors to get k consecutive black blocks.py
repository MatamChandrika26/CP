class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        if k==0:
            return 0
        if k==1:
            if "B" in blocks:
                return 0
            else:
                return 1
        windowsize=k
        slidingwindowcount=len(blocks)-windowsize+1
        index=0
        minimum=sys.maxsize
        while slidingwindowcount>0:
            tmp=blocks[index:windowsize+index]
            minimum_tmp=0
            for i in tmp:
                if i=="W":
                    minimum_tmp+=1
            if minimum_tmp<minimum:
                minimum=minimum_tmp
            index+=1
            slidingwindowcount-=1
        return minimum
