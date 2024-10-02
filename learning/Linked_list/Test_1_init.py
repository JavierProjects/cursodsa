import unittest
from Node import Node
from LinkedList_sandbox import LinkedList

class TestLinkedList(unittest.TestCase):

    def test_linkedlist_init(self):
        # Verificar si se inicializa correctamente con el valor de nodo cabeza
        linked_list = LinkedList(5)
        self.assertEqual(linked_list.get_head_node().get_value(), 5, "El nodo cabeza no fue inicializado correctamente.")
    
    def test_get_head_node(self):
        linked_list = LinkedList("Inicio")
        head_node = linked_list.get_head_node()
        self.assertIsNotNone(head_node, "El nodo cabeza no debería ser None.")
        self.assertEqual(head_node.get_value(), "Inicio", "El valor del nodo cabeza no es correcto.")

if __name__ == '__main__':
    unittest.main()
