class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print()

restaurant1 = Restaurant("Мексиканец", "мексиканская кухня")
restaurant2 = Restaurant("Гейша", "японская кухня")
restaurant3 = Restaurant("Рыцарь круголого стола", "европейская кухня")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
