#linked List

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,"=>")
            temp = temp.next

    #insert at first position
    def insertFirstPos(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    #insert after a node
    def insertAfter(self,data,prevNode):
        newNode = Node(data)

        newNode.next = prevNode.next
        prevNode.next = newNode

    #insert at the end
    def insertAtEnd(self, data):
        newNode = Node(data)

        #check if head is empty
        if self.head is None:
            self.head = newNode

        #traverse the list and append at last
        last = self.head
        while last.next:
            last = last.next

        last.next = newNode

    #delete node if value is found
    def deleteNode(self,key):
        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if (temp == None):
            return

        # Unlink the node from linked list
        prev.next = temp.next

        temp = None

    # delete node at the position
    def deleteNodeAtPosition(self, position):

        temp = self.head

        if temp is not None:
            if position == 0:
                self.head = temp.next
                temp = None
                return

        for i in range(position - 1):
            temp = temp.next

        if (temp is not None) and (temp.next is not None) and (temp.next.next is not None):
            temp.next = temp.next.next

        return

    # get count linked list iterative
    def getCountIterative(self):

        count = 0

        temp = self.head

        while temp is not None:
            count = count + 1
            temp = temp.next

        return count

    # get count recursive
    def getCountRecursive(self, node):

        if not node:
            return 0

        return 1 + self.getCountRecursive(node.next)

    def getCountRecursiveCaller(self):

        return self.getCountRecursive(self.head)





llist = LinkedList()

llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third

llist.insertFirstPos(4)
llist.insertAfter(66, second)
llist.insertAtEnd(11)
llist.printList()
#llist.deleteNode(4)
llist.deleteNodeAtPosition(0)
llist.printList()
print('count is', llist.getCountIterative())
print('count is r', llist.getCountRecursiveCaller())