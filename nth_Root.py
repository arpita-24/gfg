class Solution:
	def NthRoot(self, n, m):
		# Code here

        got = 0
        k = 1
        res = k**n
        while res<=m:
            
            if res == m:
                got = 1
                break
            else:
                k += 1
            
            res = k**n
            
        if got>0:    
            return k
        else:
            return -1
