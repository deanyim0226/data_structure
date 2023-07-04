
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
        return 0
    
    """
    remove data from linked list if the data is not present, throw an error message
    """

    def remove(self,data):
        return 0
    
    """
    get data or element associated with a given index from the linked list 
    """
    def getDatabyIndex(self,index):
        return 0
    
    """
    return the size of linked list
    """

    def size(self):
        return 0
    
    """
    display all the elements in linked list 
    """
    def display(self):    
        return 0

