class Solution:	
	def binarysearch(self, arr, n, k):
		# code here
		
		low = 0
		high = n-1
		
		
		
		if k > arr[-1] or k < arr[0]:
		    return -1
		pos = 0
		
		while low<= high:
		    mid = (low+high)//2 
		    if arr[mid] == k:
		        pos = mid
		        break
		    elif arr[mid]>k:
		        high = mid - 1
		    elif arr[mid]<k:
		        low = mid + 1
		        
	    if pos>0:
	        return pos
	    else:
	        return -1
