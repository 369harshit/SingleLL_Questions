# Python3 implementation of the approach

# Class for a node of
# the linked list


class newNode:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to print the linked list


def printList(node):
    while node is not None:
        print(node.data, "->", end=" ")
        node = node.next
    print("NULL")


# Recursive function to return the
# count of nodes in the linked list


def cntNodes(node):
    if node is None:
        return 0

    return 1 + cntNodes(node.next)


# Function to update and print
# the updated list nodes


def updateList(head, m):
    # Total nodes in the list
    cnt = cntNodes(head)

    if cnt != m and m < cnt:

        # Count of nodes to be skipped
        # from the beginning
        skip = cnt - m
        prev = None

        curr = head

        # Skip the nodes
        while skip > 0:
            prev = curr
            curr = curr.next
            skip -= 1

        # Change the pointers
        prev.next = None
        tempHead = head
        head = curr

        # Find the last node
        while curr.next is not None:
            curr = curr.next

        # Connect it to the head
        # of the sub list
        curr.next = tempHead

    # Print the updated list
    printList(head)


# Driver code


# Create the list
head = newNode(4)
head.next = newNode(5)
head.next.next = newNode(6)
head.next.next.next = newNode(1)
head.next.next.next.next = newNode(2)
head.next.next.next.next.next = newNode(3)

m = 3

updateList(head, m)
