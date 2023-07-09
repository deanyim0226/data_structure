import unittest
import solution_doublyLinkedlist

class Test(unittest.TestCase):

    def setUp(self):
        self.ex = [None,1,4,5,7,8]
        self.linkedList = solution_doublyLinkedlist.Linkedlist()
        pass

    def tearDown(self):
        pass
    

    def testAppendToEnd(self):

        self.linkedList.appendToEnd(1)
        self.linkedList.appendToEnd(4)
        self.linkedList.appendToEnd(5)
        self.linkedList.appendToEnd(7)
        self.linkedList.appendToEnd(8)
        self.linkedList.appendToFirst(10)

        self.linkedList.remove(1)

        self.linkedList.displayFromFirstElement()
        print("-----------------------------------")
        self.linkedList.displayFromLastElement()
    
if __name__ == "__main__":
    unittest.main()