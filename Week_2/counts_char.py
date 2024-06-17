def count_chars(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# Example usage
string1 = 'Happiness'
result1 = count_chars(string1)
print(result1)  # Output: {'H': 1, 'a': 1, 'p': 2, 'i': 1, 'n': 1, 'e': 1, 's': 2}

string2 = 'smiles'
result2 = count_chars(string2)
print(result2)  # Output: {'s': 2, 'm': 1, 'i': 1, 'l': 1, 'e': 1}
