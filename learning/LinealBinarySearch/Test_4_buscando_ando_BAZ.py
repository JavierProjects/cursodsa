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

    def test_sparse_search_B_in_mixed_list(self):
        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function with the test case
        sparse_search(["A", "", "", "", "B", "", "", "", "C"], "B")

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Check if "B encontrado en la posicion 4" is in the output
        self.assertIn("B encontrado en la posicion 4", captured_output.getvalue())

    def test_sparse_search_A_at_start(self):
        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function with the test case
        sparse_search(["A", "", "", "", ""], "A")

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Check if "A encontrado en la posicion 0" is in the output
        self.assertIn("A encontrado en la posicion 0", captured_output.getvalue())

    def test_sparse_search_Z_at_end(self):
        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function with the test case
        sparse_search(["", "", "", "", "Z"], "Z")

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Check if "Z encontrado en la posicion 4" is in the output
        self.assertIn("Z encontrado en la posicion 4", captured_output.getvalue())


if __name__ == "__main__":
    unittest.main()
