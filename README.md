# LessgoGrover - Quantum vs Classical Search

![Qiskit](https://img.shields.io/badge/Qiskit-Quantum-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-Interactive-red) ![Python](https://img.shields.io/badge/Python-3.8+-brightgreen)

## Overview
LessgoGrover is an interactive Streamlit web application that compares classical search algorithms with Grover's quantum search algorithm. This project demonstrates how quantum computing can significantly speed up search tasks over large, unsorted databases.

## Features
- **Classical Search**: Implements a linear search algorithm.
- **Grover's Algorithm**: Uses Qiskit to simulate quantum search.
- **Performance Comparison**: Graphical comparison of classical vs quantum search time complexities.
- **Interactive Visualization**: Displays search results using histograms.
- **User Input Options**: Allows users to test different target states and qubit numbers.

## Technologies Used
- **Qiskit**: Quantum computing framework for Grover's algorithm.
- **Streamlit**: Web interface for interactive visualization.
- **Matplotlib & NumPy**: Graph plotting and mathematical computations.

---

## Understanding the Concepts
### Classical Search (Linear Search)
In an unsorted list, finding an element requires checking each element one by one. This results in a time complexity of **O(N)**, meaning the search time scales linearly with the dataset size.

```python
for i, element in enumerate(data):
    if element == target:
        index = i
        break
```

### Grover's Algorithm (Quantum Search)
Grover’s algorithm achieves a quadratic speedup, reducing the search time complexity to **O(√N)**.

#### Key Steps:
1. **Superposition**: Initialize qubits to an equal probability state using Hadamard gates.
2. **Oracle Function**: Flips the phase of the target state.
3. **Diffusion Operator**: Amplifies the probability of the target state.
4. **Measurement**: Collapses qubits to obtain the result.

```python
qc.h(range(num_qubits))
# Apply Grover Oracle and Diffusion Operator
qc.measure(range(num_qubits), range(num_qubits))
```

---

## Performance Comparison
### Time Complexity Analysis
| Search Type  | Time Complexity |
|-------------|---------------|
| Classical (Linear) | O(N) |
| Quantum (Grover) | O(√N) |

### Sample Execution Times (Simulated)
- **Classical Search (N=1024):** ~1.02s
- **Quantum Search (N=1024):** ~0.04s

Graphs in the application visualize this speedup, showing how Grover’s algorithm outperforms classical search as dataset size increases.

---

## Running the Project
### Prerequisites
Ensure you have Python 3.8+ installed. Install dependencies using:

```sh
pip install -r requirements.txt
```

### Running the Streamlit App
```sh
streamlit run app.py
```

### Running Qiskit Tests
```sh
python test_qiskit.py
```

---

## Results & Visualization
The application allows users to:
- Compare search times for different database sizes.
- Test classical and quantum searches with custom inputs.
- View histograms of quantum search results.

## Example Output
```
Classical Search: Target found at index 47, Time taken: 1.02s
Quantum Search (Grover’s Algorithm): Execution time: 0.04s
Measurement Results: {'101111': 890, '111111': 134}
```

![Quantum Histogram](https://raw.githubusercontent.com/SujayKulkarni-2211/LessgoGrover/main/histogram.png)

---

## Future Enhancements
- **Real Quantum Hardware Execution**: Extend to IBM Quantum devices.
- **Custom Oracle Implementation**: Enhance flexibility in search criteria.
- **Improved UI/UX**: Add animations and real-time search simulations.

## Contributors
[Sujay Kulkarni](https://github.com/SujayKulkarni-2211)

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

