import unittest
import start
if start.from_test():
    print("Running from Dr Javier's code")
    from binary_search import binary_search  
else:
    print("Running from students' code")
    from binary_search_sandbox import binary_search  
    

class TestBinarySearch(unittest.TestCase):
    def test_target_found(self):
        sorted_list = [1, 3, 5, 7, 9, 11]
        target = 7
        result = binary_search(sorted_list, target)
        self.assertEqual(result, 3)  # Índice esperado donde se encuentra el 7

    def test_target_not_found(self):
        sorted_list = [1, 3, 5, 7, 9, 11]
        target = 4
        result = binary_search(sorted_list, target)
        self.assertEqual(result, "Valor no encontrado")  # Mensaje cuando no se encuentra el valor

    def test_first_element(self):
        sorted_list = [2, 4, 6, 8, 10]
        target = 2
        result = binary_search(sorted_list, target)
        self.assertEqual(result, 0)  # Índice del primer elemento

    def test_last_element(self):
        sorted_list = [2, 4, 6, 8, 10]
        target = 10
        result = binary_search(sorted_list, target)
        self.assertEqual(result, 4)  # Índice del último elemento

    def test_empty_list(self):
        sorted_list = []
        target = 5
        result = binary_search(sorted_list, target)
        self.assertEqual(result, "Valor no encontrado")  # Búsqueda en lista vacía

    def test_single_element_found(self):
        sorted_list = [7]
        target = 7
        result = binary_search(sorted_list, target)
        self.assertEqual(result, 0)  # Único elemento es el target

    def test_single_element_not_found(self):
        sorted_list = [7]
        target = 5
        result = binary_search(sorted_list, target)
        self.assertEqual(result, "Valor no encontrado")  # Único elemento no es el target

if __name__ == '__main__':
    unittest.main()
