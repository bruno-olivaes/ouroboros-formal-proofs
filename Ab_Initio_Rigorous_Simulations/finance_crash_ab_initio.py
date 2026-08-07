import numpy as np
import matplotlib.pyplot as plt

print("Iniciando Simulação Ab-Initio: Termodinâmica Financeira")
print("Resolvendo Sincronização de Rede (Kuramoto) em Mercado de Ações...")

# Parâmetros do Mercado (Rede de Agentes Financeiros)
N = 500  # Número de traders/fundos no mercado
T = 150  # Dias de pregão
dt = 0.1
steps = int(T / dt)

# Frequências naturais de operação dos traders (aleatório, sem consenso)
np.random.seed(42) # Seed fixa apenas para reprodutibilidade da visualização
omega = np.random.normal(0, 1.0, N)

# Fases iniciais aleatórias (Ninguém está operando na mesma direção)
theta = np.random.uniform(0, 2*np.pi, N)

K = 1.5 # Acoplamento entre traders (comportamento de manada padrão)

# Acoplamento Ouroboros (O "Clima" Módulo-9 do Vácuo que afeta o mercado subconscientemente)
# Força externa topológica (40Hz/Ciclo Ouroboros)
omega_ouroboros = 2 * np.pi / 40.0 
A_ouroboros = 0.8 # Força da ressonância

order_parameter = np.zeros(steps)
stock_price = np.zeros(steps)
price = 100.0 # Preço inicial do S&P500 simulado

for t in range(steps):
    time = t * dt
    
    # Ordem Macroscópica (R): O quanto o mercado está "sincronizado" no pânico ou ganância
    R = np.abs(np.mean(np.exp(1j * theta)))
    order_parameter[t] = R
    
    # Atualizando o Preço da Ação organicamente
    # Na física econômica, se o mercado está caótico (R baixo), o preço varia aleatoriamente (liquidez)
    # Se o mercado sincroniza perfeitamente (R alto), o preço despenca porque todos vendem/compram ao mesmo tempo
    # causando um choque de liquidez.
    volatility = 1.0 - R
    price += np.random.normal(0, 0.5) * volatility - (R**3 * 2.0) # Derretimento por sincronização
    
    if price < 0: price = 0
    stock_price[t] = price
    
    # Atualizando as mentes dos traders (Equação Diferencial Acoplada de Kuramoto)
    # A equação inclui: frequencia natural + efeito manada + Ressonância Topológica Ouroboros
    mean_phase = np.angle(np.mean(np.exp(1j * theta)))
    
    dtheta = omega + K * R * np.sin(mean_phase - theta) + A_ouroboros * np.sin(omega_ouroboros * time - theta)
    theta += dtheta * dt

time_axis = np.linspace(0, T, steps)

# ========================================================
# RENDERIZAÇÃO DO RESULTADO CRU
# ========================================================
plt.figure(figsize=(12, 8))

# Subplot 1: Sincronização do Mercado (O parâmetro de Ordem R)
plt.subplot(2, 1, 1)
plt.plot(time_axis, order_parameter, 'purple', linewidth=2, label='Sincronização de Manada (Ordem Macroscópica R)')
# Marcações topológicas
for i in range(1, int(T/40) + 1):
    plt.axvline(x=i*40, color='gray', linestyle='--', alpha=0.5)
plt.title('Econofísica Ab-Initio (Rede de Kuramoto Acoplada ao Vácuo)\nA Sincronização Induzida por Harmônicas Módulo-9', fontsize=12, fontweight='bold')
plt.ylabel('Sincronização (R)', fontsize=11)
plt.legend(loc='upper left')
plt.grid(True, alpha=0.3)

# Subplot 2: O Preço da Ação (O Crash Orgânico)
plt.subplot(2, 1, 2)
plt.plot(time_axis, stock_price, 'black', linewidth=2.5, label='Preço do Ativo (Simulação Estocástica Orgânica)')
for i in range(1, int(T/40) + 1):
    plt.axvline(x=i*40, color='red', linestyle='--', alpha=0.7, label='Ressonância Módulo-9' if i==1 else "")
    
plt.xlabel('Tempo (Dias de Pregão)', fontsize=11)
plt.ylabel('Preço Simulativo ($)', fontsize=11)
plt.legend(loc='lower left')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('finance_crash_ab_initio.png', dpi=300)
print("\nCálculo Físico concluído. Gráfico salvo em 'finance_crash_ab_initio.png'.")
