class Product:
    def __init__(self, _product_id, name, price, __stock):
        self._product_id = _product_id
        self.name = name
        self.price = price
        self.__stock = __stock

    def get_stock(self):
        print(f"Stock Availble Now is {self.__stock}")
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
            print(f"Added Successfully {quantity} items of {product_object}")
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
                print(f"Product : {y[0]} \t Total Price : {price*quantity}")

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
            for y in self.shopping_cart.item.values:
                print(f"Product : y[0] - Quantity : {y[1]} ")
                i = int(input("How many quantity you want for this item : "))
                if i < y[0].get_stock():
                    self.ordered_items = {y[0], i}
                    y[0].decrease_stock(i)
                else:
                    print("Re Iterate after wards and enter a valid value")
                    continue
        print("Are you Finished yet?? \n wanna recheck the cart for anything")

    def display_order_details(self):
        if not self.ordered_items:
            print("Create a Ordered List first.")
        else:
            for y in self.ordered_items.values():
                print(f"Order Id : {self.order_id} \t Product : {y[0]} \t Product Price : {y[0].price} \t Quantity : {y[1]} \t Total : {y[0].price * y[1]}")

Pen1 = Product(101, "ButterFlow", 15, 200)
Pen1.get_stock()
Pen1.decrease_stock(5)
Pen1.increase_stock(10)
Pen1.display_info()

TV1 = Electronics(201, "Sony Bravia", 200000, 15, "May 2027")
TV1.get_stock()
TV1.decrease_stock(5)
TV1.increase_stock(10)
TV1.display_info()

T_shirt1 = Clothing(301, "Nobero Black", 399, 25, 'L', "cotton")
T_shirt1.get_stock()
T_shirt1.decrease_stock(5)
T_shirt1.increase_stock(10)
T_shirt1.display_info()