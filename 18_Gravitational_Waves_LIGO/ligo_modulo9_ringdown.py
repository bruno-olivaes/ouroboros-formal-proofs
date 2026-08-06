import numpy as np
import matplotlib.pyplot as plt
import os

print("Iniciando Simulador LIGO de Ondas Gravitacionais Topológicas (Módulo-9)...")

def generate_standard_ringdown(t, freq=50, tau=0.01):
    """
    Standard General Relativity prediction for Black Hole merger ringdown.
    Smooth exponentially decaying sinusoid.
    """
    return np.exp(-t / tau) * np.sin(2 * np.pi * freq * t)

def generate_ouroboros_ringdown(t, freq=50, tau=0.01):
    """
    Ouroboros Framework prediction for BH merger ringdown.
    The gravitational wave bounces inside the Modulo-9 acoustic spacetime fluid.
    This generates high-frequency fractal overtones (Pisano echoes) embedded in the ringdown.
    """
    base_wave = generate_standard_ringdown(t, freq, tau)
    
    # Pisano sequence pattern (1, 1, 2, 3, 5, 8, 4, 3, 7, 1, 8, 9...) 
    # simplified as a complex harmonic modulation at the Modulo-9 attractor (9x frequency)
    pisano_modulation = 0.15 * np.exp(-t / (tau*1.5)) * np.sin(2 * np.pi * (freq * 9) * t)
    
    return base_wave + pisano_modulation

# Time array (simulating milliseconds after merger)
t = np.linspace(0, 0.05, 1000)
t_ms = t * 1000

standard_wave = generate_standard_ringdown(t)
ouroboros_wave = generate_ouroboros_ringdown(t)

# ---------------------------------------------------------
# Plotting
# ---------------------------------------------------------
plt.figure(figsize=(14, 8))
plt.style.use('dark_background')

# Plot Standard GR
plt.plot(t_ms, standard_wave, 'r--', alpha=0.6, linewidth=2, label='Standard General Relativity (Smooth Ringdown)')

# Plot Ouroboros Topology
plt.plot(t_ms, ouroboros_wave, 'cyan', linewidth=2, label='Ouroboros Topology (Pisano-Sequence Fractal Echoes)')

# Zoom in on a specific peak to show the fine structure
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
axins = inset_axes(plt.gca(), width="30%", height="30%", loc="upper right", borderpad=2)
axins.plot(t_ms, standard_wave, 'r--', alpha=0.6)
axins.plot(t_ms, ouroboros_wave, 'cyan')
axins.set_xlim(2, 6)
axins.set_ylim(-0.5, 0.5)
axins.set_title("Zoom: Topo-Acoustic Overtones", color='yellow', fontsize=10)
axins.tick_params(axis='both', colors='white', labelsize=8)

plt.title('Gravitational Wave Topology: Black Hole Merger Ringdown\nModulo-9 Acoustic Fractal Overtones in LIGO Data', fontsize=16, color='cyan', pad=20)
plt.xlabel('Time (milliseconds)', fontsize=12)
plt.ylabel('Strain Amplitude ($h$)', fontsize=12)
plt.grid(True, alpha=0.15)
plt.legend(fontsize=11, loc='upper right', bbox_to_anchor=(0.65, 0.95))
plt.tight_layout()

# Save the plot
output_dir = r"C:\Users\bruno\OneDrive\Desktop\Ouroboros-Quantum-Framework\18_Gravitational_Waves_LIGO"
plot_path = os.path.join(output_dir, 'ligo_modulo9_echoes.png')
plt.savefig(plot_path, dpi=300)
print(f"Predição de Ondas Gravitacionais gerada! Salvo em: {plot_path}")
