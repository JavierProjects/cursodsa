import unittest
from Node_sandbox import Node

class TestNodeGetters(unittest.TestCase):
    def test_get_value(self):
        node = Node(3)
        self.assertEqual(node.get_value(), 3)
    
    def test_get_next_node(self):
        node = Node(3)
        self.assertIsNone(node.get_next_node())

if __name__ == '__main__':
    unittest.main()
