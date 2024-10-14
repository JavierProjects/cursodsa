import unittest
import start
if start.from_test():
    print("Running from Dr Javier's code")
    from Node import Node
    from LinkedList import LinkedList
else:
    print("Running from students' code")
    from Node_sandbox import Node
    from LinkedList_sandbox import LinkedList
    

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        # Inicializar una LinkedList y agregar algunos elementos para cada prueba
        self.ll = LinkedList()
        self.ll.insert_beginning(10)
        self.ll.insert_beginning(20)
        self.ll.insert_beginning(30)
        self.ll.insert_beginning(40)
    
    def test_swap_nodes_existing_elements(self):
        # Probar intercambio de nodos que existen en la lista (30 y 10)
        self.ll.swap_nodes(30, 10)
        resultado_esperado = "40\n10\n20\n30\n"
        self.assertEqual(self.ll.stringify_list(), resultado_esperado, "Error: Intercambio entre 30 y 10 fallido")

    def test_swap_head_with_another_node(self):
        # Probar intercambio del nodo cabeza con otro nodo (40 y 20)
        self.ll.swap_nodes(40, 20)
        # Actualizar el resultado esperado
        resultado_esperado = "20\n30\n40\n10\n"
        self.assertEqual(self.ll.stringify_list(), resultado_esperado, "Error: Intercambio entre 40 y 20 fallido")

    def test_swap_nonexistent_elements(self):
        # Probar intercambio de nodos que no existen en la lista (50 y 60)
        self.ll.swap_nodes(50, 60)
        resultado_esperado = "40\n30\n20\n10\n"
        self.assertEqual(self.ll.stringify_list(), resultado_esperado, "Error: Intercambio con elementos inexistentes fallido")
    
    def test_swap_identical_elements(self):
        # Probar intercambio de nodos idénticos (10 y 10)
        self.ll.swap_nodes(10, 10)
        resultado_esperado = "40\n30\n20\n10\n"
        self.assertEqual(self.ll.stringify_list(), resultado_esperado, "Error: Intercambio de elementos idénticos fallido")

if __name__ == '__main__':
    unittest.main()
