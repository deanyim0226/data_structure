# queue is a linear data structure that the operations are performed in First In First Out. aka (FIFO) order

"""
queue can be visiualized as a drawing below

-pointer "next" is denoted as "->" 
-NULL is the same as NONE

|---DATA---| -> |---DATA---|  ->  |---DATA---|-> NULL
|----------|    |----------|      |----------|
|----------|    |----------|      |----------|
    HEAD                              TAIL

"""        
class Node:

    def __init__(self,data = None):
        self.data = data
        self.next = None
        pass

class Queue:
    def __init__(self):
        
        self.head = Node()
        self.tail = Node()
        self.size = 0

        pass
        
  # return the first element in queue without removing

    def peak(self):

        firstNode = self.head

        if self.size > 0:
            return firstNode.data
        
        else:
            -1
    
    # enqueue element meaning append element to the end of queue

    def enqueue(self,data):
      

        if self.size == 0:
            newNode = Node(data)
            self.head = newNode
            self.tail = newNode

            self.size += 1
            
        
        else:
            newNode = Node(data)
            tailNode = self.tail
            tailNode.next = newNode
            self.tail = newNode
                
            self.size += 1
                

    
    # dequeue element meaning remove the first element of queue
    def dequeue(self):
          
        if self.size > 0:

            if self.size == 1:

                firstNode = self.head   
                self.head = None
                self.tail = None
                self.size -= 1

                return firstNode.data
                
      

            else:
                    
                firstNode = self.head
                self.head = firstNode.next
                self.size -= 1

                return firstNode.data
        
        else:
            return -1

            

                    

    #display elements in queue 
    def display(self):
        
        node = self.head

        while node:
            print(node.data)

        node = node.next

    
    # return the size of queue
    def length(self):

        return self.size
