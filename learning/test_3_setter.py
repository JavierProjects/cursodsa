import unittest
from Node_sandbox import Node

class TestNodeSetNextNode(unittest.TestCase):

    def test_set_next_node_valid(self):
        t = Node(3)
        h = Node(40)

        # Prueba asignar next_node a otro Node
        t.set_next_node(h)
        self.assertEqual(t.get_next_node(), h, "Debe permitir asignar next_node a una instancia de Node")

        # Prueba asignar next_node a None
        t.set_next_node(None)
        self.assertIsNone(t.get_next_node(), "Debe permitir asignar next_node a None")

        # Prueba asignar next_node a un diccionario
        t.set_next_node({"clave": "valor"})
        self.assertEqual(t.get_next_node(), {"clave": "valor"}, "Debe permitir asignar next_node a un diccionario")

    def test_set_next_node_invalid(self):
        t = Node(3)

        # Prueba asignar next_node a un tipo no válido (por ejemplo, lista)
        with self.assertRaises(TypeError, msg="Se esperaba TypeError al asignar next_node a una lista"):
            t.set_next_node([1, 2, 3])

        # Prueba asignar next_node a un tipo no válido (por ejemplo, cadena)
        with self.assertRaises(TypeError, msg="Se esperaba TypeError al asignar next_node a una cadena"):
            t.set_next_node("tipo_invalido")

if __name__ == '__main__':
    unittest.main()
