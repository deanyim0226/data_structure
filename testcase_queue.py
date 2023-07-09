import unittest
import solution_queue

class Test(unittest.TestCase):
    def setUp(self):
        self.ex = [1,4,5,7,8]
        self.queue = solution_queue.Queue()
        pass

    def tearDown(self):
        pass
    
    # enqueue element meaning append element to the end of queue
    def testEnqueue(self):
        
        self.queue.enqueue(1)
        self.queue.enqueue(4)
        self.queue.enqueue(5)
        self.queue.enqueue(7)
        self.queue.enqueue(8)

        output = self.queue.length()
        expectedOutput = len(self.ex)
        self.assertEqual(output, expectedOutput) 

        head = self.queue.head
        output = self.ex
        expectedOutput = []

        while head:
            
            expectedOutput.append(head.data)
            head = head.next

        self.assertEqual(output,expectedOutput)

    def testPeak(self):
        
        self.queue.enqueue(1)
        output = self.queue.peak()
        expectedOutput = self.ex[0]   
        self.assertEqual(output,expectedOutput)

        self.queue.enqueue(4)
        output = self.queue.peak()
        expectedOutput = self.ex[0]
        self.assertEqual(output,expectedOutput)

        self.queue.enqueue(5)
        output = self.queue.peak()
        expectedOutput = self.ex[0]
        self.assertEqual(output,expectedOutput)

    # dequeue element meaning remove the first element of queue
    def testDequeue(self):

        self.queue.enqueue(1)
        output = self.queue.dequeue()
        expectedOutput = self.ex[0]
        self.assertEqual(output,expectedOutput)

        self.queue.enqueue(4)
        output = self.queue.dequeue()
        expectedOutput = self.ex[1]
        self.assertEqual(output,expectedOutput)

        self.queue.enqueue(1)
        self.queue.enqueue(4)
        self.queue.enqueue(5)
        self.queue.enqueue(7)
        self.queue.enqueue(8)

        output = []
        expectedOutput = self.ex

        while self.queue.size != 0:
            value = self.queue.dequeue()
            output.append(value)

        self.assertEqual(output,expectedOutput)

    # return the size of queue
    def testLength(self):
        
        self.queue.enqueue(1)
        self.queue.enqueue(4)
        self.queue.enqueue(5)
        self.queue.enqueue(7)
        self.queue.enqueue(8)
        output = self.queue.length()
        expectedOutput = len(self.ex)

        self.assertEqual(output,expectedOutput)

if __name__ == "__main__":
    unittest.main()

