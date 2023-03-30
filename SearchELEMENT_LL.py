# Iterative Python3 program to search an element
# in linked list

# Node class


class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class


class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head as None

    # This function insert a new node at the
    # beginning of the linked list
    def push(self, newElement):
        newNode = Node(newElement)
        newNode.next = self.head
        self.head = newNode

    # This Function checks whether the value
    # x present in the linked list
    def search(self, x):

        # Initialize current to head
        current = self.head

        # loop till current not equal to None
        while current is not None:
            if current.data == x:
                return True  # data found

            current = current.next

        return False  # Data Not found


# Driver code
if __name__ == '__main__':

    # Start with the empty list
    Mylist = LinkedList()

    Mylist.push(10)
    Mylist.push(30)
    Mylist.push(11)
    Mylist.push(21)
    Mylist.push(14)

    # Function call
    if Mylist.search(21):
        print("Yes")
    else:
        print("No")

