from diary import add_entry, show_entries

file_name = input("Diary filename: ")

while True:
    # Create the diary file if it does not exist.
    diary_file = open(file_name, "a")
    diary_file.close()

    print("1. Add entry")
    print("2. Find entries by date")
    print("3. Change diary file")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_entry(file_name)
    elif choice == "2":
        show_entries(file_name)
    elif choice == "3":
        file_name = input("Diary filename: ")
    elif choice == "4":
        break
