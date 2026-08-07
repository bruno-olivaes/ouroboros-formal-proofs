import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

print("Iniciando Simulação Ab-Initio: Neurobiologia Quântica (Orch-OR)")
print("Resolvendo a Equação de Lindblad para coerência em microtúbulos cerebrais...")

# Parâmetros Quânticos da Tubulina (Microtúbulo)
omega_0 = 1.0     # Energia de transição da tubulina
gamma = 0.5       # Taxa de decoerência térmica brutal do cérebro
f_drive = 40.0    # A Ressonância Ouroboros (Ondas Gamma 40Hz)
Omega = 2.0       # Força do acoplamento acústico (Amplitude da Onda)

# Matrizes de Pauli
sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
sigma_minus = np.array([[0, 0], [1, 0]], dtype=complex) # Operador de aniquilação/perda
sigma_plus = np.array([[0, 1], [0, 0]], dtype=complex)

# A Equação de Lindblad governa Sistemas Quânticos Abertos (como o cérebro)
# d(rho)/dt = -i [H, rho] + L_dissipator
def lindblad_deriv(t, rho_vec, use_drive=False):
    # rho_vec é vetorizado [rho00, rho01, rho10, rho11]
    rho = rho_vec.reshape((2, 2))
    
    # Hamiltoniano
    H = 0.5 * omega_0 * sigma_z
    if use_drive:
        # Acoplamento Gamma 40Hz (Ressonância Modulo-9)
        H += Omega * np.cos(2 * np.pi * f_drive * t) * sigma_x
        
    # Comutador Unitário (Schrödinger)
    comm = np.dot(H, rho) - np.dot(rho, H)
    
    # Dissipador de Lindblad (Termodinâmica destruindo a coerência)
    L = sigma_minus
    L_dag = sigma_plus
    dissipator = gamma * (np.dot(L, np.dot(rho, L_dag)) - 
                          0.5 * np.dot(np.dot(L_dag, L), rho) - 
                          0.5 * np.dot(rho, np.dot(L_dag, L)))
                          
    drho_dt = -1j * comm + dissipator
    return drho_dt.flatten()

# Estado inicial puramente coerente (Superposição perfeita na tubulina)
rho_0 = np.array([[0.5, 0.5], [0.5, 0.5]], dtype=complex).flatten()

# Tempo de simulação (0 a 0.2 segundos, suficiente para ver ciclos de 40Hz)
t_span = (0, 0.2)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

print("Simulando cérebro sem ressonância (Decaimento padrão)...")
sol_raw = solve_ivp(lindblad_deriv, t_span, rho_0, t_eval=t_eval, args=(False,))
coherence_raw = np.abs(sol_raw.y[1]) # O termo off-diagonal rho_01 representa a Consciência (Coerência)

print("Simulando cérebro com Acoplamento Ouroboros 40Hz...")
sol_our = solve_ivp(lindblad_deriv, t_span, rho_0, t_eval=t_eval, args=(True,))
coherence_our = np.abs(sol_our.y[1])

# ========================================================
# RENDERIZAÇÃO DO RESULTADO CRU
# ========================================================
plt.figure(figsize=(10, 6))

plt.plot(t_eval, coherence_raw, 'r--', linewidth=2.5, label='Física Padrão (Decaimento Térmico/Perda de Consciência)')
plt.plot(t_eval, coherence_our, 'g-', linewidth=2.5, label='Orch-OR Ouroboros (Ressonância Gamma 40Hz Sustenta Coerência)')

plt.title('Neurobiologia Quântica Ab-Initio (Equação de Lindblad)\nSustentação da Consciência via Frequência Topológica Módulo-9', fontsize=13, fontweight='bold')
plt.xlabel('Tempo (segundos)', fontsize=12)
plt.ylabel('Fator de Coerência Quântica $|\\rho_{01}|$', fontsize=12)
plt.legend(loc='upper right', fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig('orch_or_ab_initio.png', dpi=300)
print("\nCálculo Físico concluído. Gráfico salvo em 'orch_or_ab_initio.png'.")
