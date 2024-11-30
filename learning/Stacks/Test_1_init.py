import unittest
from Node import Node 
import start
if start.from_test():
    print("Running from Dr Javier's code")
    from stack import Stack
else:
    print("Running from students' code")
    from stack_sandbox import Stack



class TestStack(unittest.TestCase):
    def setUp(self):
        """Set up a stack instance for testing."""
        self.stack = Stack()

    def test_peek_empty_stack(self):
        """Test peek on an empty stack."""
        with self.assertRaises(AttributeError):
            self.stack.peek()  # Should raise an error because top_item is None

    def test_peek_single_element(self):
        """Test peek on a stack with a single element."""
        # Create a single node and assign it as the top_item
        node = Node(10)
        self.stack.top_item = node
        self.assertEqual(self.stack.peek(), 10)  # Peek should return the node's value

    def test_peek_multiple_elements(self):
        """Test peek when multiple nodes are added manually to the stack."""
        # Manually link nodes
        node1 = Node(10)
        node2 = Node(20)
        node2.set_next_node(node1)  # Node2 points to Node1
        self.stack.top_item = node2  # Top item is Node2

        # Peek should always return the value of the top_item
        self.assertEqual(self.stack.peek(), 20)

if __name__ == '__main__':
    unittest.main()
