import time
from functools import wraps
from collections import OrderedDict


def cached(max_size=None, seconds=None):
    if not isinstance(max_size, int) or max_size is None:
        max_size = None
    elif max_size <= 0:
        max_size = None

    if not isinstance(seconds, (int, float)) or seconds is None:
        seconds = None
    elif seconds <= 0:
        seconds = None

    def decorator(func):
        cache = OrderedDict()

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))

            current_time = time.time()

            if key in cache:
                cached_value, cached_time = cache[key]

                if seconds is None or (current_time - cached_time) < seconds:
                    cache.move_to_end(key)
                    return cached_value
                else:
                    del cache[key]

            result = func(*args, **kwargs)

            cache[key] = (result, current_time)

            cache.move_to_end(key)

            if max_size is not None and len(cache) > max_size:
                cache.popitem(last=False)

            return result

        def clear_cache():
            cache.clear()

        wrapper.clear_cache = clear_cache

        def get_cache_info():
            return {
                "size": len(cache),
                "max_size": max_size,
                "seconds": seconds,
                "keys": [key for key in cache.keys()]
            }

        wrapper.get_cache_info = get_cache_info

        return wrapper

    return decorator



print("=== Тест 1: Базовый кэш с ограничением по времени ===\n")

@cached(max_size=3, seconds=10)
def slow_function(x):
    print(f"Вычисляю для {x}...")
    return x ** 2


# Первый вызов - вычисляется
print(f"Результат: {slow_function(2)}")  # "Вычисляю для 2..." → 4
print()

# Повторный вызов - берётся из кэша
print(f"Результат: {slow_function(2)}")  # 4 (без вычисления)
print()

# Демонстрация работы с разными аргументами
print(slow_function(3))  # Вычисляется
print(slow_function(4))  # Вычисляется
print(slow_function(2))  # Из кэша
print()

# Проверка ограничения размера кэша (max_size=3)
print("Добавляем 5-й результат (должен удалиться самый старый - результат для 2):")
print(slow_function(5))  # Вычисляется, удалится 2
print(slow_function(2))  # Будет вычисляться заново
print()

print("=== Тест 2: Неограниченный кэш ===\n")


@cached(max_size=None, seconds=None)
def unlimited_cache(x):
    print(f"Вычисляю {x}...")
    return x * 10


print(unlimited_cache(1))  # Вычисляется
print(unlimited_cache(2))  # Вычисляется
print(unlimited_cache(1))  # Из кэша
print(unlimited_cache(2))  # Из кэша
print()

print("=== Тест 3: Кэш с устареванием ===\n")


@cached(max_size=None, seconds=2)
def time_sensitive(x):
    print(f"Вычисляю {x}...")
    return x + 100


print(time_sensitive(10))  # Вычисляется
print(time_sensitive(10))  # Из кэша

print("Ждем 3 секунды...")
time.sleep(3)
print(time_sensitive(10))  # Снова вычисляется (кэш устарел)
print()

print("=== Тест 4: Именованные аргументы ===\n")


@cached(max_size=5, seconds=None)
def named_args_func(a, b, multiplier=1):
    print(f"Вычисляю для a={a}, b={b}, multiplier={multiplier}...")
    return (a + b) * multiplier


print(named_args_func(2, 3))  # Вычисляется
print(named_args_func(2, 3))  # Из кэша
print(named_args_func(2, 3, multiplier=2))  # Другой ключ - вычисляется
print(named_args_func(b=3, a=2))  # Те же аргументы - из кэша
print()

print("=== Тест 5: Невалидные параметры ===\n")


@cached(max_size="invalid", seconds="also invalid")
def default_params(x):
    print(f"Вычисляю {x}...")
    return x ** 3


print(default_params(2))  # Вычисляется
print(default_params(2))  # Должно быть из кэша (параметры стали None)
print(default_params(3))  # Вычисляется
print()

print("=== Тест 6: Дополнительные методы кэша ===\n")


@cached(max_size=2, seconds=5)
def test_func(x):
    return x * 2


test_func(1)
test_func(2)
test_func(3)  # Вытеснит 1

info = test_func.get_cache_info()
print(f"Информация о кэше: {info}")

test_func.clear_cache()
print(f"После очистки кэша: size = {test_func.get_cache_info()['size']}")