class Solution:
    def thirdLargest(self,a, n):
        # code here
        if n<3:
            return -1
        else:
            b=sorted(a,reverse=1)
            return b[2]
