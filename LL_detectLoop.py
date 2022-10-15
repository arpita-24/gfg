def detectLoop(self, head):
        #code here
        s = set()
        temp = head
        while temp:
            if temp in s:
                return True
                
            s.add(temp)
            temp = temp.next
            
            
        return False
