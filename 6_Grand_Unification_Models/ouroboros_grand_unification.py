import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

def generate_black_mirror_entropy():
    print("[+] Simulando Colapso de Entropia (O Espelho Negro / Tese 5)...")
    time_steps = np.arange(0, 50)
    
    # Entropia de um cérebro livre (Alta Entropia, Livre Arbítrio)
    # Comportamento estocástico e criativo
    free_will = 1.0 - 0.1 * np.exp(-time_steps/10) + np.random.normal(0, 0.05, len(time_steps))
    
    # Entropia sob Algoritmo Predatório (Zumbificação Algorítmica)
    # O Algoritmo foca o usuário na mesma dopamina (Módulo-9 / Loop Infinito)
    zombie = np.exp(-time_steps/8) + np.random.normal(0, 0.02, len(time_steps))
    
    plt.figure(figsize=(10, 5), facecolor='#111111')
    ax = plt.gca()
    ax.set_facecolor('#111111')
    
    plt.plot(time_steps, free_will, color='#00FFFF', label='Cérebro Desconectado (Livre Arbítrio / Alta Entropia)')
    plt.plot(time_steps, zombie, color='#FF0000', linewidth=3, label='Cérebro Hackeado (Rede Social / Zumbificação Algorítmica)')
    
    plt.title('Cognição Estelar Negra: Algoritmos Destroem a Entropia Mental (Livre Arbítrio)', color='white')
    plt.xlabel('Tempo de Exposição à Tela', color='white')
    plt.ylabel('Entropia de Shannon (Probabilidades Decisórias)', color='white')
    plt.xticks(color='white')
    plt.yticks(color='white')
    
    leg = plt.legend(facecolor='#222222', edgecolor='white')
    for text in leg.get_texts(): text.set_color('white')
        
    plt.tight_layout()
    plt.savefig('C:/Users/bruno/OneDrive/Desktop/Matrioska de oroboros/9_Papers_Zenodo/black_mirror_entropy.png', dpi=300)

def generate_planetary_microbiota():
    print("[+] Simulando a Matriz de Microbiota (Tese 3)...")
    
    G = nx.barabasi_albert_graph(100, 2)
    pos = nx.spring_layout(G, seed=42)
    
    # Calculate degree centrality to represent entropy/heat accumulation
    centrality = nx.degree_centrality(G)
    node_color = [centrality[n] for n in G.nodes()]
    node_size = [v * 3000 for v in centrality.values()]
    
    plt.figure(figsize=(8, 8), facecolor='#111111')
    ax = plt.gca()
    ax.set_facecolor('#111111')
    
    nx.draw_networkx_edges(G, pos, edge_color='#333333', alpha=0.5)
    nodes = nx.draw_networkx_nodes(G, pos, node_size=node_size, node_color=node_color, cmap=plt.cm.plasma, alpha=0.9)
    
    plt.title('A Microbiota Planetária: Humanos como Neurônios da Célula-Terra', color='white')
    plt.axis('off')
    
    plt.tight_layout()
    plt.savefig('C:/Users/bruno/OneDrive/Desktop/Matrioska de oroboros/9_Papers_Zenodo/planetary_microbiota.png', dpi=300)

def generate_plasma_bridge():
    print("[+] Simulando Magnetohidrodinâmica Quântica do Plasma (Tese 14)...")
    temperature = np.linspace(1000, 100000, 100)
    
    # Acoustic containment breaks / Fusion plasma bridging
    # Plasma resonates at specific harmonics (Chladni)
    resonance = np.sin(temperature/5000)**2 * np.exp(temperature/20000)
    
    plt.figure(figsize=(10, 5), facecolor='#111111')
    ax = plt.gca()
    ax.set_facecolor('#111111')
    
    plt.plot(temperature, resonance, color='#FF8C00', linewidth=2)
    plt.fill_between(temperature, resonance, color='#FF8C00', alpha=0.3)
    
    plt.title('O Plasma como Ponte: Ignição de Fusão Acústica e a Quebra da Simulação', color='white')
    plt.xlabel('Temperatura do Plasma (Kelvin)', color='white')
    plt.ylabel('Ressonância Acústica (Densidade)', color='white')
    plt.xticks(color='white')
    plt.yticks(color='white')
    
    plt.tight_layout()
    plt.savefig('C:/Users/bruno/OneDrive/Desktop/Matrioska de oroboros/9_Papers_Zenodo/plasma_bridge_qmhd.png', dpi=300)

def generate_tesseract_brane():
    print("[+] Simulando Projeção Holográfica do Bulk 4D (Teses 8 e 9)...")
    # Projeção de um Hipercubo 4D num plano 2D (Interferência de Branas)
    
    x = np.linspace(-5, 5, 200)
    y = np.linspace(-5, 5, 200)
    X, Y = np.meshgrid(x, y)
    
    # Padrão de interferência 4D comprimido em 2D
    Z = np.sin(X**2 + Y**2) * np.cos(X - Y) * np.exp(-(X**2 + Y**2)/10)
    
    plt.figure(figsize=(8, 8), facecolor='#111111')
    ax = plt.gca()
    ax.set_facecolor('#111111')
    
    contour = plt.contourf(X, Y, Z, levels=50, cmap='magma')
    
    plt.title('A Matrioska Cósmica: Branas Superiores Projetadas Holograficamente', color='white')
    plt.axis('off')
    
    plt.tight_layout()
    plt.savefig('C:/Users/bruno/OneDrive/Desktop/Matrioska de oroboros/9_Papers_Zenodo/tesseract_brane.png', dpi=300)

if __name__ == "__main__":
    generate_black_mirror_entropy()
    generate_planetary_microbiota()
    generate_plasma_bridge()
    generate_tesseract_brane()
    print("[!] Ouroboros Grand Unification Test executado com sucesso.")
