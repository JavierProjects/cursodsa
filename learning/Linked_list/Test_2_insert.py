import unittest
from Node import Node
from LinkedList_sandbox import LinkedList

class TestLinkedListInsert(unittest.TestCase):
    
    def test_insert_beginning(self):
        # Verificar si insert_beginning coloca un nuevo nodo en el inicio
        linked_list = LinkedList("Primero")
        linked_list.insert_beginning("Nuevo")
        self.assertEqual(linked_list.get_head_node().get_value(), "Nuevo", "No se insertó correctamente el nodo al principio.")
        self.assertEqual(linked_list.get_head_node().get_next_node().get_value(), "Primero", "El nodo anterior no fue enlazado correctamente.")
    
if __name__ == '__main__':
    unittest.main()
