
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
        # your job is to implement stack data structure by using linkedlist

    def __init__(self):
        # add your instance variables
        
        self.head = Node()
        self.size = 0
    
        pass

        # add an element to the top of a stack 

    def push(self, element):

        

        if self.size == 0:
           node = Node(element)
           self.head = node
           self.size += 1
        
        else:
            head = self.head

            while head.next is not None:
                head = head.next

            node = Node(element)
            head.next = node
            self.size += 1
        
        # remove an element from the top of a stack
        # when you are trying to pop more than the size of stack
        # then you should throw an error 

    def pop(self):

       curNode = self.head
       popNode = None

       if self.size > 0:
            
            if self.size == 1:
                self.head = None
                self.size -= 1

            
            else:

                while curNode is not None:
                
                
                    if curNode.next is None:
                        popNode.next = None
                        self.size -= 1

                    popNode = curNode
                    curNode = curNode.next     

                
                        
                     

            

        # check whether the stack is empty or not
        # if stack is empty return True else return False

    def isEmpty(self):

        if self.size == 0:
            return True
        else:
            return False
        

        # get the value of the top element without removing it
        # if stack is empty, then return -1
    def peek(self):
        
        curNode = self.head

        if self.size == 0:

            return -1
        
        else:
            
            while curNode is not None:

                if curNode.next is None:
                    
                    return curNode.data
                
                curNode = curNode.next
                

        


    
