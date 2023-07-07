
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
        # your job is to implement stack data structure by using linkedlist

    def __init__(self):
        # add your instance variables
        
        self.head = Node()
    
        pass

        # add an element to the top of a stack 

    def push(self, data):

        

        if self.head == None:
            self.head = Node(data)
        
        else:
            head = self.head.next
            head = Node(data)
            self.head.next = head.next 
        

        


        return 0

        # remove an element from the top of a stack
        # when you are trying to pop more than the size of stack
        # then you should throw an error 
<<<<<<< HEAD
        #  
    def pop(self, data):

        prevNode = None
        nextNode = None
        head = self.head


        while head is not None:

            if head.data == data:
                nextNode = head.next
                prevNode.next = nextNode

                prevNode = head
                head = head.next




=======
        
    def pop():
>>>>>>> 261d07d0b3c51da54aea5ef3ca0a569d8349fb17

        return 0

        # check whether the stack is empty or not
        # if stack is empty return True else return False
    def isEmpty():

        head = Node()

        if head is not None:
            return False
        else:
            return True
        

        # get the value of the top element without removing it
        # if stack is empty, then return -1
    def peek():

        head = Node()

        if head.next == None:
            return head.data

        return 0
    
