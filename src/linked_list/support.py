class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head):
    tmp = head
    while tmp:
        print(tmp.val, end=" ")
        tmp = tmp.next
    print()

def prepare_list(ml):
    new_head = ListNode(0)
    cur = new_head
    for val in ml:
        tmp = ListNode(val)
        cur.next = tmp
        cur = tmp
    return new_head.next



