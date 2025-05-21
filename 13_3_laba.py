class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")
        print()

    def open_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' сейчас открыт!")

    def update_rating(self, new_rating):
        if 0 <= new_rating <= 5:
            self.rating = new_rating
            print(f"Рейтинг ресторана {self.restaurant_name} обновлен до {self.rating}")
        else:
            print("Ошибка: рейтинг должен быть от 0 до 5")


restaurant = Restaurant("Чай вдвоем", "восточная кухня")


restaurant.describe_restaurant()
restaurant.update_rating(4.3)
restaurant.describe_restaurant()
