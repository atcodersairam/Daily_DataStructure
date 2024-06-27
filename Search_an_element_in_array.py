Problem_Link="https://www.geeksforgeeks.org/problems/search-an-element-in-an-array-1587115621/1"

class Solution:
    #Complete the below function
    def search(self,arr, n, x):
        #Your code here
        for i in range(0,len(arr),1):
            if arr[i]==x:
                return i
            
        return -1
