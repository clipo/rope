"""
Figure 9: Tensile Strength Scaling and Required Rope Diameters for Moai Transport

This script generates a two-panel figure showing:
- Left: Breaking load vs rope diameter
- Right: Required rope diameter vs moai mass
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

# Create figure with two subplots
fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(12, 5))

# ============================================================================
# LEFT PANEL: Breaking Load vs Diameter
# ============================================================================

# Parameters
diameters = np.linspace(5, 60, 100)  # mm
tensile_strength = 916  # MPa for T. cordifolia
packing_efficiency = 0.65  # fiber packing efficiency (65%)
construction_efficiency = 0.75  # rope construction efficiency (75%)

# Calculate cross-sectional area
area = np.pi * (diameters/2)**2  # mm^2
effective_area = area * packing_efficiency  # account for fiber packing

# Calculate breaking load
# Breaking Load (N) = Tensile Strength (MPa) × Effective Area (mm²) × Construction Efficiency
breaking_load = tensile_strength * effective_area * construction_efficiency / 1000  # Convert to kN

# Plot main curve
ax_left.plot(diameters, breaking_load, 'b-', linewidth=2, 
             label='T. cordifolia (916 MPa)')
ax_left.fill_between(diameters, 0, breaking_load, alpha=0.2, color='blue')

# Add reference lines for moai requirements
ax_left.axhline(y=4, color='green', linestyle='--', linewidth=1.5, 
                label='4 ton moai requirement (~4 kN)')
ax_left.axhline(y=80, color='orange', linestyle='--', linewidth=1.5, 
                label='80 ton moai requirement (~80 kN)')

# Add safety factor line
safety_factor_8 = breaking_load / 8
ax_left.plot(diameters, safety_factor_8, 'r--', linewidth=1, alpha=0.5, 
             label='Breaking load / 8 (safety margin)')

# Mark specific points
diameter_10mm = 10
idx_10 = np.argmin(np.abs(diameters - diameter_10mm))
ax_left.plot(diameter_10mm, breaking_load[idx_10], 'ro', markersize=8)
ax_left.text(diameter_10mm, breaking_load[idx_10] + 20, f'10 mm\n{breaking_load[idx_10]:.0f} kN',
             ha='center', fontsize=8)

diameter_45mm = 45
idx_45 = np.argmin(np.abs(diameters - diameter_45mm))
ax_left.plot(diameter_45mm, breaking_load[idx_45], 'ro', markersize=8)
ax_left.text(diameter_45mm, breaking_load[idx_45] + 40, f'45 mm\n{breaking_load[idx_45]:.0f} kN',
             ha='center', fontsize=8)

# Labels and formatting
ax_left.set_xlabel('Rope Diameter (mm)')
ax_left.set_ylabel('Breaking Load (kN)')
ax_left.set_title('Rope Breaking Load vs Diameter\n(Triumfetta cordifolia, 65% packing, 75% construction efficiency)')
ax_left.grid(True, alpha=0.3)
ax_left.legend(loc='upper left', fontsize=8)
ax_left.set_xlim(5, 60)
ax_left.set_ylim(0, 1200)

# ============================================================================
# RIGHT PANEL: Required Rope Diameter vs Moai Mass
# ============================================================================

# Moai masses to analyze
moai_masses = np.array([4, 10, 20, 40, 60, 80, 86])  # tons

# Assume working load = 1 kN per ton (simplified estimate)
force_per_rope = moai_masses * 1000  # N

# Safety factor
safety_factor = 10

# Required breaking load
required_breaking_load = force_per_rope * safety_factor / 1000  # kN

# Calculate required diameter from breaking load
# Rearranging: Breaking Load = Tensile Strength × π × (d/2)² × Packing Efficiency × Construction Efficiency
# d = 2 × sqrt(Breaking Load / (Tensile Strength × π × Packing Efficiency × Construction Efficiency))
required_diameter = 2 * np.sqrt(required_breaking_load * 1000 /
                                (tensile_strength * packing_efficiency * construction_efficiency * np.pi))

# Plot required diameter vs mass
ax_right.plot(moai_masses, required_diameter, 'b-o', linewidth=2, markersize=6)

# Add handling limit lines
ax_right.axhline(y=50, color='r', linestyle='--', linewidth=2, 
                 label='Practical handling limit (~50 mm)')
ax_right.fill_between(moai_masses, 50, 70, alpha=0.2, color='red', 
                       label='Difficult to handle')

# Mark Paro
paro_mass = 86
paro_idx = np.argmin(np.abs(moai_masses - paro_mass))
ax_right.plot(paro_mass, required_diameter[paro_idx], 'r*', markersize=15)
ax_right.text(paro_mass, required_diameter[paro_idx] + 3, f'Paro\n(86 tons, {required_diameter[paro_idx]:.0f} mm)',
              ha='center', fontsize=9, weight='bold')

# Labels and formatting
ax_right.set_xlabel('Moai Mass (tons)')
ax_right.set_ylabel('Required Rope Diameter (mm)')
ax_right.set_title('Required Rope Diameter for Moai Transport\n(Safety factor = 10)')
ax_right.grid(True, alpha=0.3)
ax_right.legend(loc='upper left')
ax_right.set_xlim(0, 90)
ax_right.set_ylim(0, 70)

# Save figure
plt.tight_layout()
import os
os.makedirs('figures', exist_ok=True)
plt.savefig('figures/figure9_tensile_strength_scaling.png', dpi=600, bbox_inches='tight')
plt.savefig('figures/figure9_tensile_strength_scaling.pdf', dpi=600, bbox_inches='tight')
print("Figure 9 saved: figures/figure9_tensile_strength_scaling.png and .pdf")
plt.show()
