import tensorflow as tf
import numpy as np

# load trained model
model = tf.keras.models.load_model("robot_arm_model.h5", compile=False)

# choose a target position
x = 7.0
y = 3.0

# convert to model input
input_data = np.array([[x, y]])

# predict angles
prediction = model.predict(input_data)

theta1 = prediction[0][0]
theta2 = prediction[0][1]

print("Target position:", x, y)
print("Predicted theta1:", theta1)
print("Predicted theta2:", theta2)