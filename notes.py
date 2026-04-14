notes = []

while True:
    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        note = input("Enter note: ")
        notes.append(note)
        print("Note added!")

    elif choice == "2":
        print("\nYour Notes:")
        for n in notes:
            print("-", n)

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice")