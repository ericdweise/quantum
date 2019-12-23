This directory contains all my projects for 

# Links
[Project Q Login](https://quantum-computing.ibm.com/)
[IBM Quantum Computing ](https://www.ibm.com/quantum-computing/)


# Installing Packages
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
I don't upload y virtual environment because there is a lot of redundant
information in it that can be quickly and easily installed on any computer.
There are two ways to install packages:

### 1. Using requirements.txt
```bash
pip3 install -r requirements.txt
```

### 2. Directly install required packages
```bash
pip3 install jupyterlab qiskit
```

## Starting Virtual Environment
```bash
source qiskit-env/bin/activate
```

## Exiting Virtual Environment
```bash
deactivate
```
