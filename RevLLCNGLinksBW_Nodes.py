# Node class
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    # Function to insert a new node at the beginning
    def push(self, newElement):
        newNode = Node(newElement)
        newNode.next = self.head
        self.head = newNode

    # Utility function to print the LinkedList
    def PrintList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


# Driver code
Mylist = LinkedList()
Mylist.push(20)
Mylist.push(4)
Mylist.push(15)     
Mylist.push(85)

print("Given linked list")
Mylist.PrintList()
Mylist.reverse()
print("\nReversed linked list")
Mylist.PrintList()
