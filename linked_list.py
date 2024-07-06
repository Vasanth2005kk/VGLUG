# 1

class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

l1=Node(2,Node(4,Node(3)))
l2=Node(5,Node(6,Node(4)))

def print_head(head):
    cournt=head
    while cournt is not None:
        print(cournt.val,end=" -> ") 
        cournt=cournt.next

print_head(l1)
print()
print_head(l2)

# 2
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Calculate the sum and carry
        total = val1 + val2 + carry
        carry = total // 10
        sum_val = total % 10

        # Create a new node with the sum value
        current.next = ListNode(sum_val)

        # Move the current pointer
        current = current.next

        # Move l1 and l2 pointers to their next nodes
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next

# Example usage:
# Creating first number: 342 (represented as 2 -> 4 -> 3)
l1 = ListNode(2, ListNode(4, ListNode(3)))
# Creating second number: 465 (represented as 5 -> 6 -> 4)
l2 = ListNode(5, ListNode(6, ListNode(4)))


# Adding the two numbers
result = addTwoNumbers(l1, l2)

# Print the result list
def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

print_list(result)  # Output should be: 7 -> 0 -> 8 -> None (807)


# 3
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self,l1,l2):
        l1_copy=[]
        for i in range(len(l1)):
            cournt=ListNode(l1[i])
            l1_copy.append(str(cournt.val))
            cournt.next = cournt
        l1_copy_ans=int("".join(l1_copy[::-1]))

        l2_copy=[]
        for i in range(len(l2)):
            cournt=ListNode(l2[i])
            l2_copy.append(str(cournt.val))
            cournt.next = cournt
        l2_copy_ans=int("".join(l2_copy[::-1]))

        return list(map(int,list(str(l1_copy_ans+l2_copy_ans))[::-1]))
    
obj=Solution().addTwoNumbers(l1=[2,4,3],l2=[5,6,4])
print(obj)

