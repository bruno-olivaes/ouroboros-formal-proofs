import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector

print("Iniciando Simulação Ab-Initio: Criptografia Quântica")
print("Executando Grover's Algorithm vs Hash Dinâmico Ouroboros...")

n_qubits = 4
N = 2**n_qubits

# A senha real que o hacker quer descobrir
target_state_standard = '1111'

def phase_oracle(qc, n, target_state_bin):
    # Aplica um phase-flip (-1) apenas no estado alvo
    oracle_matrix = np.eye(2**n)
    target_idx = int(target_state_bin, 2)
    oracle_matrix[target_idx, target_idx] = -1
    
    # Adicionando a matriz customizada ao circuito
    qc.unitary(oracle_matrix, range(n), label=f"Oracle({target_state_bin})")

def diffuser(qc, n):
    # Amplificador de Amplitude (Inversão sobre a Média)
    qc.h(range(n))
    qc.x(range(n))
    
    # Multi-controlled Z gate
    qc.h(n-1)
    qc.mcx(list(range(n-1)), n-1)
    qc.h(n-1)
    
    qc.x(range(n))
    qc.h(range(n))

sim = AerSimulator()
shots = 2000

max_iterations = 6
iterations_list = list(range(1, max_iterations + 1))

prob_standard = []
prob_ouroboros = []

# O Relógio Acústico Módulo-9 (A Chave de Ouroboros muda o alvo no espaço-tempo)
# Se o hacker demora 1 iteração quântica, a topologia empurra a fechadura para o próximo estado harmônico
ouroboros_sequence = ['1111', '1110', '1100', '1000', '0000', '0001']

print("Rodando simulações quânticas (Isso requer construção pesada de matrizes unitárias)...")

for iters in iterations_list:
    # -------------------------------------------------------------
    # 1. Hack Padrão (Grover em Criptografia Clássica)
    # -------------------------------------------------------------
    qc_std = QuantumCircuit(n_qubits, n_qubits)
    qc_std.h(range(n_qubits)) # Sobreposição
    
    for i in range(iters):
        # O Oráculo é estático (a senha não muda enquanto ele calcula)
        phase_oracle(qc_std, n_qubits, target_state_standard)
        diffuser(qc_std, n_qubits)
        
    qc_std.measure(range(n_qubits), range(n_qubits))
    job_std = sim.run(transpile(qc_std, sim), shots=shots)
    counts_std = job_std.result().get_counts()
    
    prob_std = counts_std.get(target_state_standard, 0) / shots
    prob_standard.append(prob_std)
    
    # -------------------------------------------------------------
    # 2. Hack contra Ouroboros (Hash Topológico Dinâmico)
    # -------------------------------------------------------------
    qc_our = QuantumCircuit(n_qubits, n_qubits)
    qc_our.h(range(n_qubits)) # Sobreposição
    
    # O hacker está tentando achar '1111'
    hacker_target = '1111'
    
    for i in range(iters):
        # A defesa Módulo-9: A cada iteração que o algoritmo leva para rodar,
        # o oráculo rotaciona a fase do estado alvo para o próximo harmônico.
        current_target = ouroboros_sequence[i % len(ouroboros_sequence)]
        phase_oracle(qc_our, n_qubits, current_target)
        diffuser(qc_our, n_qubits)
        
    qc_our.measure(range(n_qubits), range(n_qubits))
    job_our = sim.run(transpile(qc_our, sim), shots=shots)
    counts_our = job_our.result().get_counts()
    
    # O hacker checa se achou a senha que ele queria ('1111')
    prob_our = counts_our.get(hacker_target, 0) / shots
    prob_ouroboros.append(prob_our)


# ========================================================
# RENDERIZAÇÃO DO RESULTADO CRU
# ========================================================
plt.figure(figsize=(10, 6))

plt.plot(iterations_list, prob_standard, 'b-o', linewidth=2.5, label='Hackeamento Padrão (Oráculo Estático)')
plt.plot(iterations_list, prob_ouroboros, 'r-o', linewidth=2.5, label='Criptografia Ouroboros (Hash Topológico Dinâmico)')

# A probabilidade de sucesso teórica máxima do Grover para 4 qubits (N=16) ocorre perto de 3 iterações (pi/4 * sqrt(16))
plt.axvline(x=3, color='gray', linestyle='--', alpha=0.5, label='Convergência Ótima de Grover ($M \\approx 3$)')

plt.title('Defesa Contra Computador Quântico Ab-Initio\nFalha de Amplificação de Amplitude (Algoritmo de Grover)', fontsize=14, fontweight='bold')
plt.xlabel('Iterações do Oráculo de Grover', fontsize=12)
plt.ylabel('Probabilidade de Descobrir a Senha', fontsize=12)
plt.legend(loc='upper right', fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig('crypto_grover_ab_initio.png', dpi=300)
print("\nCálculo Físico concluído. Gráfico salvo em 'crypto_grover_ab_initio.png'.")
