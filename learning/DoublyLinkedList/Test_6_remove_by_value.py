import unittest
from Node_sandbox import Node
from DoublyLinkedList_sandbox import DoublyLinkedList

class TestDoublyLinkedListRemoveByValue(unittest.TestCase):

    def setUp(self):
        self.doubly_linked_list = DoublyLinkedList()

    def test_remove_by_value_head(self):
        # Caso de prueba eliminando el nodo cabeza
        self.doubly_linked_list.add_to_tail(10)
        self.doubly_linked_list.add_to_tail(20)
        self.doubly_linked_list.add_to_tail(30)

        removed_node = self.doubly_linked_list.remove_by_value(10)
        self.assertEqual(removed_node.get_value(), 10, "El valor eliminado debería ser 10.")
        self.assertEqual(self.doubly_linked_list.head_node.get_value(), 20, "El nuevo nodo cabeza debería ser 20.")

    def test_remove_by_value_tail(self):
        # Caso de prueba eliminando el nodo cola
        self.doubly_linked_list.add_to_tail(10)
        self.doubly_linked_list.add_to_tail(20)
        self.doubly_linked_list.add_to_tail(30)

        removed_node = self.doubly_linked_list.remove_by_value(30)
        self.assertEqual(removed_node.get_value(), 30, "El valor eliminado debería ser 30.")
        self.assertEqual(self.doubly_linked_list.tail_node.get_value(), 20, "El nuevo nodo cola debería ser 20.")

    def test_remove_by_value_middle(self):
        # Caso de prueba eliminando un nodo intermedio
        self.doubly_linked_list.add_to_tail(10)
        self.doubly_linked_list.add_to_tail(20)
        self.doubly_linked_list.add_to_tail(30)

        removed_node = self.doubly_linked_list.remove_by_value(20)
        self.assertEqual(removed_node.get_value(), 20, "El valor eliminado debería ser 20.")
        self.assertEqual(self.doubly_linked_list.head_node.get_next_node().get_value(), 30, "El nodo siguiente debería ser 30.")
        self.assertEqual(self.doubly_linked_list.tail_node.get_prev_node().get_value(), 10, "El nodo anterior de la cola debería ser 10.")

    def test_remove_by_value_not_found(self):
        # Caso de prueba cuando el valor no se encuentra
        self.doubly_linked_list.add_to_tail(10)
        self.doubly_linked_list.add_to_tail(20)

        removed_node = self.doubly_linked_list.remove_by_value(30)  # 30 no está en la lista
        self.assertIsNone(removed_node, "Debería devolver None si el valor no está en la lista.")

    def test_remove_by_value_empty_list(self):
        # Caso de prueba con una lista vacía
        removed_node = self.doubly_linked_list.remove_by_value(10)
        self.assertIsNone(removed_node, "Debería devolver None si la lista está vacía.")

if __name__ == '__main__':
    unittest.main()
