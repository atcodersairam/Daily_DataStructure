Problem_link="https://www.geeksforgeeks.org/problems/reverse-digit0316/1"

class Solution:
	def reverse_digit(self, n):
	    rev = 0
	    while n!=0:
	        r=n%10
	        rev=rev*10+r
	        n=n//10
	    return rev    
