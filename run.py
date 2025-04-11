import product_states as ps

# File to store the generated product states
output_file = "data/product_states.txt"

# Number of product states to generate
num_states = 10
n_qubits = 3  # Number of qubits per product state

# Generate and save product states
with open(output_file, "w") as file:
    for i in range(num_states):
        product_state = ps.generate_product_state(n_qubits)
        file.write(" ".join(map(str, product_state)) + "\n")

print(f"{num_states} product states written to {output_file}")