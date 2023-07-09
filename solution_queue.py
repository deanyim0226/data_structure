class Node:

    def __init__(self,data =None) -> None:
        self.data = data
        self.next = None
        pass

class Queue:
    def __init__(self) -> None:
        
        self.head = Node()
        self.tail = Node()
        self.size = 0

        pass

    # return the first element in queue without removing
    def peak(self):

        if self.size > 0 :
            
            return self.head.data
        else:
            return -1
    # enqueue element meaning append element to the end of queue
    def enqueue(self,data):
        
        newNode = Node(data)

        if self.size == 0:

            self.head = newNode
            self.tail = newNode
    
            self.size += 1
        else:

            lastNode = self.tail
            lastNode.next = newNode
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
                nextNode = firstNode.next
                self.head = nextNode

                self.size -= 1

                return firstNode.data
        else:

            return -1

    #display elements in queue 
    def display(self):

        currNode = self.head

        while currNode:
            print(currNode.data)
            currNode = currNode.next
        
    # return the size of queue
    def length(self):

        return self.size    
