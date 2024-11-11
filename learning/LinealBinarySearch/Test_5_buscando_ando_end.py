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

    def test_sparse_search_C_in_mixed_list(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        sparse_search(["A", "", "", "", "B", "", "", "", "C", "", "", "D"], "C")

        sys.stdout = sys.__stdout__
        self.assertIn("C encontrado en la posicion 8", captured_output.getvalue())

    def test_sparse_search_A_at_start_of_nonempty_list(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        sparse_search(["A", "B", "", "", "E"], "A")

        sys.stdout = sys.__stdout__
        self.assertIn("A encontrado en la posicion 0", captured_output.getvalue())

    def test_sparse_search_Z_at_end_with_nonempty_middle(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        sparse_search(["", "X", "", "Y", "Z"], "Z")

        sys.stdout = sys.__stdout__
        self.assertIn("Z encontrado en la posicion 4", captured_output.getvalue())

    def test_sparse_search_D_not_in_list(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        sparse_search(["A", "", "", "", "B", "", "", "", "C"], "D")

        sys.stdout = sys.__stdout__
        self.assertIn("D no está en el conjunto de datos", captured_output.getvalue())

    def test_sparse_search_Banana_in_mixed_fruit_list(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        sparse_search(["Apple", "", "Banana", "", "", "", "", "Cow"], "Banana")

        sys.stdout = sys.__stdout__
        self.assertIn("Banana encontrado en la posicion 2", captured_output.getvalue())

    def test_sparse_search_Parth_in_large_name_list(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        sparse_search(
            ["Alex", "", "", "", "", "Devan", "", "", "Elise", "", "", "", "Gary", "", "", "Mimi", "", "", "Parth", "", "", "", "Zachary"],
            "Parth"
        )

        sys.stdout = sys.__stdout__
        self.assertIn("Parth encontrado en la posicion 18", captured_output.getvalue())


if __name__ == "__main__":
    unittest.main()
