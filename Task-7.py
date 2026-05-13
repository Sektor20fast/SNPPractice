def combine_anagrams(words_array):
    anagrams_dict = {}
    for word in words_array:
        normalized_word = word.lower()
        sorted_letters = ''.join(sorted(normalized_word))
        if sorted_letters not in anagrams_dict:
            anagrams_dict[sorted_letters] = []
        anagrams_dict[sorted_letters].append(word)
    return list(anagrams_dict.values())


print(combine_anagrams([
    "cars", "for", "potatoes", "racs", "four", "scar",
    "creams", "scream"
]))

# Дополнительные тесты
print(combine_anagrams(["listen", "silent", "hello", "world", "silent"]))
print(combine_anagrams(["Cat", "act", "tac", "Tac", "ATc"]))
print(combine_anagrams(["a", "b", "a", "c", "b"]))
print(combine_anagrams([]))
