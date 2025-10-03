import unittest
import start
if start.from_test():
    print("Running from Dr Javier's code")
    from Node import Node
    from LinkedList import LinkedList
    from miscellaneous import nth_last_element  
else:
    print("Running from students' code")
    from Node_sandbox import Node
    from LinkedList_sandbox import LinkedList
    from miscellaneous_sandbox import nth_last_element  

class TestNthLastElement(unittest.TestCase):

    def setUp(self):
        """Crear listas enlazadas reutilizables para las pruebas."""
        # LinkedList: 5 -> 4 -> 3 -> 2 -> 1
        self.ll = LinkedList()
        for value in range(1, 6):
            self.ll.insert_beginning(value)

    def test_n_greater_than_length(self):
        """Prueba cuando n es mayor que la longitud de la lista."""
        result = nth_last_element(self.ll, 10)
        self.assertIsNone(result, "Debe devolver None cuando n es mayor que la longitud de la lista")

    def test_n_equals_length(self):
        """Prueba cuando n es igual a la longitud de la lista."""
        result = nth_last_element(self.ll, 5)
        self.assertEqual(result.get_value(), 5, "Debe devolver el primer elemento cuando n es igual a la longitud de la lista")

    def test_typical_case(self):
        """Prueba un caso típico donde n es válido y está dentro de los límites."""
        result = nth_last_element(self.ll, 2)
        self.assertEqual(result.get_value(), 2, "Debe devolver el elemento correcto en la posición n desde el final")

    def test_n_is_one(self):
        """Prueba cuando n es 1 (es decir, el último elemento)."""
        result = nth_last_element(self.ll, 1)
        self.assertEqual(result.get_value(), 1, "Debe devolver el último elemento")

    def test_empty_list(self):
        """Prueba cuando la lista está vacía."""
        empty_ll = LinkedList()
        result = nth_last_element(empty_ll, 1)
        self.assertIsNone(result, "Debe devolver None para una lista vacía")

if __name__ == '__main__':
    unittest.main()
