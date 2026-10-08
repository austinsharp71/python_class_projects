def add_entry(file_name):
    date = input("Date (YYYY-MM-DD): ")
    entry = input("Diary entry: ")
    diary_file = open(file_name, "a")
    diary_file.write(date + " | " + entry + "\n")
    diary_file.close()


def show_entries(file_name):
    date = input("Date to find (YYYY-MM-DD): ")
    diary_file = open(file_name, "r")
    for line in diary_file:
        if line.startswith(date + " | "):
            print(line)
    diary_file.close()
