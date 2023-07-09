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
        
        lastNode = self.tail.next
        
        while lastNode != self.head:
            
            print(lastNode.data)
            lastNode = lastNode.prev

    # add new node to right next to the head
        
    def appendToFirst(self,data):
        
        if self.size == 0:
        
            newNode = Node(data)

            self.head.next = newNode
            newNode.prev = self.head

            self.tail.next = newNode
            self.tail.prev = self.head

            self.size +=1
        else:

            newNode = Node(data)

            firstNode = self.head.next
            self.head.next = newNode
            newNode.prev = self.head
            newNode.next = firstNode
            firstNode.prev = newNode
            self.size +=1

        return 0
    
    # remove the node that contains the same data as given data
    # remember to point to prevNode and nextNode
    
    # Two cases:  when we delete the node other than lastNode
    #             when we delete the lastNode

    def remove(self,data):

        if self.size > 0:
            
            lastNode = self.tail.next

            if lastNode.data == data:

                if lastNode.prev != None:
                    lastNode.prev.next = None
                    self.tail.next = lastNode.prev
                    self.size -= 1
                
            else:

                currNode = self.head
                prevNode = None
                nextNode = None

                while currNode != None:
                    
                    if currNode.data == data:
                        
                        nextNode = currNode.next
                        prevNode.next = nextNode
                        nextNode.prev = prevNode
                        self.size -= 1
                        
                    prevNode = currNode    
                    currNode = currNode.next

        else:
            return -1
        
    
    def appendToEnd(self,data):

        if self.size == 0:
            newNode = Node(data)

            self.head.next = newNode
            newNode.prev = self.head
            self.tail.next = newNode
            self.tail.prev = self.head
            
            self.size += 1

        else:

            lastNode = self.tail.next
            newNode = Node(data)
            lastNode.next = newNode
            newNode.prev = lastNode
            self.tail.next = newNode

            self.size += 1
        
        return 0
        

    # return length of linkedlist
    def legnth(self):

        return self.size

    
    