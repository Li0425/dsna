# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        all_ele = []
        all_ele.append(list1.val)
        temp = list1.next
        while temp:
            all_ele.append(temp.val)
            temp = temp.next
        
        all_ele.append(list2.val)
        temp = list2.next
        while temp:
            all_ele.append(temp.val)
            temp = temp.next
        
        result = []
        all_ele.sort()
        return all_ele.sort()
        # print(all_ele)
        # for idx, ele in enumerate(all_ele):
        #     if len(all_ele) > 1 and idx != len(all_ele)-2:
        #         curr_node = ListNode(ele, ListNode(all_ele[idx+1], None))
        #         result.append(curr_node)
        #     elif len(all_ele) == 0:
        #         return []
        #     else:
        #         return ListNode(all_ele[0], None)
                
        # return result.sort()