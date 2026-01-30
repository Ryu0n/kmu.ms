import numpy as np


def cross_entropy(P, Q):
    return sum([-P[i] * np.log2(Q[i]) for i in range(len(P))])


P = [1, 0]
# Q = [1, 0]
# print(cross_entropy(P, Q))

Q = [0.8, 0.2]
print(cross_entropy(P, Q))

Q = [0.5, 0.5]
print(cross_entropy(P, Q))

Q = [0.2, 0.8]
print(cross_entropy(P, Q))


P = [0.23, 0.22, 0.25, 0.19, 0.11]
entropy = sum([-p*np.log2(p) for p in P])
print(entropy)
