class EvenNumbers:
    def __init__(self, n):
        try:
            self.n = int(n) if n is not None else 0
            if self.n < 0:
                self.n = 0
        except (ValueError, TypeError):
            self.n = 0

        self.current_index = 0

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index >= self.n:
            raise StopIteration

        result = 2 * self.current_index
        self.current_index += 1
        return result


print("=== Тест 1: Базовый пример ===\n")

evens = EvenNumbers(5)
for num in evens:
    print(num)  # Должно вывести 0, 2, 4, 6, 8
print()

print("=== Тест 2: Различные значения n ===\n")

# Тест с n = 1
print("EvenNumbers(1):")
for num in EvenNumbers(1):
    print(f"  {num}")  # 0
print()

# Тест с n = 3
print("EvenNumbers(3):")
for num in EvenNumbers(3):
    print(f"  {num}")  # 0, 2, 4
print()

# Тест с n = 0
print("EvenNumbers(0):")
for num in EvenNumbers(0):
    print(f"  {num}")  # (ничего не выводится)
print()

print("=== Тест 3: Обработка невалидных данных ===\n")

# Тест с отрицательным числом
print("EvenNumbers(-5) (должен вести себя как 0):")
for num in EvenNumbers(-5):
    print(f"  {num}")  # (ничего не выводится)
print()

# Тест со строковым представлением числа
print("EvenNumbers('7'):")
for num in EvenNumbers('7'):
    print(f"  {num}")  # 0, 2, 4, 6, 8, 10, 12
print()

# Тест с невалидной строкой
print("EvenNumbers('abc') (должен вести себя как 0):")
for num in EvenNumbers('abc'):
    print(f"  {num}")  # (ничего не выводится)
print()

# Тест с None
print("EvenNumbers(None) (должен вести себя как 0):")
for num in EvenNumbers(None):
    print(f"  {num}")  # (ничего не выводится)
print()

# Тест с float
print("EvenNumbers(3.7) (преобразуется в целое число):")
for num in EvenNumbers(3.7):
    print(f"  {num}")  # 0, 2, 4 (3 элемента)
print()
