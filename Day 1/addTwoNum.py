# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # UPER
        # Understand
        # I have two linked lists. Each linked list represents a positive number. Oh and the LL is reversed.
        # Our task is to get those two numbers as represented in each linked list, and return the sum represented as a LL.
        # Also in reverse order as the inputs are similarly.
        # Plan
        # Take each nodes value from a linked list to create our positive integer and save it.
        # do the same for the other linked list.
        # Make sure to create the ints in the right order.
        # sum the numbers together.
        # and then reverse and put back into singly linked list
        # return answer
        # Execute
        int1 = ""
        int2 = ""

        curr = l1
        while curr != None:
            int1 = str(curr.val) + int1
            curr = curr.next

        curr = l2
        while curr != None:
            int2 = str(curr.val) + int2
            curr = curr.next

        int1 = int(int1)
        int2 = int(int2)
        my_sum = int1 + int2
        my_sum = str(my_sum)
        my_sum = my_sum[::-1]
        my_list = []
        for i in my_sum:
            my_list.append(int(i))

        result = ListNode()
        curr = result
        while len(my_list) > 0:
            curr.val = my_list[0]
            my_list.pop(0)
            if len(my_list) == 0:
                continue
            else:
                curr.next = ListNode()
                curr = curr.next

        return result

        # Reflect
