class Node:

    def __init__(self,data = None) -> None:
        self.data = data
        self.next = None
        self.prev = None
        pass


class Linkedlist():


    def __init__(self) -> None:
        
        self.head = Node()
        self.tail = Node()
        self.size = 0
        pass
    
    def displayFromFirstElement(self):

        currNode = self.head

        while currNode:

            print(currNode.data)
            currNode = currNode.next
      
    # display elements in linkedlist from the last element
    
    def displayFromLastElement(self):

        return 0
    
    # add new node to right next to the head
        
    def appendToFirst(self,data):
    
        return 0
    

    # remove the node that contains the same data as given data
    # remember to point to prevNode and nextNode
        
    def remove(self,data):

    
        return 0
    
    def appendToEnd(self,data):

        if self.size == 0:
            node = Node(data)

            self.head.next = node
            node.prev = self.head
            self.tail.next = node
            self.tail.prev = self.head
            
            self.size += 1

        else:

            lastNode = self.tail.next
            node = Node(data)
            lastNode.next = node
            node.prev = lastNode
            self.tail.next = node

            self.size += 1
        
        return 0
        

    # return length of linkedlist
    def legnth(self):

        return 0

    
    