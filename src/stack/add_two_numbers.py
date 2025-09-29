# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        stack_l1 = []
        stack_l2 = []
        l1_tmp = l1
        l2_tmp = l2

        while l1_tmp:
            stack_l1.append(l1_tmp.val)
            l1_tmp = l1_tmp.next

        while l2_tmp:
            stack_l2.append(l2_tmp.val)
            l2_tmp = l2_tmp.next

        buf = 0
        len_l1 = len(stack_l1)
        len_l2 = len(stack_l2)
        prior_node = None

        for idx in range(max(len_l1, len_l2)):
            num_1 = stack_l1.pop() if idx < len_l1 else 0
            num_2 = stack_l2.pop() if idx < len_l2 else 0
            candidate = num_1 + num_2 + buf
            node = ListNode(candidate % 10, prior_node)
            prior_node = node
            buf = candidate // 10

        if buf:
            node = ListNode(buf, prior_node)

        return node



node11 = ListNode(5, None)
# node12 = ListNode(4, node11)
# node13 = ListNode(2, node12)
# node14 = ListNode(7, node13)

node21 = ListNode(5, None)
# node22 = ListNode(6, node21)
# node23 = ListNode(5, node22)

node = Solution().addTwoNumbers(node11, node21)
while node.next:
    print(node.val, sep="")
    node = node.next
print(node.val)
