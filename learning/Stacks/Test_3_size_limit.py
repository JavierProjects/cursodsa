import unittest
import start
if start.from_test():
    print("Running from Dr Javier's code")
    from stack import Stack
else:
    print("Running from students' code")
    from stack_sandbox import Stack
    
    
class TestStack(unittest.TestCase):
    def setUp(self):
        """Set up a Stack instance for testing."""
        self.stack = Stack(limit=3)

    def test_push_within_limit(self):
        """Test pushing elements within the stack limit."""
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)
        self.assertEqual(self.stack.peek(), 30)  # Top should be 30
        self.assertEqual(self.stack.size, 3)  # Size should be 3

    def test_push_beyond_limit(self):
        """Test pushing elements beyond the stack limit."""
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)
        with self.assertLogs() as log:
            self.stack.push(40)  # Exceeding the limit
            self.assertIn("La pila esta llena ¡No queda espacio!", log.output[0])  # Expect a warning
        self.assertEqual(self.stack.peek(), 30)  # Top should still be 30
        self.assertEqual(self.stack.size, 3)  # Size should not increase

    def test_pop_within_limit(self):
        """Test popping elements within the stack."""
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)
        self.assertEqual(self.stack.pop(), 30)  # Pop should return 30
        self.assertEqual(self.stack.size, 2)  # Size should decrease
        self.assertEqual(self.stack.peek(), 20)  # Top should now be 20

    def test_pop_until_empty(self):
        """Test popping all elements until the stack is empty."""
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)
        self.stack.pop()
        self.stack.pop()
        self.stack.pop()
        with self.assertLogs() as log:
            result = self.stack.pop()  # Stack is empty now
            self.assertIsNone(result)  # Pop should return None
            self.assertIn("La pila esta totalmente vacia!", log.output[0])  # Expect a warning
        self.assertEqual(self.stack.size, 0)  # Size should be 0

    def test_peek_empty_stack(self):
        """Test peek on an empty stack."""
        with self.assertLogs() as log:
            result = self.stack.peek()
            self.assertIsNone(result)  # Peek should return None
            self.assertIn("La pila esta totalmente vacia!", log.output[0])  # Expect warning

    def test_has_space(self):
        """Test the has_space() method."""
        self.assertTrue(self.stack.has_space())  # Initially, should have space
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)
        self.assertFalse(self.stack.has_space())  # No space after reaching limit

    def test_is_empty(self):
        """Test the is_empty() method."""
        self.assertTrue(self.stack.is_empty())  # Initially, stack should be empty
        self.stack.push(10)
        self.assertFalse(self.stack.is_empty())  # Should not be empty after push
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())  # Should be empty after popping all elements

if __name__ == '__main__':
    unittest.main()
