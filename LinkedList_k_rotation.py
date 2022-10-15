'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''    
#Function to rotate a linked list.
def rotate(self, head, k):
    # code here
    orgHead = head
    curr = head
    stack = []
    cnt = 0
    length = 0
    c = head
    while c:
        c = c.next
        length += 1

    while cnt < k:
        stack.append(curr)
        curr = curr.next
        cnt += 1

    head = curr    

    while curr and curr.next:
        cnt += 1
        curr = curr.next
    stack = stack[::-1] 

    if k == length:
        return orgHead

    while len(stack) != 0:
        if curr:
            curr.next = stack.pop()
            curr = curr.next
        else:
            break

    curr.next = None

    return head
