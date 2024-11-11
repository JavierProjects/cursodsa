import unittest
from io import StringIO
import sys
import start
if start.from_test():
    print("Running from Dr Javier's code")
    from buscando_ando import sparse_search  
else:
    print("Running from students' code")
    from buscando_ando_sandbox import sparse_search  
    
class TestSparseSearch(unittest.TestCase):

    def test_empty_string_list(self):
        # Redirige la salida estándar a un StringIO para capturar el output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Llama a la función con el caso específico
        sparse_search([""], "Hello")

        # Restaura la salida estándar
        sys.stdout = sys.__stdout__

        # Verifica el contenido del output
        self.assertIn("Hello no está en el conjunto de datos", captured_output.getvalue())


if __name__ == "__main__":
    unittest.main()