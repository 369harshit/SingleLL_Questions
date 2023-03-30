# Python3 program to print reverse
# of a linked list

# Node class
class Node:

    # Constructor to initialize
    # the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Recursive function to print
    # linked list in reverse order
    def printrev(self, temp):

        if temp:
            self.printrev(temp.next)
            print(temp.data, end=' ')
        else:
            return

    # Function to insert a new node
    # at the beginning
    def push(self, newElement):

        newNode = Node(newElement)
        newNode.next = self.head
        self.head = newNode


# Driver code
Mylist = LinkedList()

Mylist.push(4)
Mylist.push(3)
Mylist.push(2)
Mylist.push(1)

Mylist.printrev(Mylist.head)


