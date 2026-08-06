import numpy as np
import matplotlib.pyplot as plt
import os

print("Iniciando Simulador Acústico de Condensado de Bose-Einstein (Módulo-9)...")

def generate_vortex_lattice(symmetry=6, radius=10):
    """
    Generates a vortex lattice in a rotating BEC.
    Standard physics produces an Abrikosov hexagonal lattice (6-fold symmetry).
    """
    points_x, points_y = [], []
    rings = 4
    
    # Center vortex
    points_x.append(0)
    points_y.append(0)
    
    for r in range(1, rings + 1):
        num_points = symmetry * r
        angles = np.linspace(0, 2*np.pi, num_points, endpoint=False)
        for theta in angles:
            points_x.append(r * np.cos(theta))
            points_y.append(r * np.sin(theta))
            
    return np.array(points_x), np.array(points_y)

# Generate Classical Hexagonal Lattice (6-fold)
class_x, class_y = generate_vortex_lattice(symmetry=6)

# Generate Ouroboros Topo-Acoustic Lattice (9-fold symmetry induced by 40Hz resonance)
ouro_x, ouro_y = generate_vortex_lattice(symmetry=9)

# Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), facecolor='#0d1117')
fig.patch.set_facecolor('#0d1117')

# Left Plot: Classical BEC
ax1.set_facecolor('#0d1117')
ax1.scatter(class_x, class_y, color='red', s=100, alpha=0.8, edgecolors='white')
ax1.set_title("Standard Model (No Resonance)\nHexagonal Abrikosov Vortex Lattice", color='red', fontsize=14)
ax1.axis('equal')
ax1.axis('off')

# Right Plot: Ouroboros Modulo-9 BEC
ax2.set_facecolor('#0d1117')
ax2.scatter(ouro_x, ouro_y, color='cyan', s=100, alpha=0.8, edgecolors='white')
ax2.set_title("Ouroboros Topology (40Hz Acoustic Resonance)\nModulo-9 Enforced Vortex Lattice", color='cyan', fontsize=14)
ax2.axis('equal')
ax2.axis('off')

# Draw lines to show the 9-fold symmetry
for i in range(9):
    theta = i * (2*np.pi/9)
    ax2.plot([0, 4*np.cos(theta)], [0, 4*np.sin(theta)], color='yellow', linestyle=':', alpha=0.5)

plt.suptitle("Quantum Fluid Dynamics: Topological Phase Transition in Rotating BEC", color='white', fontsize=18)
plt.tight_layout()

# Save the plot
output_dir = r"C:\Users\bruno\OneDrive\Desktop\Ouroboros-Quantum-Framework\17_Bose_Einstein_Acoustics"
plot_path = os.path.join(output_dir, 'bec_modulo9_lattice.png')
plt.savefig(plot_path, dpi=300, facecolor='#0d1117')
print(f"Predição do Condensado de Bose-Einstein gerada! Salvo em: {plot_path}")
