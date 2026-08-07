import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse as sp
import scipy.sparse.linalg as spla

print("Iniciando Simulação Ab-Initio: Condensado de Bose-Einstein (BEC)")
print("Calculando o Estado Fundamental do Hamiltoniano 2D via Evolução Autovalor (Sparse Matrix)...")

# 1. Configuração da Malha Espacial (Grade 2D)
N = 100 # Resolução da malha
L = 10.0 # Tamanho da caixa
x = np.linspace(-L/2, L/2, N)
y = np.linspace(-L/2, L/2, N)
X, Y = np.meshgrid(x, y)
dx = x[1] - x[0]

# Coordenadas polares para a simetria topológica
R = np.sqrt(X**2 + Y**2)
Theta = np.arctan2(Y, X)

# 2. Construindo o Operador Energia Cinética (Laplaciano 2D usando diferenças finitas)
# Para uma malha NxN, a matriz total tem tamanho (N^2)x(N^2)
print("Construindo a Matriz Cinética...")
diags = np.ones(N)
D1D = sp.spdiags([diags, -2*diags, diags], [-1, 0, 1], N, N) / (dx**2)
I = sp.eye(N)
# Laplaciano 2D é o Produto de Kronecker dos operadores 1D
Laplacian = sp.kron(D1D, I) + sp.kron(I, D1D)
T = -0.5 * Laplacian # Energia Cinética

# 3. Construindo os Potenciais
print("Construindo o Potencial de Armadilha e a Pressão Módulo-9...")
# Potencial Harmônico Padrão (Armadilha Magnética)
V_trap = 0.5 * (X**2 + Y**2)

# Potencial Acústico Ouroboros (Simetria Módulo-9)
# A frequência de 40Hz no espaço 2D cilíndrico impõe uma geometria de 9 polos (360/40 = 9)
acoustic_amplitude = 2.5
V_ouroboros = acoustic_amplitude * np.cos(9 * Theta) * (R > 1.0) # Atua longe do centro

# Potencial Total (Achatar para matriz diagonal 1D)
V_total = (V_trap + V_ouroboros).flatten()
V_matrix = sp.diags(V_total)

# Hamiltoniano Completo
H = T + V_matrix

# 4. Encontrando o Estado Fundamental (O Condensado)
print("Calculando a mecânica quântica orgânica (Menor Autovalor da Matriz 10000x10000)...")
# Usa o algoritmo Lanczos para matrizes esparsas
eigenvalues, eigenvectors = spla.eigsh(H, k=1, which='SA')

ground_state = eigenvectors[:, 0]
probability_density = np.abs(ground_state)**2
probability_density_2D = probability_density.reshape((N, N))

# ========================================================
# RENDERIZAÇÃO DO RESULTADO CRU
# ========================================================
plt.figure(figsize=(12, 6))

# Plot 1: O Potencial Físico Injetado
plt.subplot(1, 2, 1)
plt.contourf(X, Y, V_trap + V_ouroboros, 50, cmap='inferno')
plt.title('Potencial Híbrido Injetado\n(Armadilha + Acústica Módulo-9)')
plt.axis('equal')
plt.axis('off')

# Plot 2: O Condensado Orgânico Emergente (Solução da Equação de Schrödinger)
plt.subplot(1, 2, 2)
plt.contourf(X, Y, probability_density_2D, 100, cmap='viridis')
plt.title('BEC Ab-Initio (Estado Fundamental)\nA Matéria Ocupa a Topologia Módulo-9')
plt.axis('equal')
plt.axis('off')

plt.tight_layout()
plt.savefig('bec_ab_initio.png', dpi=300, bbox_inches='tight')
print("\nCálculo Físico concluído. Gráfico salvo em 'bec_ab_initio.png'.")
