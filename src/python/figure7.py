"""
Figure 7: Human Hand Grip Capability vs Required Rope Diameters

This script generates a figure showing the relationship between human hand grip
capability and the rope diameters required for moai transport of various sizes.
"""

import matplotlib.pyplot as plt
import numpy as np

# Set publication-quality parameters
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
plt.rcParams['legend.fontsize'] = 9
plt.rcParams['figure.dpi'] = 600

# Create figure
fig, ax = plt.subplots(figsize=(10, 7))

# ============================================================================
# Human Hand Grip Capability Data
# ============================================================================

# Human hand circumference range (mm)
hand_circumference = np.array([180, 190, 200, 210, 220])
hand_labels = ['Small', 'Small-Med', 'Medium', 'Med-Large', 'Large']

# Maximum grippable rope diameter
# Comfortable grip: approximately 35% of hand circumference / π
max_grip_comfortable = hand_circumference * 0.35 / np.pi  # diameter (mm)

# Maximum grip (difficult): approximately 45% of hand circumference / π
max_grip_limit = hand_circumference * 0.45 / np.pi  # diameter (mm)

# ============================================================================
# Plot Grip Capability
# ============================================================================

x_pos = np.arange(len(hand_labels))
width = 0.35

# Plot horizontal bars
bars1 = ax.barh(x_pos - width/2, max_grip_comfortable, width, 
                label='Comfortable grip', color='green', alpha=0.7)
bars2 = ax.barh(x_pos + width/2, max_grip_limit, width, 
                label='Maximum grip (difficult)', color='orange', alpha=0.7)

# ============================================================================
# Add Rope Diameter Requirements for Different Moai Masses
# ============================================================================

# Vertical lines showing required rope diameters
ax.axvline(x=10, color='blue', linestyle='-', linewidth=2, 
           label='10 mm (4 ton moai)')
ax.axvline(x=20, color='purple', linestyle='--', linewidth=2, 
           label='20 mm (10-20 ton moai)')
ax.axvline(x=45, color='red', linestyle='--', linewidth=2, 
           label='45 mm (80 ton moai)')
ax.axvline(x=40, color='darkred', linestyle=':', linewidth=2,
           label='40 mm (Paro, 86 tons)')

# ============================================================================
# Highlight Impractical Zone
# ============================================================================

# Shaded region for rope sizes that cannot be gripped
ax.axvspan(50, 70, alpha=0.15, color='red')
ax.text(60, 4.5, 'Exceeds practical\nhandling limits', ha='center', fontsize=9, 
        bbox=dict(boxstyle='round', facecolor='red', alpha=0.2))

# ============================================================================
# Labels and Formatting
# ============================================================================

ax.set_yticks(x_pos)
ax.set_yticklabels(hand_labels)
ax.set_xlabel('Rope Diameter (mm)')
ax.set_ylabel('Hand Size Category')
ax.set_title('Human Hand Grip Capability vs Required Rope Diameters\nfor Moai Transport')
ax.legend(loc='lower right', fontsize=9)
ax.grid(True, alpha=0.3, axis='x')
ax.set_xlim(0, 70)

# Save figure
plt.tight_layout()
import os
os.makedirs('figures', exist_ok=True)
plt.savefig('figures/figure4_grip_limits.png', dpi=600, bbox_inches='tight')
plt.savefig('figures/figure4_grip_limits.pdf', dpi=600, bbox_inches='tight')
print("Figure 4 saved: figures/figure4_grip_limits.png and .pdf")
plt.show()
