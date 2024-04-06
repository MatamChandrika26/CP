class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def pow2(m):
            if m==1:
                return True
            elif m<1 or m%4!=0:
                return False
            else:
                return pow2(m/4)
        return n>0 and pow2(n)
