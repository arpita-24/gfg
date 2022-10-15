def removeDuplicates(head):
    #code here
    prev = head
    curr = head.next
    while curr :
        if prev.data == curr.data:
            temp = curr
            curr = temp.next
            prev.next = curr
            temp = None
        else:
            prev = prev.next
            curr = curr.next
    return head
    
