class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_summary(self):
        return f"{self.product_id} | {self.name} | ${self.price} | Qty: {self.quantity}"

    def update_name(self, new_name):
        self.name = new_name

    def update_price(self, new_price):
        self.price = new_price

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id in self.products:
            print(" Error: Product ID already exists.")
            return False
        else:
            self.products[product.product_id] = product
            print(" Product added successfully.")
            return True

    def update_stock(self, product_id, new_quantity):
        product = self.products.get(product_id)
        if product:
            product.quantity = new_quantity
            print(" Stock updated.")
            return True
        else:
            print(" Error: Product not found.")
            return False

    def find_by_id(self, product_id):
        return self.products.get(product_id, None)

    def find_by_name(self, name):
        for product in self.products.values():
            if product.name.lower() == name.lower():
                return product
        return None

    def list_all(self):
        if not self.products:
            print(" Inventory is empty.")
        else:
            print("\ Current Inventory:")
            for product in self.products.values():
                print(product.get_summary())

                class ElectronicsProduct(Product):
    def __init__(self, product_id, name, price, quantity, warranty_months):
        super().__init__(product_id, name, price, quantity)
        self.warranty_months = warranty_months

    def get_summary(self):
        base = super().get_summary()
        return f"{base} | Warranty: {self.warranty_months} months"


class ClothingProduct(Product):
    def __init__(self, product_id, name, price, quantity, size, color):
        super().__init__(product_id, name, price, quantity)
        self.size = size
        self.color = color

    def get_summary(self):
        base = super().get_summary()
        return f"{base} | Size: {self.size} | Color: {self.color}"
class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_summary(self):
        return f"{self.product_id} | {self.name} | ${self.price} | Qty: {self.quantity}"

    def update_name(self, new_name):
        self.name = new_name

    def update_price(self, new_price):
        self.price = new_price



class ElectronicsProduct(Product):
    def __init__(self, product_id, name, price, quantity, warranty_months):
        super().__init__(product_id, name, price, quantity)
        self.warranty_months = warranty_months

    def get_summary(self):
        base = super().get_summary()
        return f"{base} | Warranty: {self.warranty_months} months"


class ClothingProduct(Product):
    def __init__(self, product_id, name, price, quantity, size, color):
        super().__init__(product_id, name, price, quantity)
        self.size = size
        self.color = color

    def get_summary(self):
        base = super().get_summary()
        return f"{base} | Size: {self.size} | Color: {self.color}"



class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id in self.products:
            print(" Error: Product ID already exists.")
            return False
        self.products[product.product_id] = product
        print("Product added successfully.")
        return True

    def update_stock(self, product_id, new_quantity):
        product = self.products.get(product_id)
        if product:
            product.quantity = new_quantity
            print(" Stock updated.")
            return True
        print(" Product not found.")
        return False

    def find_by_id(self, product_id):
        return self.products.get(product_id)

    def find_by_name(self, name):
        for product in self.products.values():
            if product.name.lower() == name.lower():
                return product
        return None

    def list_all(self):
        if not self.products:
            print(" Inventory is empty.")
        else:
            print("\n Current Inventory:")
            for product in self.products.values():
                print(product.get_summary())



def show_menu():
    print("""
========= GadgetGrove Inventory Manager =========

""")


def product_type_menu():
    print("""
Select Product Type:
1. Standard Product
2. Electronics Product
3. Clothing Product
""")


def main():
    inventory = Inventory()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        # Add Product
        if choice == "1":
            product_type_menu()
            p_choice = input("Choose type: ")

            product_id = input("Product ID: ")
            name = input("Name: ")
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))

            if p_choice == "1":
                product = Product(product_id, name, price, quantity)

            elif p_choice == "2":
                warranty = int(input("Warranty (months): "))
                product = ElectronicsProduct(product_id, name, price, quantity, warranty)

            elif p_choice == "3":
                size = input("Size: ")
                color = input("Color: ")
                product = ClothingProduct(product_id, name, price, quantity, size, color)

            else:
                print(" Invalid product type.")
                continue

            inventory.add_product(product)

        # Search Product
        elif choice == "2":
            method = input("Search by (1) ID or (2) Name: ")

            if method == "1":
                pid = input("Enter ID: ")
                product = inventory.find_by_id(pid)

            elif method == "2":
                name = input("Enter Name: ")
                product = inventory.find_by_name(name)

            else:
                print(" Invalid choice.")
                continue

            if product:
                print(" Product Found:")
                print(product.get_summary())
            else:
                print(" No such product found.")

        # Update Stock
        elif choice == "3":
            pid = input("Enter Product ID: ")
            qty = int(input("New Quantity: "))
            inventory.update_stock(pid, qty)

        # List all
        elif choice == "4":
            inventory.list_all()

        # Exit
        elif choice == "5":
            print(" Exiting... Goodbye Alex!")
            break

        else:
            print(" Invalid choice. Try again.")


# Run the program
if __name__ == "__main__":
    main()

