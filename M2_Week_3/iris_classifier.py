import numpy as np

def load_iris_data(file_path):
    data = np.loadtxt(file_path, delimiter=',', dtype='str')
    return data

def split_features_labels(data):
    X = data[:, :-1].astype(float)
    y = data[:, -1]
    return X, y

def compute_prior_probabilities(y):
    unique_classes, counts = np.unique(y, return_counts=True)
    prior_probabilities = counts / len(y)
    return dict(zip(unique_classes, prior_probabilities))

def compute_gaussian_parameters(X, y):
    unique_classes = np.unique(y)
    parameters = {}
    
    for cls in unique_classes:
        X_cls = X[y == cls]
        parameters[cls] = {
            'mean': X_cls.mean(axis=0),
            'var': X_cls.var(axis=0)
        }
    
    return parameters

def gaussian_pdf(x, mean, var):
    exponent = np.exp(-((x - mean) ** 2 / (2 * var)))
    return (1 / np.sqrt(2 * np.pi * var)) * exponent

def predict(X, prior_probabilities, gaussian_parameters):
    predictions = []
    unique_classes = list(prior_probabilities.keys())
    
    for x in X:
        posteriors = []
        
        for cls in unique_classes:
            prior = np.log(prior_probabilities[cls])
            conditional = np.sum(np.log(gaussian_pdf(x, gaussian_parameters[cls]['mean'], gaussian_parameters[cls]['var'])))
            posterior = prior + conditional
            posteriors.append(posterior)
        
        predictions.append(unique_classes[np.argmax(posteriors)])
    
    return predictions

# Load and prepare data
iris_data = load_iris_data('./data/iris.data.txt')
X, y = split_features_labels(iris_data)

# Train the Gaussian Naive Bayes model
prior_probabilities = compute_prior_probabilities(y)
gaussian_parameters = compute_gaussian_parameters(X, y)

# Test samples
test_samples = np.array([
    [6.3, 3.3, 6.0, 2.5],
    [5.0, 2.0, 3.5, 1.0],
    [4.9, 3.1, 1.5, 0.1]
])

# Make predictions
predictions = predict(test_samples, prior_probabilities, gaussian_parameters)
print(predictions)
