This directory contains all my projects for 

# Links
1. [Project Q Login](https://quantum-computing.ibm.com/)
2. [IBM Quantum Computing ](https://www.ibm.com/quantum-computing/)
3. [QISkit Textbook](https://delapuente.github.io/qiskit-textbook/preface)


# Environment
Written for Debian/Ubuntu

## Ubuntu/Debian packages
```bash
apt-get install -y python3 python3-pip
pip3 install virtualenv
```

## Create Virtual Environment (virtualenv)
```bash
virtualenv qiskit-env
```
I don't upload my virtual environment because there is a lot of redundant
information in it that can be quickly and easily installed on any computer.
There are two ways to install packages:

### 1. Using requirements.txt
```bash
pip3 install -r requirements.txt
```

### 2. Directly install required packages
```bash
pip3 install jupyterlab qiskit matplotlib
```

## Starting Virtual Environment
```bash
source qiskit-env/bin/activate
```

## Exiting Virtual Environment
```bash
deactivate
```


# Circuits
## Initialize Quantum Circuit
```python
From qiskit import *
qr = QuantumRegister(2)
cr = Classical Register(2)
circuit = QuantumCircuit(qr, cr)
```

## Plotting Circuit States
```python
matplotlib inline
circuit.draw
```


# Gates
For more information reread
[this chapter](https://qiskit.org/textbook/ch-gates/quantum-gates.html)
on quantum gates. From: *qiskit.org*.

## Clifford Group
### Hadamard
A half rotation of the Bloch sphere around the axis half way between
the x-axis and z-axis. 
Effectively, this interchanges the x and z states. 
It is used in measuring x states.
```python
circuit.h(qbit_index)
```

### Pauli Matrices
```python
circuit.x(qbit_index)
circuit.y(qbit_index)
circuit.z(qbit_index)
```

### S and S-dagger Gates
The S gate S-dagger gates are roots of the X Pauli matrix.
Both are quarter turns of the Block shpere around the z axis.
The effectively interchange the states in the x and y directions.
They are used in measuring y states.
```python
circuit.s()   # S gate
circuit.sdg() # S dagger gate
```


## Other Single Qbit Gates
### Rotations in the Bloch Sphere
Rotations can be made around any principle axis (x,y,z) by an arbitrary angle
```python
circuit.rx(0, theta)  # Rotate qbit 0 around the x-axis by angle theta
circuit.ry(0, theta)  # Rotate qbit 0 around the x-axis by angle theta
circuit.rz(0, theta)  # Rotate qbit 0 around the x-axis by angle theta
```


## Multiple QBit Gates
### Controlled Not
```python
circuit.cx(control, target)  	   # Control Not
circuit.ccx(ctrl1, ctrl2, target)  # Toffoli CNot
circuit.cy(cotrol, target)	   # Controlled Y Not
circuit.cz(cotrol, target)	   # Controlled Z Not
```

### Multiple Controlled Unit 1
```python
circuit.mcu1()
```

### Multiple Controlled Rotation
```python
circuit.mcrx()
circuit.mcry()
circuit.mcrz()
```

### Multiple-Control Toffoli
```python
circuit.mct()
```

### Multi-Control, Multi-Target
```python
cricuit.mcmt()
```

### Logical AND
```python
cricuit.logical_and()
```

### Logical OR
```python
cricuit.logical_or()
```

### Controlled-RY
```python
cricuit.cry()
```

### 2-Control/3-control Relative-Phase Toffoli
```python
cricuit.rccx()
cricuit.rcccx()
```


## Tensor Products (Composite Gates)
Viewing matrix representations of sequential gates:
```python
from qiskit import Aer
unitary_simulator = Aer.get_backend('unitary_simulator')
circuit = QuantumCircuit()
## Perform gate operations
gate = execute(circuit, unitary_simulator).result.get_unitary()

# Display in LaTeX
from IPython.display import display, Markdown, Latex
gate_latex = '\\begin{pmatrix}'
for line in gate:
    for element in line:
        gate_latex += str(element) + '&'
    gate_latex  = gate_latex[0:-1]
    gate_latex +=  '\\\\'
gate_latex  = gate_latex[0:-2]
gate_latex += '\end{pmatrix}'
display(Markdown(gate_latex))
```
