from qiskit_aer import AerSimulator
from qiskit import QuantumCircuit, transpile

# Simple test circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

simulator = AerSimulator()
transpiled_qc = transpile(qc, simulator)
result = simulator.run(transpiled_qc, shots=1024).result()

print("Qiskit Aer Test Successful! Results:", result.get_counts())

