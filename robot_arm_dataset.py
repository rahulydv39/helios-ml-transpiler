import numpy as np

# 1. Define the physical constraints of our robot
L1 = 5.0 # Length of first arm segment
L2 = 4.0 # Length of second arm segment
num_samples = 10000

# 2. Generate random angles (in radians)
# Restricting angles to 0 to pi/2 (0 to 90 degrees) to keep the math simple for Day 1
theta1 = np.random.uniform(0, np.pi/2, num_samples)
theta2 = np.random.uniform(0, np.pi/2, num_samples)

# 3. Calculate the resulting x and y coordinates (The Physics)
x = L1 * np.cos(theta1) + L2 * np.cos(theta1 + theta2)
y = L1 * np.sin(theta1) + L2 * np.sin(theta1 + theta2)

# 4. Stack them into inputs and targets for your Neural Network
# Inputs: Where the arm is (x, y)
X_data = np.column_stack((x, y))

# Targets: The angles required to get there (theta1, theta2)
Y_data = np.column_stack((theta1, theta2))

print(f"Generated {len(X_data)} samples.")
print(f"First input (x, y): {X_data[0]}")
print(f"First target (theta1, theta2): {Y_data[0]}")

# NOW: Feed X_data and Y_data into a tiny PyTorch or TensorFlow MLP.