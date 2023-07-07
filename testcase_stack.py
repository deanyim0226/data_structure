import unittest
import stack

class TEST(unittest.TestCase):
    def setUp(self):
        self.ex = [1,4,5,7,8]
        self.stack = stack.Stack() 
        pass

    def tearDown(self):
        pass    
    
    def test_empty(self):

        output = self.stack.isEmpty()
        expectedOutput = True
        self.assertEqual(output,expectedOutput)

        self.stack.push(1)
        output = self.stack.isEmpty()
        expectedOutput = False
        self.assertEqual(output,expectedOutput)

    def test_push(self):

        self.stack.push(1)
        self.stack.push(4)
        self.stack.push(5)
        self.stack.push(7)
        self.stack.push(8)

        index = len(self.ex) -1
        output = True
        expectedOutput = True

        while not self.stack.isEmpty():
            
            data = self.stack.peek()

            if data != self.ex[index]:
                expectedOutput = False
            
            self.stack.pop()
            index -= 1

        self.assertEqual(output,expectedOutput)

    def test_peek(self):

        self.stack.push(1)
        output = self.stack.peek()
        expectedOutput = self.ex[0]
        self.assertEqual(output,expectedOutput)

        self.stack.push(4)
        output = self.stack.peek()
        expectedOutput = self.ex[1]
        self.assertEqual(output,expectedOutput)

    def test_pop(self):

        self.stack.push(1)
        self.stack.push(4)
        self.stack.push(5)
        self.stack.push(7)
        self.stack.push(8)

        output = self.stack.peek()
        self.stack.pop()
        expectedOutput = self.ex[-1]
        self.assertEqual(output,expectedOutput)

        output = self.stack.peek()
        self.stack.pop()
        expectedOutput = self.ex[-2]
        self.assertEqual(output,expectedOutput)

        output = self.stack.peek()
        self.stack.pop()
        expectedOutput = self.ex[-3]
        self.assertEqual(output,expectedOutput)

        output = self.stack.peek()
        self.stack.pop()
        expectedOutput = self.ex[-4]
        self.assertEqual(output,expectedOutput)

        output = self.stack.peek()
        self.stack.pop()
        expectedOutput = self.ex[-5]
        self.assertEqual(output,expectedOutput)

    

if __name__ == "__main__":
    unittest.main()