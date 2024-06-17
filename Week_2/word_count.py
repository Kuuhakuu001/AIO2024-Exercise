def word_count(file_path):
    word_count_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word in word_count_dict:
                    word_count_dict[word] += 1
                else:
                    word_count_dict[word] = 1
    return word_count_dict

# Example usage
file_path = 'P1_data.txt'  # Make sure to have the file at this path or adjust the path accordingly
result = word_count(file_path)
print(result)
