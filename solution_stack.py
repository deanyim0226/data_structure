class Node:
    
    def __init__(self,data =None) -> None:
        self.data = data
        self.next = None
     
class Stack:
        # your job is to implement stack data structure by using linkedlist that you
        # previously implemented. Keep in mind that you can always modify and change your linkedlist
        # as needed 

    def __init__(self) -> None:
        # add your instance variables
        self.head = Node()
        self.size = 0
        pass

        # add an element to the top of a stack 

    def push(self,element):
        
        if self.size == 0:

            node = Node(element)
            self.head = node 
            self.size = 1

        else:
            
            currNode = self.head

            while currNode.next != None:
                
                currNode = currNode.next
            
            node = Node(element)
            currNode.next = node
            self.size += 1

        
        # remove an element from the top of a stack
        # when you are trying to pop more than the size of stack
        # then you should throw an error 
 
    def pop(self):
        
        if self.size > 0:
            
            if self.size == 1:
                self.head = None
                self.size -= 1
            else:

                currNode = self.head
                prevNode = None
            
                while currNode.next != None:

                    prevNode = currNode
                    currNode = currNode.next

                prevNode.next = None
                self.size -= 1

        # check whether the stack is empty or not
    def isEmpty(self):

        if self.size == 0:
            return True
        else:
            return False

        # get the value of the top element without removing it

    def peek(self):
        
        if self.size > 0:

            currNode = self.head

            while currNode.next != None:
                
                currNode = currNode.next
            
            return currNode.data
        else:
            return -1
    