# Step 1: Create an empty shopping list
shopping_list = []

# Step 2: Define the display_menu function
def display_menu():
    print("\nSHOPPING LIST MANAGER")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Quit")

# Step 3: Main loop
while True:
    display_menu()  # show the menu

    try:
        choice = int(input("Enter your choice (1-4): "))  # get numeric input
    except ValueError:
        print("Please enter a number.")
        continue

    if choice == 1:
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"{item} added to the list.")

    elif choice == 2:
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed.")
        else:
            print("Item not found.")

    elif choice == 3:
        print("\nShopping List:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")

    elif choice == 4:
        print("Exiting. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
