import unittest
import start
if start.from_test():
    print("Running from Dr Javier's code")
    from stack import Stack
else:
    print("Running from students' code")
    from stack_sandbox import Stack

    
class TestStackMethods(unittest.TestCase):
    def setUp(self):
        """Set up an instance of Stack for testing."""
        self.stack = Stack()

    def test_push_single_element(self):
        """Test pushing a single element onto the stack."""
        self.stack.push(10)
        self.assertEqual(self.stack.peek(), 10)  # The top item should be 10

    def test_push_multiple_elements(self):
        """Test pushing multiple elements onto the stack."""
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)
        self.assertEqual(self.stack.peek(), 30)  # The top item should be 30

    def test_pop_single_element(self):
        """Test popping a single element from the stack."""
        self.stack.push(10)
        popped_value = self.stack.pop()
        self.assertEqual(popped_value, 10)  # Popped value should be 10
        with self.assertRaises(AttributeError):
            self.stack.peek()  # Stack is now empty, so peek should raise an error

    def test_pop_multiple_elements(self):
        """Test popping multiple elements from the stack."""
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)

        popped_value = self.stack.pop()
        self.assertEqual(popped_value, 30)  # The top item should be 30
        self.assertEqual(self.stack.peek(), 20)  # New top should be 20

        popped_value = self.stack.pop()
        self.assertEqual(popped_value, 20)  # The top item should be 20
        self.assertEqual(self.stack.peek(), 10)  # New top should be 10

        popped_value = self.stack.pop()
        self.assertEqual(popped_value, 10)  # The top item should be 10

        with self.assertRaises(AttributeError):
            self.stack.peek()  # Stack should now be empty

    def test_push_and_pop_combined(self):
        """Test combining push and pop operations."""
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.pop(), 20)  # Pop should return 20
        self.stack.push(30)
        self.assertEqual(self.stack.peek(), 30)  # Top should now be 30
        self.assertEqual(self.stack.pop(), 30)  # Pop should return 30
        self.assertEqual(self.stack.pop(), 10)  # Pop should return 10
        with self.assertRaises(AttributeError):
            self.stack.peek()  # Stack should now be empty

if __name__ == '__main__':
    unittest.main()
