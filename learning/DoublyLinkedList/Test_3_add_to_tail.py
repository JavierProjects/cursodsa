import unittest
from Node_sandbox import Node
from DoublyLinkedList_sandbox import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):
    
    def test_add_to_tail(self):
        # Crea una lista doblemente enlazada
        linked_list = DoublyLinkedList()
        
        # Agrega un nodo a la cola con valor 10
        linked_list.add_to_tail(10)
        
        # Verifica que el nodo cola tenga el valor correcto
        self.assertEqual(linked_list.tail_node.get_value(), 10, "El valor del nodo cola debe ser 10.")
        
        # Verifica que el nodo cola también sea la cabeza (porque solo hay un nodo)
        self.assertEqual(linked_list.head_node.get_value(), 10, "El nodo cabeza también debe tener el valor 10 porque solo hay un nodo.")
        
        # Agrega otro nodo a la cola con valor 20
        linked_list.add_to_tail(20)
        
        # Verifica que el nuevo nodo cola tenga el valor correcto
        self.assertEqual(linked_list.tail_node.get_value(), 20, "El valor del nuevo nodo cola debe ser 20.")
        
        # Verifica que el nodo previo al nodo cola sea el nodo con valor 10
        self.assertEqual(linked_list.tail_node.get_prev_node().get_value(), 10, "El nodo previo al nodo cola debe tener el valor 10.")
        
        # Verifica que el nodo siguiente del nodo con valor 10 sea el nuevo nodo cola (20)
        self.assertEqual(linked_list.head_node.get_next_node().get_value(), 20, "El siguiente nodo de la cabeza debe tener el valor 20.")
        
if __name__ == '__main__':
    unittest.main()
