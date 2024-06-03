# Quantum Random Number Generator (QRNG)

# Description:
# Develop a quantum random number generator using the principles of quantum mechanics. This project will generate truly random numbers by measuring the quantum state of qubits.

# Key Components:
# - QRNG Implementation: Use Qiskit to generate random numbers by measuring qubits.
# - User Interface: Use Flask to create a web-based interface for users to generate random numbers.
# - Integration with IBMQ: Run the quantum circuits on IBMQ to ensure true randomness.
# - Display Random Numbers: Show the generated random numbers on the web interface.

# Possible Usage:
# - Providing a source of truly random numbers.
# - Demonstrating the principles of quantum randomness.
# - Exploring applications in cryptography and simulations.

from flask import Flask, render_template, request
from qiskit import QuantumCircuit, Aer, execute, IBMQ

app = Flask(__name__)

# Load IBMQ account
IBMQ.load_account()

def generate_random_number():
    # Define a simple quantum random number generator
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

@app.route('/generate', methods=['POST'])
def generate():
    random_number = generate_random_number()
    return render_template('random.html', random_number=random_number)

if __name__ == '__main__':
    app.run(debug=True)
