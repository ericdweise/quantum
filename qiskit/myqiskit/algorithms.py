from math import pi


def fourier_transform(circuit):
    """Perform an n-qbit QFT on a Quanutm circuit."""
    for j in range(circuit.n_qubits):
        circuit.h(circuit.qubits[j])
        for k in range(j+1, circuit.n_qubits):
            circuit.cu1(pi/float(2**(k-j)), circuit.qubits[k], circuit.qubits[j])
        circuit.barrier()
