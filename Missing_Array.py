Problem_link="https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1"

class Solution:
    
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        total_sum = n * (n + 1) // 2
        actsum=sum(arr)
        miss=total_sum-actsum
        return miss
