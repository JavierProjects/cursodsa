import unittest
from Node import Node
from LinkedList_sandbox import LinkedList

class TestLinkedListStringify(unittest.TestCase):
    
    def test_stringify_list(self):
        linked_list = LinkedList("Nodo 1")
        linked_list.insert_beginning("Nodo 2")
        linked_list.insert_beginning("Nodo 3")
        
        expected_output = "Nodo 3\nNodo 2\nNodo 1\n"
        self.assertEqual(linked_list.stringify_list(), expected_output, "La lista no fue convertida correctamente en una cadena.")
    
if __name__ == '__main__':
    unittest.main()
