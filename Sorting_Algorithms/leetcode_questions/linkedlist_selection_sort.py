class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # WRITE INSERTION_SORT METHOD HERE #
    #                                  #
    #                                  #
    #                                  #
    #                                  #
    ####################################

# strategy to solve
# Check the list: If it has zero or one node, it is already sorted.

# Create a sorted list: Start with sorted_list = None.
# Take a node: Use current to process each node from the original list

# Save the next node: Store current.next in next_node before changing any links.

# Find the correct position: If the current value is smaller than the first sorted value, 
# insert it at the beginning. Otherwise, find the correct position inside the sorted list

# Insert the node: Update the next pointers to place the node correctly.

# Move forward: Set current = next_node and repeat until all nodes are processed.

# Update head and tail: Set the new head and find the last node to update the tail.


    def insertion_sort(self):
        if self.head is None or self.head is sorted:
            return None
        sorted_list = None
        current = self.head
        while current is not None:
            next_node = current.next
            if sorted_list is None or current.value < sorted_list.value:
                current.next = sorted_list
                sorted_list = current
            else:
                temp = sorted_list
                while temp.next is not None and temp.next.value < current.value:
                    temp = temp.next
                current.next = temp.next
                temp.next = current
                
            current = next_node
        self.head = sorted_list
        self.tail = self.head
        while self.tail.next is not None:
            self.tail = self.tail.next
            
                
                
                
                
            
        


my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.insertion_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

