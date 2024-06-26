problem_link="https://www.geeksforgeeks.org/problems/prime-number2314/1"

class Solution:
    def isPrime(self, N):
        if N <= 1:
            return 0
        if N == 2:
            return 1
        if N % 2 == 0:
            return 0
        
        # Check odd divisors from 3 up to the square root of N
        limit = int(N**0.5) + 1
        for i in range(3, limit, 2):
            if N % i == 0:
                return 0
        
        return 1
