import unittest
import start
if start.from_test():
    print("Running from Dr Javier's code")
    from Queue import Queue
else:
    print("Running from students' code")
    from queue_sandbox import Queue

class TestQueueEnqueue(unittest.TestCase):
    def setUp(self):
        """Set up test cases with an empty queue and a queue with max size."""
        self.empty_queue = Queue()
        self.queue_with_limit = Queue(max_size=3)
        self.queue_with_limit.enqueue(1)
        self.queue_with_limit.enqueue(2)

    def test_enqueue_empty_queue(self):
        """Test enqueue on an empty queue."""
        self.empty_queue.enqueue(10)
        self.assertEqual(self.empty_queue.peek(), 10)
        self.assertEqual(self.empty_queue.get_size(), 1)
        self.assertFalse(self.empty_queue.is_empty())

    def test_enqueue_non_empty_queue(self):
        """Test enqueue on a non-empty queue."""
        self.queue_with_limit.enqueue(3)
        self.assertEqual(self.queue_with_limit.peek(), 1)  # Head should remain the same
        self.assertEqual(self.queue_with_limit.get_size(), 3)

    def test_enqueue_full_queue(self):
        """Test enqueue on a queue at maximum capacity."""
        self.queue_with_limit.enqueue(3)  # Fill the queue
        self.assertEqual(self.queue_with_limit.get_size(), 3)
        self.assertFalse(self.queue_with_limit.has_space())

        # Attempt to enqueue another element
        with self.assertLogs() as log:
            self.queue_with_limit.enqueue(4)
            self.assertIn("¡Lo sentimos, no hay más espacio!", log.output[0])
        self.assertEqual(self.queue_with_limit.get_size(), 3)  # Size should remain unchanged

    def test_enqueue_no_max_size(self):
        """Test enqueue on a queue with no maximum size."""
        unlimited_queue = Queue()
        for i in range(1, 11):
            unlimited_queue.enqueue(i)
        self.assertEqual(unlimited_queue.get_size(), 10)
        self.assertTrue(unlimited_queue.has_space())  # Always has space with no limit
        self.assertEqual(unlimited_queue.peek(), 1)  # First element remains the head

if __name__ == '__main__':
    unittest.main()
