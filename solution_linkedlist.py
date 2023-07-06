
# linkedlist is a linear data structure in which elements are 
# not stored at contiguous memory locations

# In simple words, it consists of nodes where each node contains a data field 
# and a referecne to the next node in the list.

"""
singly linked list can be visiualized as a drawing below

ex)

-pointer "next" is denoted as "->" 
-NULL is the same as NONE

HEAD -> |---DATA---| -> |---DATA---|  ->  |---DATA---|-> NULL
        |----------|    |----------|      |----------|
        |----------|    |----------|      |----------|
 
"""

class Node():
    def __init__(self, data = None):
            self.data = data
            self.next = None


class Linkedlist():
      
    def __init__(self):
            self.head = Node()
            self.size = 0

    """
    append data into linked list 
    """
    def append(self,data):
        
        if self.size == 0:
             
             newNode = Node(data)
             self.head.next = newNode
             self.size += 1
            
        else:
             
             currNode = self.head

             while currNode.next:                      
                currNode = currNode.next

             newNode = Node(data)
             currNode.next = newNode
             self.size += 1

    
    """
    remove data from linked list if the data is not present, leave it as it is
    """

    def remove(self,data):
  
        prevNode = None
        nextNode = None
        currNode = self.head

        while currNode:
             
            if currNode.data == data:

                if prevNode == None:

                    nextNode = currNode.next
                    self.head = nextNode
                    self.size -=1
                    break

                elif currNode.next == None:
                    
                    prevNode.next = None
                    self.size -=1
                    break
                else:
                    nextNode = currNode.next
                    prevNode.next = nextNode
                    self.size -=1
                    break

            prevNode = currNode
            currNode = currNode.next

  
    
    """
    assume index start from 1 in linkedlist
    get data or element associated with a given index from the linked list 
    if index is less than 0 or greater than the length of linkedlist, return 0
    """
    def getDatabyIndex(self,index):

        count = 0 

        currNode = self.head

        while currNode:
             
             if index == count:
                 return currNode.data
              
             count += 1
             currNode = currNode.next

        return 0
    
    """
    return the size of linked list
    """

    def getSize(self):

        return self.size
    
    """
    display all the elements in linked list 
    """
    def display(self):    
                
        currNode = self.head

        while currNode:
             
           
            print(currNode.data)
            currNode = currNode.next

        

