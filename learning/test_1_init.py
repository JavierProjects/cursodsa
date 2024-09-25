import unittest
from Node_sandbox import Node

class TestNodeInit(unittest.TestCase):
    def test_class_exists(self):
        # Test if Node class exists and is of the correct type
        try:
            self.assertTrue(issubclass(Node, object))
        except NameError:
            self.fail("Did you define a class called `Node`?")
    
    def test_node_initialization(self):
        # Test if Node initializes with a value and next_node
        node = Node(3)
        self.assertEqual(node.value, 3)
        self.assertIsNone(node.next_node)

if __name__ == '__main__':
    unittest.main()
