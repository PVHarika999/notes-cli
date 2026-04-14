def add_note():
    note = input("Enter note: ")
    with open("notes.txt", "a") as f:
        f.write(note + "\n")
    print("Note saved successfully!")

def view_notes():
    try:
        with open("notes.txt", "r") as f:
            notes = f.readlines()
            if not notes:
                print("No notes found.")
            else:
                print("\nYour Notes:")
                for i, n in enumerate(notes, 1):
                    print(f"{i}. {n.strip()}")
    except FileNotFoundError:
        print("No notes file found.")

while True:
    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_note()

    elif choice == "2":
        view_notes()

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice")