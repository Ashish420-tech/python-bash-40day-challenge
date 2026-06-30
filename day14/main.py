from logger import Logger

log = Logger()

while True:
    print("\n" + "=" * 40)
    print("      DevOps Log Manager")
    print("=" * 40)
    print("1. Create Log File")
    print("2. Write Log")
    print("3. Append Log")
    print("4. Read Log")
    print("5. Check File Exists")
    print("6. Delete Log")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    if choice == "1":
        filename = input("Enter filename: ")
        log.create_file(filename)

    elif choice == "2":
        filename = input("Enter filename: ")
        message = input("Enter log message: ")
        log.write_file(filename, message + "\n")

    elif choice == "3":
        filename = input("Enter filename: ")
        message = input("Enter log message: ")
        log.log_message(filename, message)

    elif choice == "4":
        filename = input("Enter filename: ")
        log.read_file(filename)

    elif choice == "5":
        filename = input("Enter filename: ")
        log.file_exists(filename)

    elif choice == "6":
        filename = input("Enter filename: ")
        log.delete_file(filename)

    elif choice == "7":
        print("\nThank you for using DevOps Log Manager.")
        print("Exiting...")
        break

    else:
        print("\nInvalid choice! Please select a number between 1 and 7.")
