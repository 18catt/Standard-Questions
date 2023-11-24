from math import factorial
#User function Template for python3
class Solution:

	def nthRowOfPascalTriangle(self,n):
	    # code here
	    res =[]
	    for r in range(n):
	        temp = factorial(n-1)//(factorial(n-r-1)*factorial(r)) #for pascal's triangle for every position the value is equal to nCr where n is the row and r goes from 0 to (n-1)
	        res.append(temp%(10**9+7))
	    return res
