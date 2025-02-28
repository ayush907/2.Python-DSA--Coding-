
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class linked_list:

    def __init__(self):
        self.head = None
        self.tail = None

    # method for traversing the link list
    def ll_traversal(self):
        temp = self.head
        while(temp is not None):
            print(temp.data, end=" ")
            temp = temp.next
        print()

    # inserting at the beginning
    def insert_begin(self, data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
            return 
        newnode.next = self.head
        self.head = newnode

    # inserting at the end
    def insert_end(self, data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode 
            self.tail = newnode
            return
        self.tail.next = newnode
        self.tail = newnode

    # inserting element between the linked list with help of a index
    def insert_between(self, idx, data):
        i = 0
        newnode = Node(data)

        if(idx == 0):
            self.insert_begin(data)
            return

        temp = self.head
        prev = None
        while(i != idx):
            prev = temp
            temp = temp.next
            i = i + 1

        newnode.next = prev.next
        prev.next = newnode

    # iterative search in the linked list
    def search_key(self, key):
        idx = 0
        temp = self.head
        while temp != None:
            if temp.data == key:
                return idx
            idx = idx + 1
            temp = temp.next

        return -1   # if the key is not found
    

    # recursive search in a linked list
    def helper(self, head, key):
        if head == None:
            return -1

        if head.data == key:
            return 0 
        
        idx = self.helper(head.next, key)

        if idx == -1:
            return -1
        
        return idx + 1

    def recursive_search(self, key):
        return self.helper(self.head, key)


    #function for deleting the first node
    def delete_first_node(self):
        self.head = self.head.next


    # function for delete the last node
    def delete_last_node(self):
        temp = self.head
        prev = None
        while temp.next != None:
            prev = temp
            temp = temp.next

        prev.next = None
        self.tail = prev


    # calculating the size of a linked list
    def get_size_ll(self):
        size = 0
        temp = self.head
        while temp != None:
            size = size + 1
            temp = temp.next
        return size


    # find and the nth element from the end of a linked_list
    def delete_Nth(self, n):
        # calculating size
        size = self.get_size_ll()

        if n == size:
            self.head = self.head.next    

        to_find = size - n + 1

        i = 1
        ptr = self.head   
        prev = None
        while i < to_find:
            prev = ptr
            ptr = ptr.next
            i = i + 1

        prev.next = prev.next.next



    # reverse a linked list
    def reverse_ll(self):
        current = self.head
        prev = None
        while current != None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev


    # function to find the middle Node in the linked list
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow


    # function to check is the linked_list palinderome or not
    def is_palinderome(self):
        # if head is none or tail is none means only single element present in the linked_list
        if self.head is None or self.tail is None:
            return True
        
        # find the middle node
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow    #storing the slow node in middle variable

        # reversing the second half
        current = middle 
        prev = None
        while current != None:
            next_node = current.next 
            current.next = prev
            prev = current
            current = next_node
        
        left_head = self.head
        right_head = prev

        # comparing the left_half and right_half
        while left_head != None and right_head != None:
            if left_head.data != right_head.data:
                return False      
            left_head = left_head.next
            right_head = right_head.next
            
        return True
    

    # function to detect the cycle in the linked_list
    def is_cycle(self):
        slow = self.head
        fast = self.head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):  # agar cycle hogi toh kabhi na kabhi slow orr fast same node pe milenge
                return True
            
        return False
    

    # function for removing the cycle in the linked_list
    def remove_cycle(self):
        cycle = False
        # first detect the cycle
        slow = self.head
        fast = self.head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                cycle = True
                break

        if cycle == False:
            return
        
        # finding the meeting point
        slow = self.head
        prev = None
        while slow != fast:
            prev = fast
            slow = slow.next
            fast = fast.next
        
        # breaking the cycle
        prev.next = None
        


    
ll = linked_list()

head = Node(10)
second = Node(12)
third = Node(14)
fourth = Node(16)
fifth = Node(18)
sixth = Node(89)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth
sixth.next = fourth

ll.head = head

print(ll.is_cycle())

ll.remove_cycle()
print(ll.is_cycle())

# ll = linked_list()
# ll.insert_begin(7)
# ll.insert_begin(8)
# ll.insert_begin(8)
# ll.insert_begin(7)

# # print(ll.is_palinderome())

# ll.ll_traversal()

# ll.insert_end(70)
# ll.insert_end(80)
# ll.insert_end(90)

# ll.ll_traversal()
# ll.insert_between(2,9000)
# ll.ll_traversal()
# # print(ll.search_key(9000))
# print(ll.recursive_search(9000))
# ll.delete_last_node()
# ll.ll_traversal()
# print(ll.head.data)
# print(ll.tail.data)
# ll.reverse_ll()
# ll.ll_traversal()
# # print(ll.get_size_ll())
# ll.delete_Nth(3)
# ll.ll_traversal()



