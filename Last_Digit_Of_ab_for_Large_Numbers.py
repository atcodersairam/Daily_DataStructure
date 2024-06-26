Problem Link:"https://www.geeksforgeeks.org/problems/find-last-digit-of-ab-for-large-numbers1936/1"

class Solution:
    def getLastDigit(self, a, b):
        # code here 
        a_int=int(a)
        b_int=int(b)
        return pow(a_int,b_int,10)
