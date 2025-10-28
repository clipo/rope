"""
Figure 10: Human Hand Grip Capability vs Required Rope Diameters

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

# Calculate required rope diameters using paper specifications
tensile_strength = 916  # MPa
packing_efficiency = 0.65  # 65% fiber packing efficiency
construction_efficiency = 0.75  # 75% construction efficiency
safety_factor = 10

def calc_rope_diameter(mass_tons):
    """Calculate required rope diameter for given moai mass"""
    working_load = mass_tons * 1.0  # kN
    required_breaking_load = working_load * safety_factor
    diameter = 2 * np.sqrt(required_breaking_load * 1000 /
                           (tensile_strength * packing_efficiency * construction_efficiency * np.pi))
    return diameter

# Calculate diameters for different moai sizes
d_4ton = calc_rope_diameter(4)
d_15ton = calc_rope_diameter(15)
d_80ton = calc_rope_diameter(80)
d_86ton = calc_rope_diameter(86)

# Vertical lines showing required rope diameters
ax.axvline(x=d_4ton, color='blue', linestyle='-', linewidth=2,
           label=f'{d_4ton:.0f} mm (4 ton moai)')
ax.axvline(x=d_15ton, color='purple', linestyle='--', linewidth=2,
           label=f'{d_15ton:.0f} mm (15 ton moai)')
ax.axvline(x=d_80ton, color='red', linestyle='--', linewidth=2,
           label=f'{d_80ton:.0f} mm (80 ton moai)')
ax.axvline(x=d_86ton, color='darkred', linestyle=':', linewidth=2,
           label=f'{d_86ton:.0f} mm (Paro, 86 tons)')

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
plt.savefig('figures/figure10_grip_limits.png', dpi=600, bbox_inches='tight')
plt.savefig('figures/figure10_grip_limits.pdf', dpi=600, bbox_inches='tight')
print("Figure 10 saved: figures/figure10_grip_limits.png and .pdf")
plt.show()
