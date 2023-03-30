# Python3 program to check if linked
# list is palindrome using stack


class Node:
    def __init__(self, data):
        self.data = data
        self.ptr = None


# Function to check if the linked list
# is palindrome or not


def ispalindrome(head):
    # Temp pointer
    slow = head

    # Declare a stack
    stack = []

    ispalin = True

    # Push all elements of the list
    # to the stack
    while slow is not None:
        stack.append(slow.data)

        # Move ahead
        slow = slow.ptr

    # Iterate in the list again and
    # check by popping from the stack
    while head is not None:

        # Get the top most element
        i = stack.pop()

        # Check if data is not
        # same as popped element
        if head.data == i:
            ispalin = True
        else:
            ispalin = False
            break

        # Move ahead
        head = head.ptr

    return ispalin


# Driver Code


# Addition of linked list
One = Node(1)
Two = Node(2)
Three = Node(3)
Four = Node(4)
Five = Node(3)
Six = Node(2)
Seven = Node(1)

# Initialize the next pointer
# of every current pointer
One.ptr = Two
Two.ptr = Three
Three.ptr = Four
Four.ptr = Five
Five.ptr = Six
Six.ptr = Seven
Seven.ptr = None

# Call function to check palindrome or not
result = ispalindrome(One)

print("isPalindrome:", result)
