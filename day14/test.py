from file_manager import FileManager

fm = FileManager()

fm.create_file("sample.txt")

fm.write_file("sample.txt", "DevOps Log Manager Started\n")

fm.append_file("sample.txt", "Application Running\n")

fm.read_file("sample.txt")

fm.file_exists("sample.txt")

# Uncomment to test deletion
# fm.delete_file("sample.txt")
