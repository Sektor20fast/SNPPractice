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

class JellyBean(Dessert):

    def __init__(self, name=None, calories=None, flavor=None):
        super().__init__(name, calories)
        self._flavor = flavor

    def get_flavor(self):
        return self._flavor

    def set_flavor(self, flavor):
        self._flavor = flavor

    def is_delicious(self):
        try:
            if self._flavor is None:
                return True

            flavor_lower = str(self._flavor).lower()

            if flavor_lower == "black licorice":
                return False
            else:
                return True
        except (ValueError, AttributeError, TypeError):
            return True


print("=== Тестирование класса JellyBean ===\n")

# Тест 1: Создание JellyBean с параметрами
jelly1 = JellyBean("Jelly Bean", 150, "strawberry")
print(f"Конфета: {jelly1.get_name()}")
print(f"Калории: {jelly1.get_calories()}")
print(f"Вкус: {jelly1.get_flavor()}")
print(f"is_healthy: {jelly1.is_healthy()}")
print(f"is_delicious: {jelly1.is_delicious()}")  # True
print()

# Тест 2: JellyBean с черной лакрицей
jelly2 = JellyBean("Licorice Bean", 180, "black licorice")
print(f"Конфета: {jelly2.get_name()}")
print(f"Вкус: {jelly2.get_flavor()}")
print(f"is_delicious: {jelly2.is_delicious()}")  # False
print()

# Тест 3: JellyBean с черной лакрицей (другой регистр)
jelly3 = JellyBean("Bean", 190, "BLACK LICORICE")
print(f"Конфета: {jelly3.get_name()}")
print(f"Вкус: {jelly3.get_flavor()}")
print(f"is_delicious: {jelly3.is_delicious()}")  # False (регистронезависимо)
print()

# Тест 4: JellyBean без параметров
jelly4 = JellyBean()
print(f"Конфета без параметров:")
print(f"  name: {jelly4.get_name()}")
print(f"  flavor: {jelly4.get_flavor()}")
print(f"  is_delicious: {jelly4.is_delicious()}")  # True
print()

# Тест 5: Использование сеттеров
jelly5 = JellyBean()
jelly5.set_name("Magic Bean")
jelly5.set_calories(250)
jelly5.set_flavor("chocolate")
print(f"После установки свойств:")
print(f"  name: {jelly5.get_name()}")
print(f"  calories: {jelly5.get_calories()}")
print(f"  flavor: {jelly5.get_flavor()}")
print(f"  is_delicious: {jelly5.is_delicious()}")  # True
print()

# Тест 6: Изменение вкуса на black licorice через сеттер
jelly5.set_flavor("black licorice")
print(f"После изменения вкуса на black licorice:")
print(f"  flavor: {jelly5.get_flavor()}")
print(f"  is_delicious: {jelly5.is_delicious()}")  # False
print()

# Тест 7: Различные вкусы
print("Тестирование различных вкусов:")
flavors = [
    ("vanilla", True),
    ("black licorice", False),
    ("BLACK LICORICE", False),
    ("Black Licorice", False),
    ("", True),
    (None, True),
    (123, True),
    ("grape", True),
    ("apple", True)
]

for flavor, expected in flavors:
    jelly = JellyBean("Test", 100, flavor)
    result = jelly.is_delicious()
    print(f"  Вкус: {flavor} -> is_delicious: {result} (ожидалось: {expected})")
print()
