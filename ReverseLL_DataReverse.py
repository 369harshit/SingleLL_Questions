# node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# class Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    # Add new element at the end of the list
    def push_back(self, newElement):
        newNode = Node(newElement)
        if self.head is None:
            self.head = newNode
            return
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

    # reverse the list
    def reverseList(self):
        if self.head is not None:
            prevNode = self.head
            tempNode = self.head
            curNode = self.head.next

            prevNode.next = None

            while curNode is not None:
                tempNode = curNode.next
                curNode.next = prevNode
                prevNode = curNode
                curNode = tempNode

            self.head = prevNode

            # display the content of the list

    def PrintList(self):
        temp = self.head
        if temp is not None:
            print("The list contains:", end=" ")
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print()
        else:
            print("The list is empty.")


# test the code
MyList = LinkedList()

# Add five elements in the list.
MyList.push_back(10)
MyList.push_back(20)
MyList.push_back(30)
MyList.push_back(40)
MyList.push_back(50)

# Display the content of the list.
MyList.PrintList()

# Reversing the list.
MyList.reverseList()

# Display the content of the list.
MyList.PrintList()
