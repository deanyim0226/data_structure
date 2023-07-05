
# linkedlist is a linear data structure in which elements are 
# not stored at contiguous memory locations

# In simple words, it consists of nodes where each node contains a data field 
# and a referecne to the next node in the list.

"""
singly linked list can be visiualized as image below

ex)  
pointer next is denoted as -> 

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
             
             tempHead = self.head

             while tempHead.next:                      
                tempHead = tempHead.next

             newNode = Node(data)
             tempHead.next = newNode
             self.size += 1

    
    """
    remove data from linked list if the data is not present, leave it as it is
    """

    def remove(self,data):
  
        prevNode = None
        nextNode = None
        tempHead = self.head

        while tempHead:
             
            if tempHead.data == data:

                if prevNode == None:

                    nextNode = tempHead.next
                    self.head = nextNode
                    self.size -=1
                    break

                elif tempHead.next == None:
                    
                    prevNode.next = None
                    self.size -=1
                    break
                else:
                    nextNode = tempHead.next
                    prevNode.next = nextNode
                    self.size -=1
                    break

            prevNode = tempHead
            tempHead = tempHead.next

  
    
    """
    get data or element associated with a given index from the linked list 
    """
    def getDatabyIndex(self,index):
        return 7
    
    """
    return the size of linked list
    """

    def getSize(self):

        return self.size
    
    """
    display all the elements in linked list 
    """
    def display(self):    
        
        a = 5
        test1 = [1,4,5,7,8]

        for i in range(len(test1)):
             
             print(test1[i])
        

