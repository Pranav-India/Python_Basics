# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createLinkedListFromList(lst):
    if not lst:
        return None
    else:
        head = ListNode(lst[0])
        head.next = createLinkedListFromList(lst[1:])
        return head

def linkedListToString(head):
    result = "ListNode{val: " + str(head.val)
    if head.next:
        result += ", next: " + linkedListToString(head.next) + "}"
    else:
        result += ", next: None}"
    return result

class Solution:
    def addTwoNumbers(self, l1, l2):
        list_1=[]
        while l1 is not None:
            list_1.append(l1.val)
            l1 = l1.next
        
        list_2=[]
        while l2 is not None:
            list_2.append(l2.val)
            l2 = l2.next
        sum_ = int(''.join(map(str, list_1[::-1])))+int(''.join(map(str, list_2[::-1])))
        num_list = [int(digit) for digit in str(sum_)[::-1]]
        linked_list = createLinkedListFromList(num_list)
        # print(linked_list)
        return linked_list

question = Solution()
print(linkedListToString(createLinkedListFromList([3,4,2])))
print(linkedListToString(createLinkedListFromList([4,6,5])))
print(linkedListToString(question.addTwoNumbers(createLinkedListFromList([3,4,2]),createLinkedListFromList([4,6,5]))))