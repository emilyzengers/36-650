class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

# Class to create a Linked List
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    # Print the linked list
    def print_list(self):
        if self.head == None:
            raise ValueError("List is empty")

        current = self.head
        while current:
            print(current.data, end="  ")
            current = current.next
        print("\n")

    # Find length of Linked List
    def size(self):
        if self.head == None:
            return 0

        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next

        return size

    # Insert a node in a linked list
    def insert(self, data):
        node = Node(data)
        current = self.head
        if not current:
            self.head = node
        else:
            while (current.next):
                current = current.next
            current.next = node
      
    # insert node at beginning of list 
    def insert_at_beginning(self, data):
        new_node = Node(data)
        old_head = self.head 
        self.head = new_node
        new_node.next = old_head
    
    # Insert a node in a linked list at the beginning
    def insert_front(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    # Delete a node in a linked list
    def delete(self, data):
        if not self.head:
            return

        temp = self.head

        # Check if head node is to be deleted
        if self.head.data == data:
            head = temp.next
            print("Deleted node is " + str(self.head.data))
            return

        while temp.next:
            if temp.next.data == data:
                print("Node deleted is " + str(temp.next.data))
                temp.next = temp.next.next
                return
            temp = temp.next
        print("Node not found")
        return
    
    def sort(self):
        # exract elements of linked list and assign to a list
        list = []
        current = self.head
        while current:
            list.append(current.data)
            current = current.next
        
        #print(list)

        # sort elements of list
        
        # Traverse through all array elements
        for j in range(len(list)):
     
        # Find the minimum element in remaining
        # unsorted array
            min_idx = j
            for k in range(j+1, len(list)):
                if list[min_idx] > list[k]:
                    min_idx = k    
        # Swap the found minimum element with the first element       
            tmp = list[j]
            list[j] = list[min_idx] 
            list[min_idx] = tmp
        
        #print(list)
        
        # change data of each node
        current = self.head
        for m in range(len(list)):
            current.data = list[m]
            current = current.next
            
        # print sorted linked list
        self.print_list()
        
    def remove_dups(self):
        current = self.head
        while current:
            compare = current
            while compare.next:
                if current.data == compare.next.data:
                    compare.next = compare.next.next
                else:
                    compare = compare.next
            current = current.next
            