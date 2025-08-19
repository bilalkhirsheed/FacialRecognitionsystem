'''import tensorflow as tf

# Check available GPUs
gpus = tf.config.list_physical_devices('GPU')
print("Num GPUs Available: ", len(gpus))

if gpus:
    print("GPU Device: ", gpus)
else:
    print("No GPU detected.")
'''

"""
    import torch

# Check the number of GPUs available
gpu_count = torch.cuda.device_count()
print(f"Number of GPUs available: {gpu_count}")

# If a GPU is available, get its name
if gpu_count > 0:
    for i in range(gpu_count):
        print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
else:
    print("No GPU found.")

    """
    
    
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Define a simple model
model = Sequential([
    Dense(32, input_shape=(10,), activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Create some dummy data
X = np.random.rand(100, 10)
y = np.random.randint(2, size=(100, 1))

# Train the model
model.fit(X, y, epochs=5, batch_size=10)

# Save the weights
model.save_weights('simple_model.weights.h5')

# Load the weights into a new model with the same architecture
new_model = Sequential([
    Dense(32, input_shape=(10,), activation='relu'),
    Dense(1, activation='sigmoid')
])
new_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Load the saved weights
new_model.load_weights('simple_model.weights.h5')

# Print the loaded weights
print(new_model.get_weights())
