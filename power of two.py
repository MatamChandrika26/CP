class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def pow2(m):
            if m==1:
                return True
            elif m<1 or m%2!=0:
                return False
            else:
                return pow2(m/2)
        return n>0 and pow2(n)
