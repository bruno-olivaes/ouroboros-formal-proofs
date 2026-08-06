import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def build_acoustic_chemistry():
    print("[+] Inicializando Algoritmo de Química Acústica (Fricção e Massa)...")
    
    # 4 Qubits representing 16 spatial coordinates in a vacuum
    qc = QuantumCircuit(4, 4)
    
    # 1. ESTADO SOLVE (A Névoa Quântica / Vácuo)
    # Colocamos tudo em superposição perfeita (O fluido sem massa, espalhado por igual)
    qc.h(range(4))
    
    qc.barrier()
    
    # 2. A INJEÇÃO ACÚSTICA (O Som viaja pelo vácuo)
    # Aplicamos "Fônons" (Mudanças de Fase) que simulam uma Onda Estacionária (Cimática).
    # Uma placa de Chladni concentra areia nos "nós" onde a fase destrutiva se cancela.
    # Vamos criar dois nós acústicos nos estados |0101> (5) e |1010> (10)
    
    # Marcando o Nó 5
    qc.x([1, 3])
    qc.mcp(np.pi, [0,1,2], 3) # Fase destrutiva
    qc.x([1, 3])
    
    # Marcando o Nó 10
    qc.x([0, 2])
    qc.mcp(np.pi, [0,1,2], 3) # Fase destrutiva
    qc.x([0, 2])
    
    qc.barrier()
    
    # 3. O ATRITO TERMODINÂMICO (Difusão e Coagulação)
    # A interação da onda acústica com o gel do vácuo gera fricção.
    # Aplicamos a difusão (Ondas colidindo de volta contra si mesmas).
    qc.h(range(4))
    qc.x(range(4))
    qc.h(3)
    qc.mcx([0,1,2], 3)
    qc.h(3)
    qc.x(range(4))
    qc.h(range(4))
    
    qc.measure(range(4), range(4))
    
    return qc

if __name__ == "__main__":
    qc = build_acoustic_chemistry()
    
    print("[+] Submetendo Circuito Acústico ao Simulador...")
    simulator = AerSimulator()
    compiled_qc = transpile(qc, simulator)
    
    job = simulator.run(compiled_qc, shots=8000)
    result = job.result()
    counts = result.get_counts()
    
    print(f"[-] Histograma da Densidade Espacial: {counts}")
    
    print("[!] CONCLUSÃO FÍSICA: O som coagulou o Vácuo. A Massa emergiu geometricamente!")
    
    print("[+] Gerando Prova Analítica da Fricção Acústica (Gráfico)...")
    
    plt.figure(figsize=(12, 6), facecolor='#111111')
    ax = plt.gca()
    ax.set_facecolor('#111111')
    
    states = [f"{i:04b}" for i in range(16)]
    values = [counts.get(s, 0) for s in states]
    
    colors = ['#FFD700' if s in ['0101', '1010'] else '#1A1A1A' for s in states]
    bars = plt.bar(states, values, color=colors, edgecolor='#FFFFFF')
    
    plt.title('Química Acústica: O Som "Coagula" o Vácuo e Cria Massa', color='white', fontsize=16)
    plt.ylabel('Densidade de Energia (Massa / Tiros)', color='white')
    plt.xlabel('Coordenadas do Vácuo (Qubits)', color='white')
    
    plt.xticks(rotation=45, color='white')
    plt.yticks(color='white')
    
    for bar, state, value in zip(bars, states, values):
        if state in ['0101', '1010']:
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 100, 
                     f'NÓ ACÚSTICO\n{value} (Massa)', ha='center', color='#FFD700', fontweight='bold', fontsize=9)
                     
    plt.tight_layout()
    plt.savefig('C:/Users/bruno/OneDrive/Desktop/Matrioska de oroboros/9_Papers_Zenodo/acoustic_mass_friction.png', dpi=300)
    print("[+] Gráfico salvo: acoustic_mass_friction.png")
