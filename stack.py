
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
        # your job is to implement stack data structure by using linkedlist that you
        # previously implemented. Keep in mind that you can always modify and change your linkedlist
        # as needed 

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





        return 0

        # check whether the stack is empty or not
    def isEmpty():

        head = Node()

        if head is not None:
            return False
        else:
            return True
        

        # get the value of the top element without removing it

    def peek():

        head = Node()

        if head.next == None:
            return head.data

        return 0
    
