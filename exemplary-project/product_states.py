import numpy as np

# Function to generate a random single-qubit state
def random_qubit_state():
    # Generate random numbers for the amplitudes
    alpha, beta = np.random.random(2)
    # Normalize to ensure |alpha|^2 + |beta|^2 = 1
    norm = np.sqrt(alpha**2 + beta**2)
    alpha, beta = alpha / norm, beta / norm
    return np.array([alpha, beta])

# Function to create an n-qubit product state
def generate_product_state(n):
    # Generate random single-qubit states for each qubit
    state = np.array([1.0])  # Start with scalar value for tensor product
    for _ in range(n):
        qubit_state = random_qubit_state()
        state = np.kron(state, qubit_state)  # Tensor product with the previous state
    return state

# Ensure this code runs only when the script is executed directly
if __name__ == "__main__":
    # Example: Generate a 3-qubit product state
    n_qubits = 3
    product_state = generate_product_state(n_qubits)

    # Display the generated state
    print("Generated Product State:", product_state)