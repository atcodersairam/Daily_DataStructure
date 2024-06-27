Question="https://www.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1"


def getMinMax( a, n):
    mini=a[0]
    maxi=a[0]
    for i in range(0,len(a),1):
        if a[i]<mini:
            mini=a[i]
        if a[i]>maxi:
            maxi=a[i]
    return mini,maxi
    
