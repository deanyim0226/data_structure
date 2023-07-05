from io import StringIO
import sys
import unittest
import solution_linkedlist


class Test(unittest.TestCase):

    def setUp(self):
        self.ex = [None,1,4,5,7,8]
        self.llist = solution_linkedlist.Linkedlist()
        pass

    def tearDown(self):
        pass


    def test_append(self):
        
        self.llist.append(1)
        self.llist.append(4)
        self.llist.append(5)
        self.llist.append(7)
        self.llist.append(8)

        expected_output = len(self.ex)-1

        output = self.llist.getSize()
        self.assertEqual(output, expected_output)

        head = self.llist.head
        expected_output = []

        output = self.ex
        while head != None:
            expected_output.append(head.data)
            head = head.next
   
        self.assertEqual(output,expected_output)    

    def test_remove(self):

        self.llist.append(1)
        self.llist.append(4)
        self.llist.append(5)
        self.llist.append(7)
        self.llist.append(8)
  
        self.llist.remove(5)
        
        expected_output = [None,1,4,7,8]
        output = []

        head = self.llist.head
        while head != None:
            
            output.append(head.data)
            head = head.next        
            
        self.assertEqual(output, expected_output)


        self.llist.remove(8)

        expected_output = [None,1,4,7]
        output = []

        head = self.llist.head
        while head != None:
            
            output.append(head.data)
            head = head.next        
        self.assertEqual(output, expected_output)

        self.llist.remove(1)

        expected_output = [None,4,7]
        output = []
        
        head = self.llist.head
        while head != None:
            
            output.append(head.data)
            head = head.next        
        self.assertEqual(output, expected_output)


        self.llist.remove(7)
        expected_output = [None,4]
        output = []
        
        head = self.llist.head
        while head != None:
            
            output.append(head.data)
            head = head.next        
        self.assertEqual(output, expected_output)

        self.llist.remove(9)
        expected_output = [None, 4]
        output = []
        
        head = self.llist.head
        while head != None:
            
            output.append(head.data)
            head = head.next        
        self.assertEqual(output, expected_output)
            
    def test_databyIndex(self):
        
        expected_output = 7

        self.llist.append(1)
        self.llist.append(4)
        self.llist.append(5)
        self.llist.append(7)
        self.llist.append(8)

        output = self.llist.getDatabyIndex(4)

        self.assertEqual(output, expected_output)
        
        return 0
    
    def test_display(self):
        
        # Redirect stdout to a stirng buffer
        self.llist.append(1)
        self.llist.append(4)
        self.llist.append(5)
        self.llist.append(7)
        self.llist.append(8)
    
        captured_output = StringIO()
        sys.stdout = captured_output
        
        self.llist.display()

        # get the value of the captured output
        output = captured_output.getvalue().strip()

        # reset stdout
        sys.stdout = sys.__stdout__

        expected_output = "None\n1\n4\n5\n7\n8"
        self.assertEqual(output, expected_output) 

    def test_size(self):
        
        self.llist.append(1)
        self.llist.append(4)
        self.llist.append(5)
        self.llist.append(7)
        self.llist.append(8)

        expected_output = len(self.ex)-1
        output = self.llist.getSize()
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()