import unittest
import start
if start.from_test():
    print("Running from Dr Javier's code")
    from Queue import Queue
else:
    print("Running from students' code")
    from queue_sandbox import Queue


class TestQueueDequeue(unittest.TestCase):
    def setUp(self):
        """Set up test cases with an empty queue and a populated queue."""
        self.empty_queue = Queue()
        self.populated_queue = Queue()
        self.populated_queue.enqueue(1)
        self.populated_queue.enqueue(2)
        self.populated_queue.enqueue(3)

    def test_dequeue_empty_queue(self):
        """Test dequeue on an empty queue."""
        with self.assertLogs() as log:
            result = self.empty_queue.dequeue()
            self.assertIn("¡Esta cola está totalmente vacía!", log.output[0])
        self.assertIsNone(result)  # Should return None for an empty queue
        self.assertEqual(self.empty_queue.get_size(), 0)

    def test_dequeue_single_element(self):
        """Test dequeue on a queue with a single element."""
        single_element_queue = Queue()
        single_element_queue.enqueue(10)
        result = single_element_queue.dequeue()
        self.assertEqual(result, 10)  # Returned value should match the dequeued value
        self.assertTrue(single_element_queue.is_empty())  # Queue should be empty after dequeue
        self.assertEqual(single_element_queue.get_size(), 0)

    def test_dequeue_multiple_elements(self):
        """Test dequeue on a queue with multiple elements."""
        result = self.populated_queue.dequeue()
        self.assertEqual(result, 1)  # Should return the head of the queue
        self.assertEqual(self.populated_queue.get_size(), 2)  # Size should decrease by 1
        self.assertEqual(self.populated_queue.peek(), 2)  # New head should be the next element

    def test_dequeue_until_empty(self):
        """Test dequeuing all elements until the queue is empty."""
        self.assertEqual(self.populated_queue.dequeue(), 1)
        self.assertEqual(self.populated_queue.dequeue(), 2)
        self.assertEqual(self.populated_queue.dequeue(), 3)
        self.assertTrue(self.populated_queue.is_empty())  # Queue should be empty
        self.assertEqual(self.populated_queue.get_size(), 0)
        with self.assertLogs() as log:
            result = self.populated_queue.dequeue()  # Attempt to dequeue from an empty queue
            self.assertIn("¡Esta cola está totalmente vacía!", log.output[0])
        self.assertIsNone(result)  # Should return None

if __name__ == '__main__':
    unittest.main()
