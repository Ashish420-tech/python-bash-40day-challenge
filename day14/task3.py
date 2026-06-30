import os


class FileManager:

    def create_file(self, filename):
        with open(filename, "w") as file:
            pass
        print(f"{filename} created successfully.")
