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
    def front(self,data):
        return 0
    # enqueue element meaning append element to the end of queue
    def enqueue(self,data):
        return 0
    
    # dequeue element meaning remove the first element of queue
    def dequeue(self,data):
        return 0

    #display elements in queue 
    def display(self):
        return 0
    # return the size of queue
    def length(self):

        return 0    
