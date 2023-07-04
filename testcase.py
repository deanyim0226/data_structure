# linkedlist is a linear data structure in which elements are 
# not stored at contiguous memory locations

# In simple words, it consists of nodes where each node contains a data field 
# and a referecne to the next node in the list.

 
class Node:
    
    def __init__(self,data = None) -> None:
        self.data = data
        self.next = None

class Linkedlist:

    def __init__(self) -> None:
        self.head = Node()
        self.size = 0

    def append(self,data):

        if self.size == 0:
            
            node = Node(data)
            self.head = node
            self.size += 1

        else:
            
            head = self.head

            while head.next != None:

                head = head.next
            
            node = Node(data)
            head.next = node

            self.size += 1

    def remove(self,value):

        """"
        head = self.head
        prevNode = None

        while head != None:

            if head.data == value:
                prevNode.next = None

            prevNode = head    
            head = head.next

        
          if self.head.data == value:
        
            self.head = self.head.next
        
    
      head = self.head
        
        prevNode = None
        nextNode = None

        while head != None:

            if head.data == value:
                "delete the node connect prev node pointer to nextNode"
                nextNode = head.next
                prevNode.next = nextNode
            
            prevNode = head
            head = head.next
        """

    
    def display(self):
        
        temp = self.head
        while temp != None:

            print(temp.data)
            temp= temp.next    
        

########### 1 2 3 ############

