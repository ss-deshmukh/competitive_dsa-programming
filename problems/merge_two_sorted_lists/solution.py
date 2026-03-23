class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Create a dummy node to act as the start of the result list
        dummy = ListNode(0)
        ptr = dummy

        # 2. Iterate as long as BOTH lists have nodes to compare
        while list1 and list2:
            if list1.val <= list2.val:
                ptr.next = list1     # Link the smaller node
                list1 = list1.next   # Move the pointer in list1
            else:
                ptr.next = list2
                list2 = list2.next
            ptr = ptr.next           # Move the result pointer forward

        # 3. If one list runs out, attach the entire remainder of the other
        # This fixes Case 3: if list1 is [], ptr.next becomes [0]
        ptr.next = list1 if list1 is not None else list2

        return dummy.next