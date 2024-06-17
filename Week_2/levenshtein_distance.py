def levenshtein_distance(source, target):
    # Step 1: Initialize the matrix
    m, n = len(source), len(target)
    D = [[0] * (n + 1) for _ in range(m + 1)]

    # Step 2: Fill the first row and first column
    for i in range(1, m + 1):
        D[i][0] = i
    for j in range(1, n + 1):
        D[0][j] = j

    # Step 3: Fill the rest of the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if source[i - 1] == target[j - 1] else 1
            D[i][j] = min(D[i - 1][j] + 1,  # Deletion
                          D[i][j - 1] + 1,  # Insertion
                          D[i - 1][j - 1] + cost)  # Substitution

    return D[m][n], D

def print_matrix(D, source, target):
    source = ' ' + source
    target = ' ' + target
    print("     " + "  ".join(target))
    for i, row in enumerate(D):
        print((source[i] if i > 0 else ' ') + "  ".join(map(str, row)))

# Example usage
source = "yu"
target = "you"
distance, D = levenshtein_distance(source, target)
print(f"Levenshtein distance between '{source}' and '{target}': {distance}")
print_matrix(D, source, target)