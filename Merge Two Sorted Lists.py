
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        use = tem = ListNode()
        while list1 and list2:
            if list1.val<list2.val:
                use.next=list1
                use= use.next; list1=list1.next;
            else:
                use.next=list2
                use = use.next;list2 = list2.next;
        if list1 or list2:
            use.next=list1 if list1 else list2

        return tem.next   
