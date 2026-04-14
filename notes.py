notes = []

while True:
    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Delete All Notes")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        note = input("Enter note: ")
        notes.append(note)
        print("Note added!")

    elif choice == "2":
        if not notes:
            print("No notes available.")
        else:
            print("\nYour Notes:")
            for i, n in enumerate(notes, start=1):
                print(f"{i}. {n}")

    elif choice == "3":
        confirm = input("Are you sure you want to delete all notes? (yes/no): ")
        if confirm.lower() == "yes":
            notes.clear()
            print("All notes deleted!")
        else:
            print("Deletion cancelled.")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")