import unittest
from Node_sandbox import Node

class TestNode(unittest.TestCase):

    def setUp(self):
        # Configuración inicial de nodos para las pruebas
        self.node1 = Node("Primero")
        self.node2 = Node("Segundo")
        self.node3 = Node("Tercero")

    def test_initial_values(self):
        # Verificar que los valores iniciales sean correctos
        self.assertEqual(self.node1.get_value(), "Primero")
        self.assertIsNone(self.node1.get_next_node())
        self.assertIsNone(self.node1.get_prev_node())

    def test_set_next_node(self):
        # Probar el método set_next_node y verificar el enlace
        self.node1.set_next_node(self.node2)
        self.assertEqual(self.node1.get_next_node(), self.node2)

        # Probar que acepta un diccionario como next_node
        test_dict = {"key": "value"}
        self.node1.set_next_node(test_dict)
        self.assertEqual(self.node1.get_next_node(), test_dict)

        # Probar que el tipo incorrecto lanza una excepción
        with self.assertRaises(TypeError):
            self.node1.set_next_node("No es un nodo ni diccionario")

    def test_set_prev_node(self):
        # Probar el método set_prev_node y verificar el enlace
        self.node2.set_prev_node(self.node1)
        self.assertEqual(self.node2.get_prev_node(), self.node1)

        # Probar que acepta un diccionario como prev_node
        test_dict = {"key": "value"}
        self.node2.set_prev_node(test_dict)
        self.assertEqual(self.node2.get_prev_node(), test_dict)

        # Probar que el tipo incorrecto lanza una excepción
        with self.assertRaises(TypeError):
            self.node2.set_prev_node(123)

    def test_linked_nodes(self):
        # Verificar el funcionamiento del enlace bidireccional
        self.node1.set_next_node(self.node2)
        self.node2.set_prev_node(self.node1)

        self.assertEqual(self.node1.get_next_node(), self.node2)
        self.assertEqual(self.node2.get_prev_node(), self.node1)

        # Probar una cadena de nodos
        self.node2.set_next_node(self.node3)
        self.node3.set_prev_node(self.node2)

        self.assertEqual(self.node2.get_next_node(), self.node3)
        self.assertEqual(self.node3.get_prev_node(), self.node2)

    def test_reset_links(self):
        # Probar que podemos reiniciar los enlaces de next_node y prev_node a None
        self.node1.set_next_node(self.node2)
        self.node2.set_prev_node(self.node1)

        # Reiniciar el siguiente y anterior nodo
        self.node1.set_next_node(None)
        self.node2.set_prev_node(None)

        self.assertIsNone(self.node1.get_next_node())
        self.assertIsNone(self.node2.get_prev_node())

if __name__ == '__main__':
    unittest.main()
