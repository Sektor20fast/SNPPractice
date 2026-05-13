def multiply_numbers(inputs=None):
    if inputs is None:
        return None

    inputs_str = str(inputs)

    digits = []
    for char in inputs_str:
        if char.isdigit():
            digits.append(int(char))

    if not digits:
        return None

    product = 1
    for digit in digits:
        product *= digit

    return product

print(multiply_numbers())
print(multiply_numbers('ss'))
print(multiply_numbers('1234'))
print(multiply_numbers('sssdd34'))
print(multiply_numbers(2.3))
print(multiply_numbers([5, 6, 4]))