
def coincidence(lst=None, rng=None):
    try:
        return [
            item for item in lst
            if isinstance(item, (int, float)) and item in rng
        ]
    except TypeError:
        return []



print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence())
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))