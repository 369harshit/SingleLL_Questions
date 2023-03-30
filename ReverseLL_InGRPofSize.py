# Python program to reverse a
# linked list in group of given size

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

    def reverse(self, head, k):

        if head is None:
            return None
        current = head
        next = None
        prev = None
        count = 0

        # Reverse first k nodes of the linked list
        while current is not None and count < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        # next is now a pointer to (k+1)th node
        # recursively call for the list starting
        # from current. And make rest of the list as
        # next of first node
        if next is not None:
            head.next = self.reverse(next, k)

        # prev is new head of the input list
        return prev

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next


# Driver program
Mylist = LinkedList()
Mylist.push(9)
Mylist.push(8)
Mylist.push(7)
Mylist.push(6)
Mylist.push(5)
Mylist.push(4)
Mylist.push(3)
Mylist.push(2)
Mylist.push(1)

print("Given linked list")
Mylist.printList()
Mylist.head = Mylist.reverse(Mylist.head, 3)

print("\nReversed Linked list")
Mylist.printList()