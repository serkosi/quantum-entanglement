import product_states as ps

# Centralized parameters for the project
output_file = "data/product_states.txt"
num_states = 10
n_qubits = 4
num_layers = 5  # Example number of layers for training
epochs = 50

# Generate and save product states
with open(output_file, "w") as file:
    for i in range(num_states):
        product_state = ps.generate_product_state(n_qubits)
        file.write(" ".join(map(str, product_state)) + "\n")

print(f"{num_states} product states written to {output_file}")