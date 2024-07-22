import numpy as np

def compute_cosine(v1, v2):
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    cos_sim = dot_product / (norm_v1 * norm_v2)
    return cos_sim

# Example usage
x = np.array([1, 2, 3, 4])
y = np.array([1, 0, 3, 0])

cosine_similarity = compute_cosine(x, y)
print("Cosine Similarity:", cosine_similarity)
