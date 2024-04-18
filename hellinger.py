import numpy as np

inner_sum = 0
p = [0.5316231756,
0.4674922601,
0.0008845643521
]
q = [0.5276422764,
0.4699186992,
0.00243902439
]
r = [0.5264158115,
0.4697833523,
0.003800836184
]

for i in range(len(p)):
    temp = np.sqrt(q[0]) - np.sqrt(r[0])
    inner_sum += (temp ** 2)

dist = np.sqrt(inner_sum) / np.sqrt(2)

print(dist)