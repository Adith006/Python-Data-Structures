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

    # WRITE MERGE METHOD HERE #
    #                         #
    #                         #
    #                         #
    #                         #
    ###########################
    
    def merge(self,other_list):
        if other_list.head is None:
            return
        if self.head is None:
            self.head = other_list.head
            self.tail = other_list.tail
            self.length = other_list.length
            return
        
        first = self.head
        second = other_list.head
        
        if first.value <= second.value:
            new_head = first
            first = first.next
        else:
            new_head = second
            second = second.next
        current = new_head
        
        while first is not None and second is not None:
            if first.value<= second.value:
                current.next = first
                first = first.next
                
            else:
                current.next = second
                second = second.next
            
            current = current.next
            
        if first is not None:
            current.next = first
        else:
            current.next = second
            
        self.head = new_head
        self.tail = self.head
        
        while self.tail.next is not None:
            self.tail = self.tail.next
            
        self.length += other_list.length
            
        
        


l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)


l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""