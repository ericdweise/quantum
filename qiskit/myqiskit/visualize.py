from math import floor

from qiskit import *
from IPython.display import display, Markdown, Latex


unitary_simulator = Aer.get_backend('unitary_simulator')
statevector_simulator = Aer.get_backend('statevector_simulator')


def complex_pretty(c):
    if c.imag == 0 and c.real == 0:
        return '0'

    elif c.imag == 0:
        if c.real == floor(c.real):
            return str(int(c.real))
        else:
            return f'{c.real:.2f}'

    elif c.real == 0:
        if c.imag == floor(c.imag):
            return f'{int(c.imag)}j'
        else:
            return f'{c.imag:.2f}j'

    if c.real == floor(c.real):
        rp = f'{int(c.real)}'
    else:
        rp = f'{c.real:.2f}'

    if c.imag > 0:
        op = ' + '
        if c.imag == floor(c.imag):
            ip = f'{int(c.imag)}'
        else:
            ip = f'{c.imag:.2f}'

    else:
        op = ' - '
        if c.imag == floor(c.imag):
            ip = f'{-int(c.imag)}'
        else:
            ip = f'{-c.imag:.2f}'

    return(rp + op + ip + 'j')


def get_unitary(circuit):
    job = execute(circuit, unitary_simulator)
    result = job.result()
    return result.get_unitary()

def matrix_pretty(circuit):
    gate = get_unitary(circuit)
    gate_latex = '\\begin{pmatrix}'
    for line in gate:
        for element in line:
            gate_latex += complex_pretty(element) + '&'
        gate_latex  = gate_latex[0:-1]
        gate_latex +=  '\\\\'
    gate_latex  = gate_latex[0:-2]
    gate_latex += '\end{pmatrix}'
    display(Markdown(gate_latex))


def statevector(circuit):
    job = execute(circuit, statevector_simulator)
    result = job.result()
    return result.get_statevector()


def statevector_pretty(circuit):
    svector = statevector(circuit)
    latex = '\\begin{pmatrix}'
    for element in svector:
        latex += complex_pretty(element)
        latex +=  '\\\\'
    latex  = latex[0:-2]
    latex += '\end{pmatrix}'
    display(Markdown(latex))
