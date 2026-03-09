import tensorflow as tf
from robot_arm_dataset import X_data, Y_data

# Build neural network: 2 → 16 → 16 → 2
model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation='tanh', input_shape=(2,)),
    tf.keras.layers.Dense(16, activation='tanh'),
    tf.keras.layers.Dense(2)
])

# Compile model
model.compile(
    optimizer=tf.keras.optimizers.Adam(0.001),
    loss='mse'
)

# Train model
model.fit(
    X_data,
    Y_data,
    epochs=500,
    batch_size=32,
    validation_split=0.2
)

# Save trained model
model.save("robot_arm_model.keras")