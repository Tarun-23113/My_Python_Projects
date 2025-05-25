class Product:
    def __init__(self, _product_id, name, price, __stock):
        self._product_id = _product_id
        self.name = name
        self.price = price
        self.__stock = __stock

    def get_stock(self):
        return self.__stock

    def decrease_stock(self, quantity):
        if self.__stock > 0:
            self.__stock -= quantity;
            print(f"Decreased Stock of {self.name} by {quantity}")
        else:
            print("Unable to Decrease Stock")

    def increase_stock(self, quantity):
        self.__stock += quantity
        print(f"Done... Stock is Increased by {quantity}")

    def display_info(self):
        print(f"Product_ID : {self._product_id} \n Name : {self.name} \n Price : {self.price} \n Stock : {self.__stock}")

class Electronics(Product):
    def __init__(self, product_id, name, price, stock, warranty_years):
        super().__init__(product_id, name, price, stock)
        self.warranty_years = warranty_years

    def display_info(self):
        super().display_info()
        print(f"Warranty Years : {self.warranty_years}")

class Clothing(Product):
    def __init__(self, product_id, name, price, stock, size, material):
        super().__init__(product_id, name, price, stock)
        self.size = size
        self.material = material

    def display_info(self):
        super().display_info()
        print(f"Size : {self.size} \n Material : {self.material}")

class Shoppingcart:
    def __init__(self):
        self.items: dict[str, tuple[Product, int]] = {}

    def add_item(self, product_object, quantity):
        if product_object.get_stock()  > 0:
            self.items.update({product_object._product_id : (product_object, quantity)})
            print(f"Added Successfully {quantity} items of {product_object.name}")
        else:
            print(f"......{product_object} is not in stock")

    def remove_item(self, product_id, quantity):
        if product_id in self.items:
            if quantity >= self.items[product_id][1]:
                self.items.pop(product_id)
                print("All Items are removed of this product type")
            else:
                tuple1 = self.items[product_id]
                quantity2 = tuple1[1]-quantity
                tuple2 = (tuple1[0], quantity2)
                self.items.update({product_id : tuple2})
                print(f"Operation Successful we have removed {quantity} items of {tuple[0]}")
        else:
            print("... it seeems  .. like this product do not exist")

    def get_total_price(self):
        if not self.items:
            print("Your cart is empty add some items")
        else:
            sum = 0
            for y in self.items.values():
                price = y[0].price
                quantity = y[1]
                sum += price*quantity
            print(f"Your total sum is {sum} only Sir !!! \n do you wish to add more items ???")

    def display_cart(self):
        if not self.items:
            print("Your cart is empty add some items")
        else:
            for y in self.items.values():
                price = y[0].price
                quantity = y[1]
                print(f"Product : {y[0].name} \t Total Price : {price*quantity}")

class Order:
    _next_order_id = 1001
    def __init__(self, customer_name, shopping_cart):
        self.customer_name = customer_name
        self.shopping_cart = shopping_cart
        self.order_id = Order._next_order_id
        Order._next_order_id += 1
        self.ordered_items: dict[Product, int] = {}
        self.total_amount = 0

    def iterate_cart(self):
        self.shopping_cart.display_cart()
        if not self.shopping_cart.items:
            print("....seems like your cart is empty")
        else:
            for y in self.shopping_cart.items.values():
                print(f"Product : y[0] - Quantity : {y[1]} ")
                i = int(input("How many quantity you want for this item : "))
                if i < y[0].get_stock():
                    self.ordered_items[y[0]] = i
                    y[0].decrease_stock(i)
                else:
                    print("Re Iterate after wards and enter a valid value")
                    continue
        print("Are you Finished yet?? \n wanna recheck the cart for anything")

    def display_order_details(self):
        if not self.ordered_items:
            print("Create a Ordered List first.")
        else:
            for x in self.ordered_items:
                print(f"Order Id : {self.order_id} \t Product : {x.name} \t Product Price : {x.price} \t Quantity : {self.ordered_items[x]} \t Total : {x.price * self.ordered_items[x]}")

#Test this system

electronics_list = [
    Electronics("E101", "Laptop", 50000, 10, 2),
    Electronics("E102", "Smartphone", 25000, 15, 1),
    Electronics("E103", "Tablet", 15000, 12, 1),
    Electronics("E104", "Smartwatch", 8000, 20, 1),
    Electronics("E105", "Monitor", 12000, 8, 2),
    Electronics("E106", "TV", 30000, 6, 2),
    Electronics("E107", "Headphones", 2000, 25, 1),
    Electronics("E108", "Keyboard", 1500, 20, 1),
    Electronics("E109", "Mouse", 1000, 30, 1),
    Electronics("E110", "Speakers", 3500, 15, 1)
]

clothing_list = [
    Clothing("C201", "T-Shirt", 500, 30, "M", "Cotton"),
    Clothing("C202", "Jeans", 1200, 25, "L", "Denim"),
    Clothing("C203", "Jacket", 2000, 10, "XL", "Leather"),
    Clothing("C204", "Dress", 1500, 15, "S", "Silk"),
    Clothing("C205", "Shorts", 800, 18, "M", "Cotton"),
    Clothing("C206", "Shirt", 900, 22, "L", "Linen"),
    Clothing("C207", "Kurta", 1100, 14, "M", "Cotton"),
    Clothing("C208", "Blazer", 2500, 8, "XL", "Wool"),
    Clothing("C209", "Sweater", 1800, 12, "L", "Wool"),
    Clothing("C210", "Cap", 300, 40, "Free", "Cotton")
]

all_products = electronics_list + clothing_list

orders = []
carts = []

while True:
    print("\n==== Available Products ====")
    print(f"{'ID':<6} {'Name':<15} {'Price':<8} {'Stock':<6}")
    print("-" * 40)
    for prod in all_products:
        print(f"{prod._product_id:<6} {prod.name:<15} {prod.price:<8} {prod.get_stock():<6}")

    cart = Shoppingcart()
    carts.append(cart)
    cart_index = len(carts) - 1
    print(f"\nCreated Cart #{cart_index}")

    while True:
        prod_id = input("Enter Product ID to add (or type 'done' to finish): ")
        if prod_id.lower() == 'done':
            break
        matching = [p for p in all_products if p._product_id == prod_id]
        if matching:
            qty = input("Enter quantity: ")
            if not qty.isdigit():
                print("Invalid quantity, please enter a number.")
                continue
            qty = int(qty)
            cart.add_item(matching[0], qty)
        else:
            print("Invalid Product ID")

    cart.display_cart()

    place_order = input("\nDo you want to place an order with this cart? (yes/no): ").lower()
    if place_order == 'yes':
        break

while True:
    name = input("\nEnter your name to place order (or type 'exit' to quit): ").strip()
    if name.lower() == 'exit':
        break
    while(True):
        cart_index = int(input("\nEnter the cart no. to place order : "))
        if cart_index >= len(carts):
            print(f"Invalid Cart Index, you only have {len(carts)} no. of Carts at present")
            continue
        else:
            break

    order = Order(name, carts[cart_index])
    order.iterate_cart()
    order.display_order_details()
    orders.append(order)

    another_order = input("\nDo you want to place another order? (yes/no): ").lower()
    if another_order != 'yes':
        break

print("\n\n==== Summary of All Orders ====")
for order in orders:
    order.display_order_details()
    print("-" * 40)
