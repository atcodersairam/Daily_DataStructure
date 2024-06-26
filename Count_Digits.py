Problem="https://www.geeksforgeeks.org/problems/count-digits5716/1"
class Solution:
    def evenlyDivides(self, N: int) -> int:
        count = 0
        N_str = str(N)
        for digit_char in N_str:  # iterate through each character in the string
            digit = int(digit_char)  # convert character to integer
            if digit != 0 and N % digit == 0:  # check if N is divisible by digit and digit is not zero
                count += 1
        return count
