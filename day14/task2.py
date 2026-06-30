class FileReader:

    def read(self, filename):
        try:
            with open(filename) as f:
                print(f.read())
        except FileNotFoundError:
            print("File not found")
