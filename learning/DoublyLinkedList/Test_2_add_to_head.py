import unittest
from Node_sandbox import Node
from DoublyLinkedList_sandbox import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):
    
    def test_init(self):
        # Verifica que al inicializar, la lista esté vacía (sin cabeza ni cola)
        linked_list = DoublyLinkedList()
        self.assertIsNone(linked_list.head_node, "El nodo cabeza debe ser None al inicializar la lista.")
        self.assertIsNone(linked_list.tail_node, "El nodo cola debe ser None al inicializar la lista.")
    
    def test_add_to_head(self):
        # Crea una lista doblemente enlazada
        linked_list = DoublyLinkedList()
        
        # Agrega un nodo a la cabeza con valor 10
        linked_list.add_to_head(10)
        
        # Verifica que el nodo cabeza tenga el valor correcto
        self.assertEqual(linked_list.head_node.get_value(), 10, "El valor del nodo cabeza debe ser 10.")
        
        # Verifica que el nodo cabeza también sea la cola (porque solo hay un nodo)
        self.assertEqual(linked_list.tail_node.get_value(), 10, "El nodo cola también debe tener el valor 10 porque solo hay un nodo.")
        
        # Agrega otro nodo a la cabeza con valor 20
        linked_list.add_to_head(20)
        
        # Verifica que el nuevo nodo cabeza tenga el valor correcto
        self.assertEqual(linked_list.head_node.get_value(), 20, "El valor del nuevo nodo cabeza debe ser 20.")
        
        # Verifica que el nodo siguiente al nodo cabeza tenga el valor del nodo anterior (10)
        self.assertEqual(linked_list.head_node.get_next_node().get_value(), 10, "El siguiente nodo de la cabeza debe tener el valor 10.")
        
        # Verifica que el nodo previo del nodo anterior (10) sea el nuevo nodo cabeza (20)
        self.assertEqual(linked_list.head_node.get_next_node().get_prev_node().get_value(), 20, "El nodo previo del nodo 10 debe ser el nodo cabeza con valor 20.")

if __name__ == '__main__':
    unittest.main()
