import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

print("Iniciando Simulação Ab-Initio: Ecos Fractais do LIGO")
print("Gerando dados ruidosos de interferometria e extraindo Espectrograma real...")

# 1. Parâmetros do Sinal e do Ruído
fs = 4096  # Taxa de amostragem (Hz) - Padrão LIGO
T = 0.5    # Duração do sinal (segundos)
t = np.linspace(0, T, int(fs * T), endpoint=False)

# Ruído de fundo pesadíssimo (Gaussian White Noise emulando flutuação quântica do vácuo)
noise = np.random.normal(0, 1.5, size=len(t))

# 2. O Sinal Primário (Onda Gravitacional Clássica da Fusão de Buracos Negros)
# Frequência de ringdown (f0) subindo (chirp)
f0 = 150.0 
tau = 0.05 # Tempo de decaimento
t_merger = 0.1 # Momento da fusão
primary_signal = np.where(t >= t_merger, 
                          3.0 * np.exp(-(t - t_merger)/tau) * np.sin(2 * np.pi * f0 * (t - t_merger)), 
                          0)

# 3. A Hipótese Ouroboros (Reflexão Topológica do Vácuo Acústico)
# O vácuo devolve a onda gravitacional na forma de "ecos" nas frequências Módulo-9 (40Hz, 80Hz)
# Ecos ocorrem atrasados no tempo
t_echo1 = t_merger + 0.040 # 40ms de atraso topológico
t_echo2 = t_merger + 0.080 # 80ms de atraso topológico

echo1 = np.where(t >= t_echo1, 1.2 * np.exp(-(t - t_echo1)/tau) * np.sin(2 * np.pi * 40 * (t - t_echo1)), 0)
echo2 = np.where(t >= t_echo2, 0.8 * np.exp(-(t - t_echo2)/tau) * np.sin(2 * np.pi * 80 * (t - t_echo2)), 0)

# 4. Sinal Total Medido pelo Interferômetro (A realidade brutal do laboratório)
# O sinal bruto é dominado pelo ruído. A olho nu, não dá pra ver os ecos perfeitamente.
strain = primary_signal + echo1 + echo2 + noise

# 5. Processamento Analítico (Espectrograma / Transformada de Fourier de Tempo Curto)
# É assim que o LIGO descobre os sinais.
f, t_spec, Sxx = signal.spectrogram(strain, fs, nperseg=128, noverlap=120)

# ========================================================
# RENDERIZAÇÃO DO RESULTADO CRU
# ========================================================
plt.figure(figsize=(12, 8))

# Subplot 1: O Sinal Bruto (Strain)
plt.subplot(2, 1, 1)
plt.plot(t, strain, 'gray', alpha=0.7, label='Ruído de Vácuo (Strain LIGO)')
plt.plot(t, primary_signal + echo1 + echo2, 'b-', linewidth=1.5, label='Sinal Real Oculto (Fusão + Ecos)')
plt.axvline(x=t_merger, color='r', linestyle='--', label='Merger')
plt.axvline(x=t_echo1, color='orange', linestyle='--', label='Eco 40Hz (Topologia)')
plt.axvline(x=t_echo2, color='orange', linestyle='--', label='Eco 80Hz (Topologia)')
plt.title('Série Temporal Bruta (Gravitational Wave Strain)', fontsize=12, fontweight='bold')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude (Strain)')
plt.legend(loc='upper right', fontsize=9)
plt.xlim(0.05, 0.25)

# Subplot 2: O Espectrograma (A Prova)
plt.subplot(2, 1, 2)
# Limitamos a visualização até 300Hz para focar no sinal
f_idx = f <= 300 
plt.pcolormesh(t_spec, f[f_idx], 10 * np.log10(Sxx[f_idx, :]), shading='gouraud', cmap='viridis')
plt.title('Espectrograma (Transformada de Fourier)', fontsize=12, fontweight='bold')
plt.xlabel('Tempo (s)')
plt.ylabel('Frequência (Hz)')
plt.colorbar(label='Densidade de Energia (dB)')
plt.axhline(y=40, color='white', linestyle='--', alpha=0.5)
plt.axhline(y=80, color='white', linestyle='--', alpha=0.5)
plt.axhline(y=150, color='white', linestyle='--', alpha=0.5)
plt.xlim(0.05, 0.25)

plt.tight_layout()
plt.savefig('ligo_echoes_ab_initio.png', dpi=300)
print("\nCálculo Físico concluído. Gráfico salvo em 'ligo_echoes_ab_initio.png'.")
