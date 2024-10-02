import unittest
from Node import Node
from LinkedList_sandbox import LinkedList

class TestLinkedListRemove(unittest.TestCase):
    
    def test_remove_node(self):
        linked_list = LinkedList(10)
        linked_list.insert_beginning(20)
        linked_list.insert_beginning(30)

        # Eliminar nodo de enmedio
        linked_list.remove_node(20)
        self.assertNotIn(str(20), linked_list.stringify_list(), "El nodo no fue eliminado correctamente.")
        
        # Eliminar nodo cabeza
        linked_list.remove_node(30)
        self.assertNotIn(str(30), linked_list.stringify_list(), "El nodo cabeza no fue eliminado correctamente.")
    
if __name__ == '__main__':
    unittest.main()
