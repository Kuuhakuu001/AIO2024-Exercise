import numpy as np


def create_train_data():
    data = [
        ['Sunny', 'Hot', 'High', 'Weak', 'No'],
        ['Sunny', 'Hot', 'High', 'Strong', 'No'],
        ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
        ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
        ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
        ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
        ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
        ['Overcast', 'Mild', 'High', 'Weak', 'No'],
        ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
        ['Rain', 'Mild', 'Normal', 'Weak', 'Yes']
    ]
    return np.array(data)

train_data = create_train_data()
print(train_data)

def compute_prior_probability(train_data):
    y_unique, counts = np.unique(train_data[:, -1], return_counts=True)
    prior_probability = counts / len(train_data)
    return prior_probability

prior_probability = compute_prior_probability(train_data)
print("P(Play Tennis = No):", prior_probability[0])
print("P(Play Tennis = Yes):", prior_probability[1])


def compute_conditional_probability(train_data):
    y_unique = ['No', 'Yes']
    conditional_probability = []
    list_x_name = []

    for i in range(train_data.shape[1] - 1):
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)
        x_conditional_probability = np.zeros((len(y_unique), len(x_unique)))

        for j, y in enumerate(y_unique):
            y_count = np.sum(train_data[:, -1] == y)
            for k, x in enumerate(x_unique):
                xy_count = np.sum((train_data[:, i] == x) & (train_data[:, -1] == y))
                x_conditional_probability[j, k] = xy_count / y_count
        
        conditional_probability.append(x_conditional_probability)

    return conditional_probability, list_x_name

conditional_probability, list_x_name = compute_conditional_probability(train_data)
print("x1 =", list_x_name[0])
print("x2 =", list_x_name[1])
print("x3 =", list_x_name[2])
print("x4 =", list_x_name[3])

def get_index_from_value(feature_name, list_features):
    return np.where(list_features == feature_name)[0][0]

train_data = create_train_data()
_, list_x_name = compute_conditional_probability(train_data)
outlook = list_x_name[0]

i1 = get_index_from_value("Overcast", outlook)
i2 = get_index_from_value("Rain", outlook)
i3 = get_index_from_value("Sunny", outlook)

print(i1, i2, i3)

train_data = create_train_data()
conditional_probability, list_x_name = compute_conditional_probability(train_data)
x1 = get_index_from_value("Sunny", list_x_name[0])
print("P('Outlook'='Sunny'|Play Tennis='Yes') =", np.round(conditional_probability[0][1, x1], 2))


train_data = create_train_data()
conditional_probability, list_x_name = compute_conditional_probability(train_data)
x1 = get_index_from_value("Sunny", list_x_name[0])
print("P('Outlook'='Sunny'|Play Tennis='No') =", np.round(conditional_probability[0][0, x1], 2))

def train_naive_bayes(train_data):
    prior_probability = compute_prior_probability(train_data)
    conditional_probability, list_x_name = compute_conditional_probability(train_data)
    return prior_probability, conditional_probability, list_x_name

def prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability):
    x1 = get_index_from_value(X[0], list_x_name[0])
    x2 = get_index_from_value(X[1], list_x_name[1])
    x3 = get_index_from_value(X[2], list_x_name[2])
    x4 = get_index_from_value(X[3], list_x_name[3])
    
    p0 = prior_probability[0]
    p1 = prior_probability[1]
    
    p0 *= conditional_probability[0][0, x1]
    p0 *= conditional_probability[1][0, x2]
    p0 *= conditional_probability[2][0, x3]
    p0 *= conditional_probability[3][0, x4]
    
    p1 *= conditional_probability[0][1, x1]
    p1 *= conditional_probability[1][1, x2]
    p1 *= conditional_probability[2][1, x3]
    p1 *= conditional_probability[3][1, x4]
    
    if p0 > p1:
        y_pred = 0
    else:
        y_pred = 1

    return y_pred

X = ['Sunny', 'Cool', 'High', 'Strong']
data = create_train_data()
prior_probability, conditional_probability, list_x_name = train_naive_bayes(data)
pred = prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability)

if pred:
    print("Ad should go!")
else:
    print("Ad should not go!")
