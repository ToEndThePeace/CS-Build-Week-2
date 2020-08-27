# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def remove_kth_from_end(head, k):
    # first-pass, store them all in a standard list for easier manipulation
    # not memory efficient, but time complexity is O(n)
    index_map = []
    current = head
    while current is not None:
        index_map.append(current)
        current = current.next
    
    if k > 0 and len(index_map) >= k:
        remove_this = index_map[-k]
        if head == remove_this:
            head = remove_this.next
        else:
            index_map[-(k + 1)].next = remove_this.next
    
    return head


"""
Write a function that receives as input the head node of a linked list and an integer k. Your function should remove the kth node from the end of the linked list and return the head node of the updated list.

For example, if we have the following linked list: 
(20) -> (19) -> (18) -> (17) -> (16) -> (15) -> (14) -> (13) -> (12) -> (11) -> null

The head node would refer to the node (20).  Let k = 4, so our function should remove the 4th node from the end of the linked list, the node (14).

After the function executes, the state of the linked list should be:
(20) -> (19) -> (18) -> (17) -> (16) -> (15) -> (13) -> (12) -> (11) -> null

If k is longer than the length of the linked list, the linked list should not be changed.

Can you implement a solution that performs a single pass through the linked list and doesn't use any extra space?

Note: When reading the tests, the linked list contents are enumerated in between square brackets; this does NOT mean the inputs are arrays.

For example, a test input of head: [2, 4 ,6] indicates that the input is a singly-linked list
(2) -> (4) -> (6) -> null whose head is the first element in the linked list.


Input:
head: [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
k: 4
Expected Output:
[20, 19, 18, 17, 16, 15, 13, 12, 11]


Input:
head: [2, 4, 6]
k: 5
Expected Output:
[2, 4, 6]


Input:
head: [10, 20, 30, 40, 50]
k: 1
Expected Output:
[10, 20, 30, 40]


Input:
head: [100, 200]
k: 2
Expected Output:
[200]


t:
head: [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
k: 0
Expected Output:
[20, 19, 18, 17, 16, 15, 14, 13, 12, 11]

"""