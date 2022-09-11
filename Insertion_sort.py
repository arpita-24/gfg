class Solution:
    def insert(self, alist, index, n):
        #code here
        temp = alist[index]
        k = 0
        swap = 0
        for j in range(index-1,-1,-1):
            if temp<alist[j]:
                swap += 1
                alist[j+1] = alist[j]
                k = j
            else:
                break
        if swap>0:
            alist[k] = temp
        # print(alist)
        return alist
        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        #code here
        for i in range(1,n):
            alist = self.insert(alist,i,n)
        
        return alist
