import unittest
import start
if start.from_test():
    print("Running from Dr Javier's code")
    from Node import Node    
else:
    print("Running from students' code")
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
