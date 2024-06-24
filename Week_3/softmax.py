import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        return torch.exp(x) / torch.sum(torch.exp(x), dim=0)


class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, x):
        c = torch.max(x)
        return torch.exp(x - c) / torch.sum(torch.exp(x - c), dim=0)


# Examples 1
data = torch.Tensor([1, 2, 3])
softmax = Softmax()
output = softmax(data)
print(output)
# >> tensor([0.0900, 0.2447, 0.6652])

softmax_stable = SoftmaxStable()
output = softmax_stable(data)
print(output)
# >> tensor([0.0900, 0.2447, 0.6652])
