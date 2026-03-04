import numpy as np

# Generate a random dataset (100 samples, 5 features)
np.random.seed(0)
data = np.random.rand(100, 5)

# Calculate the mean of each feature
mean = np.mean(data, axis=0)

# Center the data
centered_data = data - mean

# Calculate the covariance matrix
cov_matrix = np.cov(centered_data, rowvar=False)

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Sort eigenvalues and eigenvectors in descending order
idx = np.argsort(-eigenvalues)
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

# Select top 2 principal components
top_components = eigenvectors[:, :2]

# Project data onto top components
projected_data = np.dot(centered_data, top_components)

print("Original Data Shape:", data.shape)
print("Projected Data Shape:", projected_data.shape)