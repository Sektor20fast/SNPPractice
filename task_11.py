class Dessert:
    def __init__(self, name=None, calories=None):
        self._name = name
        self._calories = calories

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_calories(self):
        return self._calories

    def set_calories(self, calories):
        self._calories = calories

    def is_healthy(self):
        try:
            if self._calories is None:
                return False
            calories_value = float(self._calories)
            return calories_value < 200
        except (ValueError, TypeError):
            return False

    def is_delicious(self):
        return True


# Тесты

print("=== Тестирование класса Dessert ===\n")

# Тест 1: Создание десерта с параметрами
dessert1 = Dessert("Cake", 350)
print(f"Десерт: {dessert1.get_name()}, калории: {dessert1.get_calories()}")
print(f"is_healthy: {dessert1.is_healthy()}")  # False (>200)
print(f"is_delicious: {dessert1.is_delicious()}")  # True
print()

# Тест 2: Создание десерта без параметров
dessert2 = Dessert()
print(f"Десерт: {dessert2.get_name()}, калории: {dessert2.get_calories()}")
print(f"is_healthy: {dessert2.is_healthy()}")  # False
print(f"is_delicious: {dessert2.is_delicious()}")  # True
print()

# Тест 3: Использование сеттеров
dessert3 = Dessert("Ice Cream", 150)
print(f"До изменения: {dessert3.get_name()}, {dessert3.get_calories()}")
dessert3.set_name("Gelato")
dessert3.set_calories(180)
print(f"После изменения: {dessert3.get_name()}, {dessert3.get_calories()}")
print(f"is_healthy: {dessert3.is_healthy()}")  # True (<200)
print()

# Тест 4: Проверка на невалидные данные
dessert4 = Dessert("Cookie", "not a number")
print(f"Десерт: {dessert4.get_name()}, калории: {dessert4.get_calories()}")
print(f"is_healthy with invalid calories: {dessert4.is_healthy()}")  # False
dessert4.calories = None
print(f"is_healthy with None: {dessert4.is_healthy()}")  # False
print()
