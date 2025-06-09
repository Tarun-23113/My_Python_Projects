class Smartphone:
    os = "Android"
    def __init__(self, brand, model, price, is_on=False):
        self.brand = brand
        self.model = model
        self._price = price
        self.__is_on = is_on
    
    def turn_on(self):
        self.__is_on = True
        print("Is On")
        
    def turn_off(self):
        self.__is_on = False
        print("Is Off")
    
    def Phone(self, number):
        if self.__is_on:
            print(f"Calling {number}")
        else:
            print("Phone is Off")
    
    def get_status(self):
        print("On") if self.__is_on else print("Off")

phone1 = Smartphone("Realme", "Narzo", 10000)
phone1.Phone(123)
phone1.turn_on()
phone1.Phone(123)

phone1.get_status()
phone1._price
phone1._Smartphone__is_on