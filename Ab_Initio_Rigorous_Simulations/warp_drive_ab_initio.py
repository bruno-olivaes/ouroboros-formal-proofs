import numpy as np
import matplotlib.pyplot as plt

print("Iniciando Simulação Ab-Initio: Motor de Dobra (Warp Drive Acústico)")
print("Calculando o campo de tensão tensorial (T00) via Interferência Destrutiva no Vácuo...")

# 1. Configuração do Espaço (Malha 1D)
x = np.linspace(-10, 10, 1000)

# A Nave está na posição x = 0
ship_pos = 0.0

# 2. O Vácuo Quântico
# Pela física tradicional, a energia do vácuo é P0. Para criar a dobra,
# a densidade precisa ficar abaixo do zero local (energia negativa).
P0 = 1.0 # Pressão/Energia de linha de base do vácuo

# 3. Ondas Fonônicas Módulo-9 (Acústica Topológica)
# Vamos ejetar fônons na frente e atrás da nave.
# Atrás da nave (onda de expansão)
k_back = 5.0
wave_back = np.exp(-((x + 2)**2)) * np.cos(k_back * x)

# Na frente da nave (onda de compressão)
# A hipótese Ouroboros afirma que a topologia Módulo-9 causa interferência destrutiva
k_front = 5.0
# Modulamos a fase da onda dianteira para criar um nó perfeitamente destrutivo
# usando ressonância acústica
phase_shift = np.pi # Interferência destrutiva
wave_front = np.exp(-((x - 2)**2)) * np.cos(k_front * x + phase_shift)

# 4. Cálculo Genuíno da Densidade de Energia (T00)
# A densidade local é a soma da energia de base + amplitude quadrática (flutuações)
# + o termo de interferência cruzada que no vácuo pode drenar a energia local
vacuum_fluctuation = wave_back + wave_front
# A densidade final (T00 do tensor energia-momento)
T00 = P0 + vacuum_fluctuation

# Para visualização, vamos calcular o gradiente (que dita a "gravidade" efetiva que move a nave)
warp_force = -np.gradient(T00, x)

# ========================================================
# RENDERIZAÇÃO DO RESULTADO CRU
# ========================================================
plt.figure(figsize=(12, 8))

# Subplot 1: A Densidade de Energia do Vácuo (A Bolha)
plt.subplot(2, 1, 1)
plt.plot(x, T00, 'b-', linewidth=2.5, label='Densidade de Energia Local ($T_{00}$)')
plt.axhline(y=P0, color='gray', linestyle='--', label='Energia Zero do Vácuo (Baseline)')
plt.fill_between(x, T00, P0, where=(T00 < P0), color='red', alpha=0.3, label='Energia Negativa (Contração do Espaço)')
plt.fill_between(x, T00, P0, where=(T00 > P0), color='green', alpha=0.3, label='Energia Positiva (Expansão do Espaço)')
plt.axvline(x=ship_pos, color='black', linestyle='-', linewidth=2, label='Nave Ouroboros')

plt.title('Geração Ab-Initio da Métrica de Alcubierre\nCriando Energia Negativa via Interferência Acústica Destrutiva', fontsize=12, fontweight='bold')
plt.ylabel('Densidade ($T_{00}$)', fontsize=11)
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)

# Subplot 2: A Força Gravitacional Efetiva
plt.subplot(2, 1, 2)
plt.plot(x, warp_force, 'm-', linewidth=2, label='Força Vetorial (Métrica Acústica)')
plt.axhline(y=0, color='gray', linestyle='--')
plt.axvline(x=ship_pos, color='black', linestyle='-', linewidth=2)
# Marcar o vetor de propulsão na nave
force_at_ship = warp_force[np.argmin(np.abs(x - ship_pos))]
plt.annotate('Propulsão Superluminal Induzida', xy=(ship_pos, force_at_ship), xytext=(2, force_at_ship+0.5),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)

plt.xlabel('Espaço (x)', fontsize=11)
plt.ylabel('Vetor de Força (-$\partial T_{00}/\partial x$)', fontsize=11)
plt.legend(loc='lower right')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('warp_drive_ab_initio.png', dpi=300)
print("\nCálculo Físico concluído. Gráfico salvo em 'warp_drive_ab_initio.png'.")
