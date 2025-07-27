shopping_list = []

def display_menu():
    print("\nShopping List Manager")
    print("1. View Shopping List")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Exit")

while True:
    display_menu()
    
    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        print("Shopping List:")
        for item in shopping_list:
            print(f"- {item}")
    elif choice == 2:
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"{item} added.")
    elif choice == 3:
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed.")
        else:
            print(f"{item} not found in list.")
    elif choice == 4:
        print("Exiting Shopping List Manager.")
        break
    else:
        print("Please choose a valid option.")
