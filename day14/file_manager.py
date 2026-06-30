import os


class FileManager:

    def create_file(self, filename):
        """Create an empty file."""
        try:
            with open(filename, "w"):
                pass
            print(f"[SUCCESS] {filename} created successfully.")
        except Exception as e:
            print(f"[ERROR] {e}")

    def write_file(self, filename, content):
        """Write content to a file."""
        try:
            with open(filename, "w") as file:
                file.write(content)
            print(f"[SUCCESS] Content written to {filename}.")
        except Exception as e:
            print(f"[ERROR] {e}")

    def append_file(self, filename, content):
        """Append content to a file."""
        try:
            with open(filename, "a") as file:
                file.write(content)
            print(f"[SUCCESS] Content appended to {filename}.")
        except Exception as e:
            print(f"[ERROR] {e}")

    def read_file(self, filename):
        """Read and display file content."""
        try:
            with open(filename, "r") as file:
                print("\n----- File Content -----")
                print(file.read())
                print("------------------------")
        except FileNotFoundError:
            print("[ERROR] File not found.")
        except Exception as e:
            print(f"[ERROR] {e}")

    def delete_file(self, filename):
        """Delete a file."""
        try:
            if os.path.exists(filename):
                os.remove(filename)
                print(f"[SUCCESS] {filename} deleted successfully.")
            else:
                print("[ERROR] File does not exist.")
        except Exception as e:
            print(f"[ERROR] {e}")

    def file_exists(self, filename):
        """Check if a file exists."""
        if os.path.exists(filename):
            print("[INFO] File exists.")
            return True
        else:
            print("[INFO] File does not exist.")
            return False
