# Python3 program to find
# Nth node from end

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # CreateNode and make linked list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Function to get the nth node from
    # the last of a linked list
    def printNthFromLast(self, n):
        temp = self.head  # Used temp variable

        length = 0
        while temp is not None:
            temp = temp.next
            length += 1

        # Print count
        if n > length:  # If entered location is greater than length of linked list
            print('Location is greater than the' +
                  ' length of LinkedList')
            return
        temp = self.head
        for i in range(0, length - n):
            temp = temp.next
        print(temp.data)


# Driver's Code
if __name__ == "__main__":
    MyList = LinkedList()
    MyList.push(20)
    MyList.push(4)
    MyList.push(15)
    MyList.push(35)

    # Function call
    MyList.printNthFromLast(4)

# This code is contributed by Yogesh Joshi
