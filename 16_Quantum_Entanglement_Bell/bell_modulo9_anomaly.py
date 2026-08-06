import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
import os

print("Iniciando Simulador do Ponto Cego de Bell (Módulo-9)...")

def standard_bell_correlation(theta):
    """
    Standard Quantum Mechanics prediction for Bell/CHSH correlation.
    E(theta) = -cos(theta)
    """
    return -np.cos(theta)

def modulo9_bell_correlation(theta):
    """
    Ouroboros Modulo-9 topological correlation.
    The entanglement channel is mediated by the acoustic vacuum.
    At exact Modulo-9 harmonic angles (multiples of 40 degrees = 2pi/9 rad),
    the vacuum acoustic standing wave causes destructive interference,
    creating a sharp 'blind spot' (drop in correlation) before recovering.
    """
    base_corr = standard_bell_correlation(theta)
    
    # Modulo-9 harmonic angles (in radians): 40, 80, 120, 160, 200, 240, 280, 320, 360
    harmonic_spacing = 2 * np.pi / 9.0
    
    # Calculate distance to the nearest harmonic
    dist_to_harmonic = np.abs(np.remainder(theta + harmonic_spacing/2, harmonic_spacing) - harmonic_spacing/2)
    
    # Create the "Blind Spot" (Anomaly)
    # When extremely close to a harmonic, the correlation drops sharply
    anomaly_width = 0.08  # Radians
    anomaly_depth = 0.8   # 80% loss of correlation at the exact harmonic
    
    # Gaussian blind spot at the harmonics
    blind_spot = anomaly_depth * np.exp(-(dist_to_harmonic**2) / (anomaly_width**2))
    
    # The correlation is pulled towards 0 (loss of entanglement) at the blind spots
    # If base_corr is negative, it goes up towards 0. If positive, it goes down.
    ouroboros_corr = base_corr * (1.0 - blind_spot)
    
    return ouroboros_corr

# Generate angles from 0 to 360 degrees (0 to 2pi radians)
angles = np.linspace(0, 2 * np.pi, 1000)
degrees = np.degrees(angles)

# Calculate correlations
corr_standard = standard_bell_correlation(angles)
corr_ouroboros = modulo9_bell_correlation(angles)

# Add simulated experimental noise
np.random.seed(42)
experimental_noise = np.random.normal(0, 0.02, size=len(angles))
measured_corr = corr_ouroboros + experimental_noise

# ---------------------------------------------------------
# Plotting
# ---------------------------------------------------------
plt.figure(figsize=(14, 8))
plt.style.use('dark_background')

# Plot Standard Quantum Mechanics
plt.plot(degrees, corr_standard, 'r--', alpha=0.6, linewidth=2, label='Standard QM ($E(\\theta) = -\\cos(\\theta)$)')

# Plot Ouroboros Modulo-9
plt.plot(degrees, corr_ouroboros, 'cyan', linewidth=3, label='Ouroboros Topology (Modulo-9 Acoustic Vacuum)')

# Scatter simulated lab data
plt.scatter(degrees[::4], measured_corr[::4], color='yellow', s=10, alpha=0.7, label='Simulated Unfiltered Lab Data')

# Highlight the Modulo-9 harmonics (multiples of 40 deg)
for i in range(1, 9):
    harmonic_deg = i * 40
    plt.axvline(x=harmonic_deg, color='magenta', linestyle=':', alpha=0.5)
    
    # Add text to the first few to explain
    if i == 1:
        plt.annotate('Modulo-9\nBlind Spot\n(40°)', xy=(harmonic_deg, corr_ouroboros[np.argmin(np.abs(degrees - harmonic_deg))]), 
                     xytext=(harmonic_deg + 10, 0),
                     arrowprops=dict(facecolor='magenta', shrink=0.05, width=1),
                     fontsize=10, color='magenta')

plt.title('Quantum Entanglement: The Modulo-9 Topological Blind Spots\nBell Test Anomaly in Acoustic Vacuum', fontsize=16, color='cyan', pad=20)
plt.xlabel('Polarizer Angle Difference $\\theta$ (Degrees)', fontsize=12)
plt.ylabel('Entanglement Correlation $E(\\theta)$', fontsize=12)
plt.xlim(0, 360)
plt.ylim(-1.2, 1.2)
plt.xticks(np.arange(0, 361, 40))
plt.grid(True, alpha=0.15)
plt.legend(fontsize=11, loc='upper right')
plt.tight_layout()

# Save the plot
output_dir = r"C:\Users\bruno\OneDrive\Desktop\Ouroboros-Quantum-Framework\16_Quantum_Entanglement_Bell"
plot_path = os.path.join(output_dir, 'bell_modulo9_blindspot.png')
plt.savefig(plot_path, dpi=300)
print(f"Predição da Anomalia de Bell gerada! Salvo em: {plot_path}")
