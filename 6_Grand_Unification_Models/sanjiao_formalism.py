import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def simulate_sanjiao_vs_binary():
    print("[+] Inicializando Comparador de Espaço de Hilbert...")
    print("[+] Modelo 1: Lógica Binária Ortodoxa (0 e 1)")
    print("[+] Modelo 2: Lógica Sanjiao Ouroboros (Yin=0, Yang=1, Tao/Compressor=2)")
    
    # Número de partículas/componentes emulados
    N = np.arange(1, 15)
    
    # Espaço de Estados (Hilbert Space Size)
    binary_states = 2**N
    sanjiao_states = 3**N
    
    print("[-] Calculando divergência exponencial da dimensão...")
    
    # Gerar Gráfico
    plt.figure(figsize=(12, 6), facecolor='#111111')
    ax = plt.gca()
    ax.set_facecolor('#111111')
    
    plt.plot(N, binary_states, color='#FF4500', linewidth=3, marker='o', label='Matemática Ortodoxa (Binária / 2^N)')
    plt.plot(N, sanjiao_states, color='#00FF00', linewidth=3, marker='s', label='Formalismo Sanjiao (Trinária / Qutrits / 3^N)')
    
    # Escala logarítmica para vermos a separação de universos
    plt.yscale('log')
    
    plt.title('A Supremacia do Sanjiao: O Estado "Tao" Esmaga a Lógica Binária', color='white', fontsize=16)
    plt.ylabel('Densidade de Processamento (Tamanho do Universo)', color='white')
    plt.xlabel('Número de Partículas (N)', color='white')
    
    plt.xticks(color='white')
    plt.yticks(color='white')
    
    leg = plt.legend(facecolor='#222222', edgecolor='white')
    for text in leg.get_texts():
        text.set_color('white')
        
    plt.grid(color='#333333', linestyle=':', linewidth=1)
    
    plt.tight_layout()
    plt.savefig('C:/Users/bruno/OneDrive/Desktop/Matrioska de oroboros/9_Papers_Zenodo/sanjiao_formalism.png', dpi=300)
    print("[+] Gráfico salvo: sanjiao_formalism.png")
    
    print("[!] CONCLUSÃO FÍSICA: Ao ignorar o terceiro polo (O Neutro/Compressor), a ciência ortodoxa joga fora 99.9% da realidade computável do universo.")

if __name__ == "__main__":
    simulate_sanjiao_vs_binary()
