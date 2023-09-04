# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self,input_list):
        self.list_for_ll = input_list
        self.linkedlist =  self.createLinkedListFromList(self.list_for_ll)
 
    def createLinkedListFromList(self,input_list):
        if not input_list:
            return None
        else:
            head = ListNode(input_list[0])
            head.next = self.createLinkedListFromList(input_list[1:])
            return head

    def linkedListToString(self,head):
        result = "ListNode{val: " + str(head.val)
        if head.next:
            result += ", next: " + self.linkedListToString(head.next) + "}"
        else:
            result += ", next: None}"
        return result

    def __str__(self):
        return self.linkedListToString(self.linkedlist)


ll_obj = LinkedList([2,3,4])

print(ll_obj)