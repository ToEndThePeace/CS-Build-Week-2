from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        my thought process:
            iterating over any linked list requires a while loop
            iterating over both at the same time is going to required 2 conditions

            first set the head, as it would complicate the loop to do it inside
            the loop over both linked lists, checking each value and appending the smaller one

            since the listst are presorted, we can maintain the sort by simply adding the
            smaller valued node each loop iteration

            after the loop breaks (when we've reached the end of either list),
            I'll implement two more loops (one of which will not run) that loop over the
            remaining elements of each list 
            this works because anything left over will be larger than what we've seen so far
        """
        # error handling so that next if doesn't throw an error
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next

        # keep track of our current place in the linked list
        current = head

        # loop over both with comparisons done for each iteration to see what's next
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            # increment current pointer
            current = current.next

        # append the remaining nodes to the new list
        # THESE ACTUALLY don't need to be loops, because the remaining list will be in order
        # and the pointer is already correct
        if l1 is not None:
            current.next = l1

        if l2 is not None:
            current.next = l2

        return head


def make_linked_list(l: List[int]) -> ListNode:
    head = ListNode(l[0])

    current = head
    for i in range(1, len(l)):
        current.next = ListNode(l[i])
        current = current.next
    return head


def print_linked_list(head: ListNode) -> None:
    print("[", end="")
    current = head
    while current is not None:
        if current.next is not None:
            print(f"{current.val}, ", end="")
        else:
            print(f"{current.val}", end="")
        current = current.next
    print("]")


test = Solution()

ex1 = [make_linked_list([1, 2, 4]),
       make_linked_list([1, 3, 4])]
ex2 = [make_linked_list([0, 0, 2, 4, 7, 10]),
       make_linked_list([0, 1, 1, 2, 3, 4, 4, 5, 20])]

print_linked_list(test.mergeTwoLists(*ex1))
print_linked_list(test.mergeTwoLists(*ex2))
