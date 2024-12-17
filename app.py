from qiskit_aer import AerSimulator
from qiskit import transpile, QuantumCircuit
from qiskit.visualization import plot_histogram
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time


# Classical Search: Linear Search
def classical_search(target, data):
    start_time = time.time()
    for i, element in enumerate(data):
        if element == target:
            index = i
            break
    end_time = time.time()
    return index, (end_time - start_time)


# Grover's Algorithm: Quantum Search
def grover_algorithm(target, num_qubits):
    qc = QuantumCircuit(num_qubits, num_qubits)

    # Step 1: Initialize qubits in superposition (Hadamard)
    qc.h(range(num_qubits))

    # Step 2: Oracle (flip phase of the target state)
    for i, bit in enumerate(target):
        if bit == '0':
            qc.x(i)
    
    # Apply the Grover oracle: multi-controlled X (to flip target)
    qc.h(num_qubits - 1)
    qc.mcx(list(range(num_qubits - 1)), num_qubits - 1)
    qc.h(num_qubits - 1)
    
    # Step 3: Apply Diffusion Operator (inversion about the average)
    qc.h(range(num_qubits))
    qc.x(range(num_qubits))
    qc.h(num_qubits - 1)
    qc.mcx(list(range(num_qubits - 1)), num_qubits - 1)
    qc.h(num_qubits - 1)
    qc.x(range(num_qubits))
    qc.h(range(num_qubits))

    # Step 4: Measure the qubits
    qc.measure(range(num_qubits), range(num_qubits))
    return qc


# Run Grover's Algorithm (Quantum Search)
def run_grover(num_qubits, target):
    simulator = AerSimulator()
    qc = grover_algorithm(target, num_qubits)
    transpiled_qc = transpile(qc, simulator)

    # Time the quantum search
    start_time = time.time()
    result = simulator.run(transpiled_qc, shots=1024).result()
    end_time = time.time()
    
    counts = result.get_counts()
    execution_time = end_time - start_time

    return counts, execution_time


# Streamlit App
def main():
    st.title("Classical vs Quantum Search - Grover's Algorithm")
    st.write("### Compare Grover's Algorithm with Classical Search for an Unsorted Database")

    # Graph 1: Time Complexity Comparison O(N) vs O(sqrt(N))
    st.write("### Pre-generated Time Complexity Comparison: O(N) vs O(sqrt(N))")
    fig, ax = plt.subplots()
    n_range = np.arange(1, 21)  # Logarithmic scale for better comparison
    classical_times = n_range  # O(N) time complexity
    quantum_times = np.sqrt(n_range)  # O(sqrt(N)) time complexity (Grover's search)
    
    ax.plot(n_range, classical_times, label="Classical Search Time (O(N))", color="blue")
    ax.plot(n_range, quantum_times, label="Quantum Search Time (O(sqrt(N)))", color="red")
    ax.set_xlabel("Database Size (N)")
    ax.set_ylabel("Time (arbitrary units)")
    ax.set_title("Time Complexity Comparison")
    ax.legend()

    st.pyplot(fig)

    # Graph 2: Classical vs Quantum Search Time for Database Sizes from 2^4 to 1 million
    st.write("### Pre-generated Classical vs Quantum Search Time Comparison (Database Sizes from 2^4 to 1 million)")

    db_sizes = [2**i for i in range(4, 21)] + [1000000]  # Sizes: 2^4 to 2^20 and 1 million
    classical_search_times = []
    quantum_search_times = []

    for size in db_sizes:
        data = [bin(i)[2:].zfill(int(np.log2(size))) for i in range(size)]  # Unsorted database

        # Classical search time
        _, classical_time = classical_search('1' * int(np.log2(size)), data)
        classical_search_times.append(classical_time)
        
        # Quantum search time (Grover's algorithm)
        _, quantum_time = run_grover(int(np.log2(size)), '1' * int(np.log2(size)))
        quantum_search_times.append(quantum_time)

    fig, ax = plt.subplots()
    ax.plot(db_sizes, classical_search_times, label="Classical Search Time", color="blue")
    ax.plot(db_sizes, quantum_search_times, label="Quantum Search (Grover) Time", color="red")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Database Size (N)")
    ax.set_ylabel("Time (seconds)")
    ax.set_title("Classical vs Quantum Search Time (Log Scale)")
    ax.legend()

    st.pyplot(fig)

    # User Input for Number of Qubits and Target State
    num_qubits = st.number_input("Enter the number of qubits (4 to 30 recommended):", min_value=4, max_value=30, value=4, step=1)
    
    # Default target state is all 1s based on number of qubits
    default_target = '1' * num_qubits
    target_state = st.text_input(f"Enter a {num_qubits}-bit target state (e.g., '1111'):", value=default_target)

    # Validation for target state length
    if len(target_state) != num_qubits or not set(target_state).issubset({"0", "1"}):
        st.error(f"Target state must be {num_qubits}-bit long and contain only 0s and 1s.")
        return

    # Classical Search
    st.write("### Running Classical Search...")
    data = [bin(i)[2:].zfill(num_qubits) for i in range(2**num_qubits)]  # Unsorted database
    classical_index, classical_time = classical_search(target_state, data)
    st.write(f"**Classical Search:** Target found at index {classical_index}, Time taken: {classical_time:.5f} seconds")

    # Grover's Algorithm
    st.write("### Running Quantum Search (Grover's Algorithm)...")
    grover_results, grover_time = run_grover(num_qubits, target_state)
    st.write(f"**Quantum Search (Grover's Algorithm):** Execution time: {grover_time:.5f} seconds")

    # Display Grover's Results
    st.write("### Measurement Results (Quantum Search - Grover's Algorithm):")
    st.write(grover_results)

    # Plot Histogram
    fig, ax = plt.subplots()
    plot_histogram(grover_results, ax=ax)
    st.pyplot(fig)

    # Comparison of Classical vs Quantum Search
    st.write("### Comparison of Classical vs Quantum Search:")
    st.write(f"- Classical Search Time: {classical_time:.5f} seconds")
    st.write(f"- Quantum Search (Grover's Algorithm) Time: {grover_time:.5f} seconds")

    # Display Time Overheads
    st.write("### Time Overheads Comparison:")
    quantum_overhead = grover_time - classical_time
    st.write(f"- **Quantum Overhead** (Grover): {quantum_overhead:.5f} seconds")

if __name__ == "__main__":
    main()
