import pennylane as qml
import numpy as np
from data_generation import output_file, n_qubits, num_layers, epochs

# Set up the quantum device
dev = qml.device("default.qubit", wires=n_qubits)

# Define the QNN circuit that receives a product state vector as input.
def qnn(product_state, params):
    # Prepare the quantum state using AmplitudeEmbedding.
    # Set normalize=False if the product states are already normalized.
    qml.AmplitudeEmbedding(product_state, wires=range(n_qubits), normalize=False)
    # Apply a variational circuit; here we use BasicEntanglerLayers as an example.
    qml.BasicEntanglerLayers(params, wires=range(n_qubits))
    # Measure an observable (e.g., expectation value of PauliZ on qubit 0)
    return qml.expval(qml.PauliZ(0))

@qml.qnode(dev)
def circuit(product_state, params):
    return qnn(product_state, params)

# Function to load product states from the output file.
def load_product_states(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()
    states = []
    for line in lines:
        # Each line contains space-separated float numbers representing a state vector.
        state_values = list(map(float, line.strip().split()))
        state = np.array(state_values)
        states.append(state)
    return states

# Load product states from the data file.
product_states = load_product_states(output_file)

# For demonstration, assign random binary labels to each product state.
labels = np.random.choice([0, 1], size=len(product_states))

# Initialize variational parameters for the circuit.
params = qml.numpy.random.randn(num_layers, n_qubits)

# Set up an optimizer and define the number of training epochs.
opt = qml.GradientDescentOptimizer(stepsize=0.1)

# Training loop: Update the parameters to minimize a simple mean-squared error loss.
for epoch in range(epochs):
    for product_state, label in zip(product_states, labels):
        # Define the cost function for the current product state and label.
        def cost(params):
            prediction = circuit(product_state, params)
            return (prediction - label) ** 2
        
        params = opt.step(cost, params)
    
    # Optionally, print the average loss every 10 epochs.
    if epoch % 10 == 0:
        losses = [(circuit(ps, params) - lbl) ** 2 for ps, lbl in zip(product_states, labels)]
        loss_val = np.mean(losses)
        print(f"Epoch {epoch}, Loss: {loss_val}")

print("Training complete!")
