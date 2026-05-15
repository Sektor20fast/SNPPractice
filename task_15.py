class BlockTranspositionCipher:
    """
    Класс для шифрования и дешифрования текста методом блочной перестановки.
    """

    def __init__(self, text, key, decrypt_mode=False):
        """
        Конструктор класса BlockTranspositionCipher.

        Args:
            text: исходный текст для обработки
            key: текстовый ключ из уникальных английских букв
            decrypt_mode: если True - выполняется дешифрование, иначе шифрование
        """
        # Валидация ключа
        self._validate_key(key)

        # Обработка ключа
        self.key = key
        self.key_length = len(key)
        self.order = self._get_key_order(key)

        # Инвертируем порядок для дешифрования
        if decrypt_mode:
            self.order = self._invert_order(self.order)

        self.text = text
        self.decrypt_mode = decrypt_mode
        self._prepare_blocks()

    def _validate_key(self, key):
        """
        Проверяет ключ на соответствие требованиям.
        """
        if not key:
            raise ValueError("Ключ не может быть пустым")

        # Проверка, что ключ состоит только из букв английского алфавита
        if not all(c.isalpha() and c.isascii() for c in key):
            raise ValueError("Ключ должен состоять только из букв английского алфавита")

        # Проверка уникальности букв (игнорируя регистр)
        key_lower = key.lower()
        if len(set(key_lower)) != len(key):
            raise ValueError("Все буквы в ключе должны быть уникальны (регистр не учитывается)")

    def _get_key_order(self, key):
        """
        Преобразует ключ в числовой массив порядка.
        """
        # Приводим ключ к нижнему регистру
        key_lower = key.lower()

        # Получаем числовые значения (a=0, b=1, ..., z=25)
        numeric_values = [ord(c) - ord('a') for c in key_lower]

        # Сортируем индексы по числовым значениям
        order = sorted(range(self.key_length), key=lambda i: numeric_values[i])

        return order

    def _invert_order(self, order):
        """
        Инвертирует порядок перестановки для дешифрования.
        """
        inverse = [0] * len(order)
        for i, pos in enumerate(order):
            inverse[pos] = i
        return inverse

    def _prepare_blocks(self):
        """
        Подготавливает блоки текста для итерации.
        """
        self.blocks = []

        # Разбиваем текст на блоки длины key_length
        for i in range(0, len(self.text), self.key_length):
            block = self.text[i:i + self.key_length]

            # Дополняем последний блок пробелами при необходимости
            if len(block) < self.key_length:
                block = block.ljust(self.key_length, ' ')

            self.blocks.append(block)

    def _process_block(self, block):
        """
        Обрабатывает один блок согласно порядку перестановки.
        """
        # Создаем массив для результата
        result = [''] * self.key_length

        # Переставляем символы согласно порядку
        for new_pos, old_pos in enumerate(self.order):
            result[new_pos] = block[old_pos]

        return ''.join(result)

    def __iter__(self):
        """
        Возвращает итератор по обработанным блокам.
        """
        self._current_block = 0
        return self

    def __next__(self):
        """
        Возвращает следующий обработанный блок.
        """
        if self._current_block >= len(self.blocks):
            raise StopIteration

        processed_block = self._process_block(self.blocks[self._current_block])

        # Для дешифрования удаляем лишние пробелы только в последнем блоке
        if self.decrypt_mode and self._current_block == len(self.blocks) - 1:
            processed_block = processed_block.rstrip()

        self._current_block += 1
        return processed_block

    def encrypt(self):
        """
        Шифрует весь текст и возвращает результат.
        """
        # Временно сохраняем состояние итератора
        # Сбрасываем итератор для полного прохода
        self._current_block = 0
        result = ''.join(self)
        return result

    def decrypt(self):
        """
        Дешифрует весь текст и возвращает результат.
        """
        # Временно сохраняем состояние итератора
        self._current_block = 0
        result = ''.join(self)
        return result


print("=== Пример 1: Шифрование с явной итерацией по блокам ===\n")

text = "HELLOWORLD"
key = "bAc"

print(f"Исходный текст: '{text}'")
print(f"Ключ: '{key}'")
print(f"Длина ключа: {len(key)}")
print("\nПроцесс шифрования по блокам:")

cipher = BlockTranspositionCipher(text, key, decrypt_mode=False)
for i, encrypted_block in enumerate(cipher, 1):
    print(f"Блок {i}: '{encrypted_block}'")

print("\n=== Пример 2: Полное шифрование ===\n")

cipher = BlockTranspositionCipher(text, key, decrypt_mode=False)
encrypted = cipher.encrypt()
print(f"Полный зашифрованный текст: '{encrypted}'")

print("\n=== Пример 3: Дешифрование с итерацией ===\n")

print(f"Зашифрованный текст: '{encrypted}'")
print("Процесс дешифрования по блокам:")

decipher = BlockTranspositionCipher(encrypted, key, decrypt_mode=True)
for i, decrypted_block in enumerate(decipher, 1):
    print(f"Блок {i}: '{decrypted_block}'")

print("\n=== Пример 4: Полное дешифрование с обрезкой пробелов ===\n")

decipher = BlockTranspositionCipher(encrypted, key, decrypt_mode=True)
decrypted = decipher.decrypt()
print(f"Полный расшифрованный текст: '{decrypted}'")

print("\n=== Дополнительные тесты ===\n")

# Тест 1: Разные ключи
print("Тест 1: Шифрование с ключом 'cba'")
text1 = "ABCDEFGH"
key1 = "cba"
cipher1 = BlockTranspositionCipher(text1, key1, decrypt_mode=False)
encrypted1 = cipher1.encrypt()
print(f"Исходный: '{text1}' -> Зашифрованный: '{encrypted1}'")

decipher1 = BlockTranspositionCipher(encrypted1, key1, decrypt_mode=True)
decrypted1 = decipher1.decrypt()
print(f"Расшифрованный: '{decrypted1}'")
print(f"Верно: {text1 == decrypted1}\n")

# Тест 2: Текст, не кратный длине ключа
print("Тест 2: Текст, не кратный длине ключа")
text2 = "HELLO"
key2 = "abc"
cipher2 = BlockTranspositionCipher(text2, key2, decrypt_mode=False)
encrypted2 = cipher2.encrypt()
print(f"Исходный: '{text2}' -> Зашифрованный: '{encrypted2}'")

decipher2 = BlockTranspositionCipher(encrypted2, key2, decrypt_mode=True)
decrypted2 = decipher2.decrypt()
print(f"Расшифрованный: '{decrypted2}'")
print(f"Верно: {text2 == decrypted2}\n")

# Тест 3: Разные регистры в ключе
print("Тест 3: Разные регистры в ключе")
text3 = "PYTHONPROGRAMMING"
key3 = "ZyXwVuT"
cipher3 = BlockTranspositionCipher(text3, key3, decrypt_mode=False)
encrypted3 = cipher3.encrypt()
print(f"Исходный: '{text3}'")
print(f"Ключ: '{key3}'")
print(f"Зашифрованный: '{encrypted3}'")

decipher3 = BlockTranspositionCipher(encrypted3, key3, decrypt_mode=True)
decrypted3 = decipher3.decrypt()
print(f"Расшифрованный: '{decrypted3}'")
print(f"Верно: {text3 == decrypted3}\n")

# Тест 4: Валидация ключа
print("Тест 4: Проверка валидации ключа")

try:
    cipher4 = BlockTranspositionCipher("test", "aab", decrypt_mode=False)
    print("Ошибка: Должно было быть исключение")
except ValueError as e:
    print(f"Ключ 'aab' → Ошибка: {e}")

try:
    cipher5 = BlockTranspositionCipher("test", "ab1", decrypt_mode=False)
    print("Ошибка: Должно было быть исключение")
except ValueError as e:
    print(f"Ключ 'ab1' → Ошибка: {e}")

try:
    cipher6 = BlockTranspositionCipher("test", "", decrypt_mode=False)
    print("Ошибка: Должно было быть исключение")
except ValueError as e:
    print(f"Пустой ключ → Ошибка: {e}")

print("\n=== Тест 5: Демонстрация порядка перестановки ===\n")

key_demo = "acb"
text_demo = "12345"
print(f"Ключ: '{key_demo}'")
print(f"Числовые значения: {[ord(c.lower()) - ord('a') for c in key_demo]}")

cipher_demo = BlockTranspositionCipher(text_demo, key_demo, decrypt_mode=False)
print(f"Исходный текст: '{text_demo}'")
print("Разбивка на блоки:")

for i, block in enumerate(cipher_demo.blocks, 1):
    print(f"  Блок {i}: '{block}'")
    processed = cipher_demo._process_block(block)
    print(f"    После перестановки: '{processed}'")

encrypted_demo = cipher_demo.encrypt()
print(f"\nЗашифрованный текст: '{encrypted_demo}'")

print("\n=== Тест 6: Проверка с оригинальным примером ===\n")

# Оригинальный пример из условия
original_text = "helloworld"
original_key = "acb"
print(f"Оригинальный текст: '{original_text}'")
print(f"Ключ: '{original_key}'")

cipher_orig = BlockTranspositionCipher(original_text, original_key, decrypt_mode=False)
encrypted_orig = cipher_orig.encrypt()
print(f"Зашифрованный текст: '{encrypted_orig}'")
print(f"Ожидалось: 'hlelwoolrd  '")

decipher_orig = BlockTranspositionCipher(encrypted_orig, original_key, decrypt_mode=True)
decrypted_orig = decipher_orig.decrypt()
print(f"Расшифрованный текст: '{decrypted_orig}'")
print(f"Ожидалось: '{original_text}'")
print(f"Успех: {original_text == decrypted_orig}")
