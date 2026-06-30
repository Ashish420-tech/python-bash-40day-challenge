servers = []

while True:
    print("\n===== Server Inventory Manager =====")
    print("1. Add Server")
    print("2. View Servers")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        server = input("Enter Server Name: ")
        servers.append(server)
        print(f"{server} added successfully!")

    elif choice == "2":
        print(servers)

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please try again.")
