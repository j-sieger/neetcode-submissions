# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        nodes_list = []
        while curr:
            nodes_list.append(curr)
            curr = curr.next

        i,j = 0 , len(nodes_list)-1
        while i<j:
            nodes_list[i].next = nodes_list[j]
            i = i +1
            if i>=j:
                break
            nodes_list[j].next = nodes_list[i]
            j -=1
        nodes_list[i].next = None
            

    ### BELOW CODE ALSO WORKING. #####
        # curr = head
        # nodes_list = []
        # while curr:
        #     nodes_list.append(curr)
        #     curr = curr.next
        
        # dummy = node = ListNode()
        # i,j = 0 , len(nodes_list)-1

        # while i<j:
        #     node.next = nodes_list[i]
        #     i +=1
        #     node = node.next
        #     if i>=j:
        #         break
            
        #     node.next = nodes_list[j]
        #     j -=1
        #     node = node.next

        # node.next = nodes_list[i]
        # node.next.next = None
        
        





        