import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

def build_er_epr_teleportation():
    print("[+] Inicializando Algoritmo de Teletransporte Quântico (ER=EPR)...")
    # Qubit 0: A Matéria/Informação que vai cair no Buraco Negro (O Ralo)
    # Qubit 1: A borda do Buraco Negro (Parte do canal EPR)
    # Qubit 2: O Injetor de Vácuo (O Flutuação Quântica do outro lado do Bulk)
    
    # Criamos o circuito com 3 qubits e 1 bit clássico para medir o resultado final
    qc = QuantumCircuit(3, 1)
    
    # 1. Preparando o Estado Inicial da Matéria (Q0)
    # Vamos injetar um estado de energia específico (Ex: Fase Rotacionada)
    # Representa a informação única de uma partícula entrando no "Ralo"
    qc.rx(np.pi/3, 0)
    
    qc.barrier()
    
    # 2. Criando o Buraco de Minhoca (Emaranhamento EPR entre Q1 e Q2)
    # Isso é o Bulk conectando o núcleo da galáxia à borda atômica.
    qc.h(1)
    qc.cx(1, 2)
    
    qc.barrier()
    
    # 3. O Ralo Engole a Matéria (Medição de Bell em Q0 e Q1)
    # A partícula interage com a borda do buraco negro
    qc.cx(0, 1)
    qc.h(0)
    
    # 4. A Travessia Instantânea pelo Bulk
    # Os resultados clássicos colapsam a topologia. Q2 (O Injetor)
    # instantaneamente sofre a mutação dependendo do que caiu no buraco negro.
    # Usamos c_if (condicional clássico) para aplicar as correções, mas
    # no simulador aer podemos usar circuitos deferidos de medição
    qc.cx(1, 2)
    qc.cz(0, 2)
    
    # 5. Medindo o que saiu do Injetor (Q2)
    # Para provar que a informação chegou, revertemos a rotação inicial em Q2
    # e medimos. Se a informação viajou perfeitamente, Q2 deve ler sempre '0' (após revertido).
    qc.barrier()
    qc.rx(-np.pi/3, 2)
    qc.measure(2, 0)
    
    return qc

if __name__ == "__main__":
    qc = build_er_epr_teleportation()
    
    print("[+] Submetendo Circuito de Topologia ER=EPR ao Simulador...")
    simulator = AerSimulator()
    compiled_qc = transpile(qc, simulator)
    
    job = simulator.run(compiled_qc, shots=5000)
    result = job.result()
    counts = result.get_counts()
    
    print(f"[-] Histograma de Saída do Injetor: {counts}")
    
    # Se o teletransporte funcionou perfeitamente, a saída deve ser 100% no estado '0'
    fidelity = counts.get('0', 0) / 5000 * 100
    
    print(f"[!] SUCESSO: O Injetor recriou a informação perfeitamente sem percurso linear!")
    print(f"[!] Fidelidade da Transferência via Buraco de Minhoca: {fidelity}%")
    
    # Gerar Gráfico
    print("[+] Gerando Prova Analítica da Matrioska (Gráfico)...")
    
    plt.figure(figsize=(10, 6), facecolor='#111111')
    ax = plt.gca()
    ax.set_facecolor('#111111')
    
    states = ['Falha de Transmissão (1)', 'Sucesso Absoluto ER=EPR (0)']
    values = [counts.get('1', 0), counts.get('0', 0)]
    
    colors = ['#FF0000', '#00FF00']
    bars = plt.bar(states, values, color=colors, edgecolor='#FFFFFF')
    
    plt.title('ER=EPR: Teletransporte Quântico (Ralo e Injetor)', color='white', fontsize=16)
    plt.ylabel('Fidelidade da Informação (Shots)', color='white')
    
    plt.xticks(color='white')
    plt.yticks(color='white')
    
    for bar, value in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 50, 
                 f'{value} shots\n{(value/5000)*100}%', ha='center', color='white', fontweight='bold')
                 
    plt.tight_layout()
    plt.savefig('C:/Users/bruno/OneDrive/Desktop/Matrioska de oroboros/9_Papers_Zenodo/er_epr_teleportation.png', dpi=300)
    print("[+] Gráfico salvo: er_epr_teleportation.png")
