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

    def front(self,data):

        firstNode = self.head.next

        if firstNode.data is data:
            return firstNode.data

        


    def peek(self):

        return 0
    # enqueue element meaning append element to the end of queue

    def enqueue(self,data):
        size = self.size

        if size == 0:
            newNode = Node(data)
            self.head.next = newNode
            self.tail.prev = newNode
            self.tail.next = self.head

            size += 1
        
        else:

            currNode = self.head.next
            newNode = Node(data)

            if newNode.data == data:
                self.head.next = newNode
                newNode.next = currNode
                self.tail.prev = currNode
                self.tail.next = newNode
            

        return 0
    
    # dequeue element meaning remove the first element of queue
    def dequeue(self):
        size = self.size
        currNode = self.head.next
        
        if size == 0:
            currNode = None
        
        else:
            while currNode:
                if self.tail.prev:
                    lastNode = self.tail.prev
                    temp = lastNode.prev
                    lastNode = None
                    size -= 1
                    self.tail.prev = temp
                    self.tail.next = self.head
                    

        return 0

    #display elements in queue 
    def display(self):
        size = self.size
        currNode = self.head

        if size == 0:
            return None
        else:
            while currNode.next is not None:
                self.tail.prev = currNode
                currNode = currNode.next
                self.tail.next = self.head
                print(currNode)
                currNode = self.head
            
        return 0
    # return the size of queue
    def length(self):
        size = self.size
        currNode = self.head

        while currNode.next is not None:
            currNode = currNode.next
            size += 1

        return size    
