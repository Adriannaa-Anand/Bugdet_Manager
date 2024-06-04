class BudgetManager:
    def __init__(self, filename='budget_data.txt'):
        self.filename = filename
        self.categories = self.load_budget()

    def load_budget(self):
        categories = {}
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    category, balance = line.strip().split(',')
                    categories[category] = float(balance)
        except FileNotFoundError:
            pass
        return categories

    def save_budget(self):
        with open(self.filename, 'w') as file:
            for category, balance in self.categories.items():
                file.write(f"{category},{balance}\n")

    def add_category(self, category_name):
        if category_name not in self.categories:
            self.categories[category_name] = 0.0
            self.save_budget()
            print(f"Added {category_name} category.")
        else:
            print("Category already exists.")

    def add_funds(self, category_name, amount):
        if category_name in self.categories:
            self.categories[category_name] += amount
            self.save_budget()
            print(f"Added {amount} to {category_name}.")
        else:
            print("Category does not exist.")

    def spend_funds(self, category_name, amount):
        if category_name in self.categories:
            if self.categories[category_name] >= amount:
                self.categories[category_name] -= amount
                self.save_budget()
                print(f"Spent {amount} from {category_name}.")
            else:
                print("Insufficient funds in this category.")
        else:
            print("Category does not exist.")

    def show_balance(self):
        print("Current Budget:")
        for category, balance in self.categories.items():
            print(f"{category}: Rs.{balance:.2f}")


def main():
    budget_manager = BudgetManager()

    # Ask user how many categories they want to create
    while True:
        try:
            num_categories = int(input("How many categories do you want to create? "))
            if num_categories > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Add categories based on user input
    for _ in range(num_categories):
        category_name = input("Enter category name: ")
        budget_manager.add_category(category_name)

    while True:
        print("\n1. Add Funds\n2. Spend Funds\n3. Show Balance\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            category_name = input("Enter category name: ")
            amount = float(input("Enter amount to add: Rs."))
            budget_manager.add_funds(category_name, amount)
        elif choice == "2":
            category_name = input("Enter category name: ")
            amount = float(input("Enter amount to spend: Rs."))
            budget_manager.spend_funds(category_name, amount)
        elif choice == "3":
            budget_manager.show_balance()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
