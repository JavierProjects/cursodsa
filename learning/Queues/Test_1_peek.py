import unittest
import start
if start.from_test():
    print("Running from Dr Javier's code")
    from Node import Node
    from Queue import Queue
else:
    print("Running from students' code")
    from Node_sandbox import Node
    from queue_sandbox import Queue

    
class TestQueue(unittest.TestCase):
    def setUp(self):
        """Set up test cases with an empty queue and a queue with max size."""
        self.empty_queue = Queue()
        self.queue_with_limit = Queue(max_size=3)
        self.queue_with_limit.enqueue(1)
        self.queue_with_limit.enqueue(2)

    def test_is_empty(self):
        """Test the is_empty method."""
        # Empty queue should return True
        self.assertTrue(self.empty_queue.is_empty())
        # Queue with elements should return False
        self.assertFalse(self.queue_with_limit.is_empty())

    def test_has_space(self):
        """Test the has_space method."""
        # Empty queue without limit should have space
        self.assertTrue(self.empty_queue.has_space())
        # Queue with limit should have space when not full
        self.assertTrue(self.queue_with_limit.has_space())
        # Fill the queue and check again
        self.queue_with_limit.enqueue(3)
        self.assertFalse(self.queue_with_limit.has_space())

    def test_get_size(self):
        """Test the get_size method."""
        # Empty queue should return size 0
        self.assertEqual(self.empty_queue.get_size(), 0)
        # Queue with elements should return correct size
        self.assertEqual(self.queue_with_limit.get_size(), 2)
        # Add and remove elements, then check size
        self.queue_with_limit.enqueue(3)
        self.assertEqual(self.queue_with_limit.get_size(), 3)
        self.queue_with_limit.dequeue()
        self.assertEqual(self.queue_with_limit.get_size(), 2)

    def test_peek(self):
        """Test the peek method."""
        # Peeking an empty queue should return None
        self.assertIsNone(self.empty_queue.peek())
        # Peeking a non-empty queue should return the head's value
        self.assertEqual(self.queue_with_limit.peek(), 1)
        # After dequeuing, the next value should be the new head
        self.queue_with_limit.dequeue()
        self.assertEqual(self.queue_with_limit.peek(), 2)

if __name__ == '__main__':
    unittest.main()
