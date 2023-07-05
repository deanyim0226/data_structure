
# linkedlist is a linear data structure in which elements are 
# not stored at contiguous memory locations

# In simple words, it consists of nodes where each node contains a data field 
# and a referecne to the next node in the list.


# we can't have two identical values in the objects /into two differnt objects?
# we can have  the value in multiple objects


"""
singly linked list
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
             head = Node(data)
             node = head.next
             self.size += 1
        
        else:
             
             head = self.head

             while head.next != None:
                  
                  head = head.next
            
        node = Node(data)
        head.next = node
        self.size += 1






    """
    remove data from linked list if the data is not present, throw an error message
    """
       

    def remove(self,data):
        
        removeNode = None
        nextNode = None
        head = self.head

        while head.data != None:
                
            if head.data == data:      
                removeNode = head
                head = head.next
                removeNode = None

        while head.next != None:
             nextNode = head
        
        

        



                  
    
    """
    get data or element associated with a given index from the linked list 
    """
    def getDatabyIndex(self,index):

        ptr=0
        ptr = self.head
        head = self.head.next
        value = self.head.data

        
        while head != None:    
             
             if ptr == index:
                  return value
             
        

             
             
    
    """
    return the size of linked list
    """

    def size(self):

        sizeOflist = 0
        self.sizeOflist = self.size
        return sizeOflist
    
    """
    display all the elements in linked list 
    """
    def display(self):    
        
        display = self.head

        while display != None:
             print(display.data) 

             display = self.head.next





