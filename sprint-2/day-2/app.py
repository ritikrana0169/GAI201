import json

def displayMenu():
    with open("menu.json", "r") as file:
        menu_data = json.load(file)

    print("Menu:")
    print("Dish Name\tPrice\tAvailability")
    print("--------------------------------")

    for dish in menu_data:
        availability = "Available" if dish["availability"] else "Not Available"
        print(f"{dish['dish_name']}\t\t{dish['price']}\t{availability}")




def remove_dish_by_name(self, dish_name):
        removed_dish_id = None
        for dish_id, dish in self.menu.items():
            if dish.name.lower() == dish_name.lower():
                removed_dish_id = dish_id
                del self.menu[dish_id]
                self._update_menu_json()
                print(f"Dish '{dish_name}' removed successfully.")
                break

        if removed_dish_id is None:
            print(f"Dish '{dish_name}' not found in the menu.")



def _update_menu_json(self):
    menu_data = [{"dish_id": dish.dish_id, "name": dish.name, "price": dish.price, "availability": dish.availability}
                    for dish in self.menu.values()]

    with open("menu.json", "w") as file:
            json.dump(menu_data, file, indent=4)






def main():
    while True:
        print("Welcome to Zesty Zomato!")
        print("0. Display Menu")
        print("1. Add Dish")
        print("2. Remove Dish")
        print("3. Update Dish Availability")
        print("4. Take Order")
        print("5. Update Order Status")
        print("6. Review Orders")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '0':
            print("\nMENU")
            displayMenu()
        elif choice == '1':
            # Implement adding a new dish
            pass
        elif choice == '2':
            print("/nREMOVE DISH")
            dishName=str(input("Enter dish name to remove dish:"))
            remove_dish_by_name(dishName)
            pass
        elif choice == '3':
            # Implement updating dish availability
            pass
        elif choice == '4':
            # Implement taking a new order
            pass
        elif choice == '5':
            # Implement updating order status
            pass
        elif choice == '6':
            # Implement reviewing orders
            pass
        elif choice == '7':
            print("Thank you for using Zesty Zomato!")
            break
        else:
            print("Invalid choice. Please select a valid option.")




main()
