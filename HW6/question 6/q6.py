class Node(object):
    def __init__(self, data):
        self.data = data
        self.previous = None


# Class to create a Linked List
class ReverseLinkedList(object):
    def __init__(self, tail=None):
        self.tail = tail

    # Print the linked list
    def print_list(self):
        if self.tail == None:
            raise ValueError("List is empty")

        current = self.tail
        while current:
            print(current.data, end="  ")
            current = current.previous
        print("\n")

    # Find length of Linked List
    def size(self):
        if self.tail == None:
            return 0

        size = 0
        current = self.tail
        while current:
            size += 1
            current = current.previous

        return size

    # Insert a node in a linked list
    def insert(self, data):
        node = Node(data)
        current = self.tail
        if not current:
            self.tail = node
        else:
            while (current.previous):
                current = current.previous
            current.previous = node
            
    # insert node at beginning of list 
    def insert_left(self, data):
        new_node = Node(data)
        old_tail = self.tail 
        self.tail = new_node
        new_node.previous = old_tail

    # Delete a node in a linked list
    def delete(self, data):
        if not self.tail:
            return

        temp = self.tail

        # Check if head node is to be deleted
        if self.tail.data == data:
            head = temp.previous
            print("Deleted node is " + str(self.tail.data))
            return

        while temp.previous:
            if temp.previous.data == data:
                print("Node deleted is " + str(temp.previous.data))
                temp.previous = temp.previous.previous
                return
            temp = temp.previous
        print("Node not found")
        return
    
    def search(self, data):
        current = self.tail
        while current:
            if current.data == data:
                return True 
            return False
            current = current.previous   