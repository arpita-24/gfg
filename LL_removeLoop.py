#Function to remove a loop in the linked list.
def removeLoop(self, head):
    # code here
    # remove the loop without losing any nodes
    stack = set()
    prev = None
    curr = head
    while curr:
        if curr not in stack:
            stack.add(curr)
        else:
            prev.next = None
            break

        prev = curr
        curr = curr.next

    return head
