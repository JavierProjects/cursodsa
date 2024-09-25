import unittest
import subprocess

def load_file_in_context(filename):
    """Load and execute a Python file in the current context."""
    with open(filename) as f:
        exec(f.read(), globals())

class TestNodeExercise(unittest.TestCase):
    
    def test_node_ejercicio_script(self):
        # Run the student's Node_ejercicio.py script and capture the output
        try:
            # Ensure the script runs and capture the output
            result = subprocess.run(['python3', 'Node_ejercicio.py'], capture_output=True, text=True, check=True)
            output = result.stdout.strip().split('\n')  # Get the output as a list of lines
            
            # Check that the script printed the correct values for Giovany and Yady
            self.assertEqual(output[0], "Le gustan las princesas", "El valor de Giovany es incorrecto")
            self.assertEqual(output[1], "Le gustan las flores", "El valor de Yady es incorrecto")

        except subprocess.CalledProcessError as e:
            self.fail(f"Hubo un error al ejecutar el archivo Node_ejercicio.py: {e}")

    
    def test_student_code(self):
        # Load the student's code from Node_ejercicio.py
        load_file_in_context("Node_ejercicio.py")
        
        try:            
            if Juan.next_node != Giovany:
                self.fail("¿Asignaste `next_node` de `Juan` a `Giovany`?")
            if Giovany.next_node != Yady:
                self.fail("¿Asignaste `next_node` de `Giovany` a `Yady`?")                
            if Yady.next_node is not None:
                self.fail("`next_node` de `Yady` no debe estar asignado a ningun valor debe valer `None`!")

        except AttributeError:
            self.fail("¿Creaste el metodo `set_next_node` dentro de la clase `Node`?")
        except TypeError:
            self.fail("¿Añadiste `self` y `next_node` como parametros de `set_next_node`?")

if __name__ == '__main__':
    unittest.main()
