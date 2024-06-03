# Quantum Cryptography Simulator

# Description:
# Build a simulator for quantum key distribution (QKD) protocols like BB84. This project will demonstrate the principles of quantum cryptography and how it can be used to securely share keys between two parties.

# Key Components:
# - QKD Protocol Implementation: Implement the BB84 protocol using Qiskit.
# - User Interface: Use Flask to create a web-based interface where users can initiate key distribution sessions.
# - Integration with IBMQ: Connect to IBMQ to run the quantum circuits and generate keys.
# - Visualization: Display the quantum states and the process of key distribution.

# Possible Usage:
# - Educating about quantum cryptography.
# - Demonstrating secure key exchange.
# - Analyzing the impact of eavesdropping.

from flask import Flask, render_template, request
from qiskit import QuantumCircuit, Aer, execute, IBMQ

app = Flask(__name__)

# Load IBMQ account
IBMQ.load_account()

def bb84_protocol():
    # Define a simple BB84 protocol implementation
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator).result()
    counts = result.get_counts()
    return counts

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run():
    counts = bb84_protocol()
    return render_template('result.html', counts=counts)

if __name__ == '__main__':
    app.run(debug=True)
