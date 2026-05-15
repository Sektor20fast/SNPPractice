def max_odd(n):
    res = 0
    try:
        for item in n:
            if (isinstance(item, (int, float))
                    and (item % 2 != 0)
                    and (res < item)) : res = item
        if res != 0:
            return res
        else: return 'None'
    except TypeError:
        return 'err'


print(max_odd([1, 2, 3, 4, 4]))
print(max_odd([21.0, 2, 3, 4, 4]))
print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))
print(max_odd(['ololo', 'fufufu']))
print(max_odd([2, 2, 4]))

