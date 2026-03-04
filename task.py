import numpy as np

# Create numbers from 1 to 100000
data = np.arange(1, 100001)

# Shuffle the numbers randomly
np.random.shuffle(data)

# Reshape into rows and columns (example: 1000 x 100)
dataset = data.reshape(1000, 100)

print("Dataset shape:", dataset.shape)
print(dataset)