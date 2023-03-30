# A linked list node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# deletes alternate nodes
# of a list starting with head
def deleteAlt(head):
    if head is None:
        return

    # Initialize prev and node to be deleted
    prev = head
    now = head.next

    while prev is not None and now is not None:

        # Change next link of previous node
        prev.next = now.next

        # Free memory
        now = None

        # Update prev and node
        prev = prev.next
        if prev is not None:
            now = prev.next


# UTILITY FUNCTIONS TO TEST fun1() and fun2()
# Given a reference (pointer to pointer) to the head
# of a list and an , push a new node on the front
# of the list.
def push(head_ref, new_data):
    # allocate node
    new_node = Node(new_data)

    # put in the data
    new_node.data = new_data

    # link the old list of the new node
    new_node.next = head_ref

    # move the head to point to the new node
    head_ref = new_node
    return head_ref


# Function to print nodes in a given linked list
def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next


# Driver code
if __name__ == '__main__':
    # Start with the empty list
    head = None

    # Using head=push() to construct below list
    # 1.2.3.4.5
    head = push(head, 5)
    head = push(head, 4)
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)

    print("List before calling deleteAlt() ")
    printList(head)

    deleteAlt(head)

    print("\nList after calling deleteAlt() ")
    printList(head)
