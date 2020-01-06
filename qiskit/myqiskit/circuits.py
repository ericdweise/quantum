from qiskit import QuantumCircuit


def encode_int(number, bit_depth=8):
    '''Encode an integer into a quantum circuit.'''
    assert(isinstance(number, int))
    assert(isinstance(bit_depth, int))
    assert(bit_depth > 0)
    assert(number >= 0)
    assert(number <= 2**bit_depth - 1)

    circuit = QuantumCircuit(bit_depth)
    for i in range(bit_depth, -1, -1):
        bit_power = 2**i
        if number >= bit_power:
            circuit.x(i)
            number -= bit_power

    return circuit
