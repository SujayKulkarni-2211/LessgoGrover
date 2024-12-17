from qiskit_aer import AerSimulator
from qiskit import QuantumCircuit, transpile

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

simulator = AerSimulator()
result = simulator.run(transpile(qc, simulator), shots=1024).result()

print("Qiskit works! Results:", result.get_counts())
