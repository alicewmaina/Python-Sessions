# finally: Runs no matter what, often used to clean up (like closing a file).
# Custom Errors: Create custom exceptions for special cases (e.g., EmptyFileError).


try:
    with open("sample.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("File closed.")