def from_test(filename='start_from.txt'):
    try:
        with open(filename, 'r') as file:
            content = file.read().strip()  # Read and strip whitespace
            return content == "test"  # Check if content is "test"
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return False

if __name__ == "__main__":
    filename = 'start_.txt'
    result = check_file_content(filename)
    print(result)