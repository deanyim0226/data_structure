from io import StringIO
import sys
import unittest
import doublyLinkedlist
#import solutions.solution_doublyLinkedlist as solution_doublyLinkedlist

class Test(unittest.TestCase):

    def setUp(self):
        self.ex = [None,1,4,5,7,8]
        self.linkedList = doublyLinkedlist.Linkedlist()
        pass

    def tearDown(self):
        pass
    

    def testAppendToEnd(self):

        self.linkedList.appendToEnd(1)
        self.linkedList.appendToEnd(4)
        self.linkedList.appendToEnd(5)
        self.linkedList.appendToEnd(7)
        self.linkedList.appendToEnd(8)

        head = self.linkedList.head
        expectedOutput = True
        output = True
        index = 0

        while head:
            
            if head.data != self.ex[index]:
                output = False

            index += 1
            head = head.next
        
        self.assertEqual(output,expectedOutput)


    def testAppendToFirst(self):
        self.linkedList.appendToFirst(1)
        self.linkedList.appendToFirst(4)
        self.linkedList.appendToFirst(5)
        self.linkedList.appendToFirst(7)
        self.linkedList.appendToFirst(8)

        head = self.linkedList.head
        expectedOutput = [None,8,7,5,4,1]
        output = []
        
        while head:
            
            output.append(head.data)
            head = head.next


        self.assertEqual(output,expectedOutput)
            
    def testAppendToBoth(self):

        self.linkedList.appendToEnd(1)
        self.linkedList.appendToEnd(3)
        self.linkedList.appendToFirst(4)
        self.linkedList.appendToEnd(5)
        self.linkedList.appendToFirst(8)
        self.linkedList.appendToEnd(10)
        self.linkedList.appendToFirst(9)

        head = self.linkedList.head
        expectedOutput = [None,9,8,4,1,3,5,10]
        output = []

        while head:
            output.append(head.data)
            head = head.next
        
        self.assertEqual(output,expectedOutput)


    def testDisplayFromFirstElement(self):
        
        self.linkedList.appendToFirst(1)
        self.linkedList.appendToEnd(4)
        self.linkedList.appendToFirst(5)
        self.linkedList.appendToEnd(7)
        self.linkedList.appendToFirst(8)

        captured_output = StringIO()
        sys.stdout = captured_output
        
        self.linkedList.displayFromFirstElement()

        # get the value of the captured output
        output = captured_output.getvalue().strip()

        # reset stdout
        sys.stdout = sys.__stdout__

        expected_output = "None\n8\n5\n1\n4\n7"
        self.assertEqual(output,expected_output)


    def testDisplayFromLastElement(self):
       
        self.linkedList.appendToFirst(10)
        self.linkedList.appendToEnd(1)
        self.linkedList.appendToEnd(4)
        self.linkedList.appendToEnd(5)
        self.linkedList.appendToEnd(7)
        self.linkedList.appendToFirst(8)
        
        captured_output = StringIO()
        sys.stdout = captured_output
        
        self.linkedList.displayFromLastElement()

        # get the value of the captured output
        output = captured_output.getvalue().strip()

        # reset stdout
        sys.stdout = sys.__stdout__

        expected_output = "7\n5\n4\n1\n10\n8"

        self.assertEqual(output,expected_output)

    def testRemove(self):

        self.linkedList.appendToEnd(1)
        self.linkedList.appendToEnd(3)
        self.linkedList.appendToFirst(4)
        self.linkedList.appendToEnd(5)
        self.linkedList.appendToFirst(8)
        self.linkedList.appendToEnd(10)
        self.linkedList.appendToFirst(9)


        self.linkedList.remove(9)
        expected_output = [None, 8,4,1,3,5,10]

        head = self.linkedList.head
        output = []
        while head:
            output.append(head.data)
            head = head.next
        
        self.assertEqual(output,expected_output)

        self.linkedList.remove(1)
        expected_output = [None, 8,4,3,5,10]

        head = self.linkedList.head
        output = []
        while head:
            output.append(head.data)
            head = head.next
        
        self.assertEqual(output,expected_output)

        self.linkedList.remove(10)
        expected_output = [None, 8,4,3,5]

        head = self.linkedList.head
        output = []
        while head:
            output.append(head.data)
            head = head.next
        
        self.assertEqual(output,expected_output)

        self.linkedList.remove(4)
        expected_output = [None, 8,3,5]

        head = self.linkedList.head
        output = []
        while head:
            output.append(head.data)
            head = head.next
        
        self.assertEqual(output,expected_output)

        self.linkedList.remove(3)
        expected_output = [None, 8,5]

        head = self.linkedList.head
        output = []
        while head:
            output.append(head.data)
            head = head.next
        
        self.assertEqual(output,expected_output)

        self.linkedList.remove(5)
        expected_output = [None, 8]

        head = self.linkedList.head
        output = []
        while head:
            output.append(head.data)
            head = head.next
        
        self.assertEqual(output,expected_output)

        self.linkedList.remove(10)
        expected_output = [None, 8]

        head = self.linkedList.head
        output = []
        while head:
            output.append(head.data)
            head = head.next
        
        self.assertEqual(output,expected_output)

        self.linkedList.remove(8)
        expected_output = [None]
        
        output = self.linkedList.remove(10)
        expected_output = -1
        self.assertEqual(output,expected_output)
    
    def testLegnth(self):

        self.linkedList.appendToEnd(1)
        self.linkedList.appendToEnd(4)
        self.linkedList.appendToEnd(5)
        self.linkedList.appendToEnd(7)
        self.linkedList.appendToEnd(8)

        output = self.linkedList.size
        expectedOutput = len(self.ex)-1

        self.assertEqual(output,expectedOutput)
        
        
if __name__ == "__main__":
    unittest.main()