"""
Figure 11: Rope Diameter Requirements Across the Documented Spectrum of Moai Sizes

This script generates a two-panel figure showing:
- Top: Bar chart of specific named moai with rope diameter requirements
- Bottom: Continuous relationship between moai mass and rope diameter

Demonstrates where rope technology reaches its physical impossibility limit.
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
fig, (ax_top, ax_bottom) = plt.subplots(2, 1, figsize=(12, 10))

# ============================================================================
# DATA FOR SPECIFIC MOAI SPECIMENS
# ============================================================================

moai_names = ['Experimental\nReplica', 'Ahu Akivi\n(typical)', 'Paro',
              'Ahu Tongariki\n(largest)', 'Te Tokanga\n(quarry)']
moai_masses = np.array([4.3, 18, 86, 90, 260])  # metric tons

# Rope calculation parameters
tensile_strength = 916  # MPa for T. cordifolia
efficiency = 0.75  # rope construction efficiency
safety_factors_sf10 = 10
safety_factors_sf5 = 5

# Calculate required rope diameter
# Assume working load = 1 kN per ton (simplified)
working_load = moai_masses * 1.0  # kN

# Calculate required breaking load
required_breaking_load_sf10 = working_load * safety_factors_sf10  # kN
required_breaking_load_sf5 = working_load * safety_factors_sf5  # kN

# Calculate diameter: d = 2 × sqrt(Breaking_load / (tensile_strength × π × efficiency))
required_diameter_sf10 = 2 * np.sqrt(required_breaking_load_sf10 * 1000 / 
                                     (tensile_strength * efficiency * np.pi))
required_diameter_sf5 = 2 * np.sqrt(required_breaking_load_sf5 * 1000 / 
                                    (tensile_strength * efficiency * np.pi))

# Colors based on transport status
colors = ['green', 'blue', 'orange', 'orange', 'red']
markers = ['o', 's', '^', '^', 'X']

# ============================================================================
# TOP PANEL: Bar Chart of Specific Moai
# ============================================================================

x_pos = np.arange(len(moai_names))
width = 0.3

# Plot bars for both safety factors
bars1 = ax_top.bar(x_pos - width/2, required_diameter_sf10, width, 
                   label='Safety factor = 10', 
                   color=colors, alpha=0.7, edgecolor='black', linewidth=1.5)

bars2 = ax_top.bar(x_pos + width/2, required_diameter_sf5, width, 
                   label='Safety factor = 5', 
                   color=colors, alpha=0.4, edgecolor='black', 
                   linewidth=1.5, hatch='//')

# Add horizontal reference lines
ax_top.axhline(y=40, color='orange', linestyle='--', linewidth=2, alpha=0.7, 
               label='Difficult to grip (40 mm)')
ax_top.axhline(y=50, color='red', linestyle='-', linewidth=2.5, alpha=0.8, 
               label='Maximum grip limit (50 mm)')
ax_top.axhline(y=70, color='darkred', linestyle=':', linewidth=2, alpha=0.6, 
               label='Physically impossible (70 mm)')

# Shaded zones
ax_top.fill_between([-0.5, len(moai_names)-0.5], 0, 40, alpha=0.1, 
                     color='green', label='Comfortable range')
ax_top.fill_between([-0.5, len(moai_names)-0.5], 40, 50, alpha=0.1, 
                     color='orange')
ax_top.fill_between([-0.5, len(moai_names)-0.5], 50, 150, alpha=0.15, 
                     color='red')

# Add value labels on bars
for i, (d1, d2) in enumerate(zip(required_diameter_sf10, required_diameter_sf5)):
    if d1 < 100:
        ax_top.text(i - width/2, d1 + 2, f'{d1:.0f}', ha='center', 
                    va='bottom', fontsize=8, fontweight='bold')
    if d2 < 100:
        ax_top.text(i + width/2, d2 + 2, f'{d2:.0f}', ha='center', 
                    va='bottom', fontsize=8, fontweight='bold')
    else:
        ax_top.text(i + width/2, 140, f'{d2:.0f}', ha='center', 
                    va='top', fontsize=8, fontweight='bold', color='red')

# Annotations
ax_top.annotate('Successfully\ntransported', xy=(1, 25), xytext=(1, 35),
                arrowprops=dict(arrowstyle='->', color='blue', lw=1.5),
                fontsize=8, ha='center', color='blue', fontweight='bold')

ax_top.annotate('Largest transported\n(still within limits)', xy=(3, 41), xytext=(3.5, 55),
                arrowprops=dict(arrowstyle='->', color='orange', lw=1.5),
                fontsize=8, ha='center', color='darkorange', fontweight='bold')

ax_top.annotate('Impossible with\navailable technology',
                xy=(4, 102), xytext=(3.8, 120),
                arrowprops=dict(arrowstyle='->', color='darkred', lw=2),
                fontsize=9, ha='center', color='darkred', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.3))

# Formatting
ax_top.set_ylabel('Required Rope Diameter (mm)', fontweight='bold')
ax_top.set_title('Rope Diameter Requirements for Documented Moai Specimens', 
                 fontsize=14, fontweight='bold')
ax_top.set_xticks(x_pos)
ax_top.set_xticklabels(moai_names, fontsize=9)
ax_top.set_ylim(0, 150)
ax_top.legend(loc='upper left', fontsize=8, ncol=2)
ax_top.grid(True, alpha=0.3, axis='y')

# ============================================================================
# BOTTOM PANEL: Continuous Relationship
# ============================================================================

# Generate continuous curves
moai_range = np.linspace(1, 300, 500)
working_load_range = moai_range * 1.0
required_breaking_load_range_sf10 = working_load_range * 10
required_breaking_load_range_sf5 = working_load_range * 5

diameter_sf10 = 2 * np.sqrt(required_breaking_load_range_sf10 * 1000 / 
                            (tensile_strength * efficiency * np.pi))
diameter_sf5 = 2 * np.sqrt(required_breaking_load_range_sf5 * 1000 / 
                           (tensile_strength * efficiency * np.pi))

# Plot continuous curves
ax_bottom.plot(moai_range, diameter_sf10, 'b-', linewidth=2.5, 
               label='Required diameter (SF=10)', alpha=0.8)
ax_bottom.plot(moai_range, diameter_sf5, 'b--', linewidth=2, 
               label='Required diameter (SF=5)', alpha=0.6)

# Add horizontal reference lines
ax_bottom.axhline(y=40, color='orange', linestyle='--', linewidth=2, alpha=0.7)
ax_bottom.axhline(y=50, color='red', linestyle='-', linewidth=2.5, alpha=0.8)
ax_bottom.axhline(y=70, color='darkred', linestyle=':', linewidth=2, alpha=0.6)

# Shaded zones
ax_bottom.fill_between(moai_range, 0, 40, alpha=0.1, color='green')
ax_bottom.fill_between(moai_range, 40, 50, alpha=0.1, color='orange')
ax_bottom.fill_between(moai_range, 50, 150, alpha=0.15, color='red')

# Plot specific moai as points
for i, (mass, diam, name, color, marker) in enumerate(
        zip(moai_masses, required_diameter_sf10, moai_names, colors, markers)):
    markersize = 12 if mass < 100 else 15
    markeredgewidth = 1.5 if mass < 100 else 2
    ax_bottom.plot(mass, diam, marker=marker, markersize=markersize, 
                   color=color, markeredgecolor='black', 
                   markeredgewidth=markeredgewidth, 
                   label=name.replace('\n', ' '), zorder=5)

# Add zone labels
ax_bottom.text(150, 20, 'FEASIBLE RANGE\n(comfortable grip)',
               ha='center', fontsize=10, fontweight='bold', color='darkgreen',
               bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.3))

ax_bottom.text(150, 45, 'CHALLENGING\n(approaching limits)',
               ha='center', fontsize=9, fontweight='bold', color='darkorange',
               bbox=dict(boxstyle='round', facecolor='orange', alpha=0.2))

ax_bottom.text(200, 100, 'IMPOSSIBLE\n(exceeds grip capability)',
               ha='center', fontsize=10, fontweight='bold', color='darkred',
               bbox=dict(boxstyle='round', facecolor='red', alpha=0.2))

# Add transport limit line
transport_limit_mass = 90
ax_bottom.axvline(x=transport_limit_mass, color='purple', linestyle='-.', 
                  linewidth=2, alpha=0.5)
ax_bottom.text(transport_limit_mass + 5, 130, 
               'Observed transport\nlimit (~90 tons)', 
               fontsize=8, color='purple', fontweight='bold')

# Formatting
ax_bottom.set_xlabel('Moai Mass (metric tons)', fontweight='bold')
ax_bottom.set_ylabel('Required Rope Diameter (mm)', fontweight='bold')
ax_bottom.set_title('Physical Limits of Rope Technology for Moai Transport', 
                    fontsize=13, fontweight='bold')
ax_bottom.set_xlim(0, 300)
ax_bottom.set_ylim(0, 150)
ax_bottom.legend(loc='upper left', fontsize=8, ncol=2)
ax_bottom.grid(True, alpha=0.3)

# Save figure
plt.tight_layout()
import os
os.makedirs('figures', exist_ok=True)
plt.savefig('figures/figure11_moai_progression.png', dpi=600, bbox_inches='tight')
plt.savefig('figures/figure11_moai_progression.pdf', dpi=600, bbox_inches='tight')

# Print summary data
print("Figure 11 saved: figures/figure11_moai_progression.png and .pdf")
print("\nRope diameter requirements:")
print("-" * 70)
for name, mass, diam_10, diam_5 in zip(moai_names, moai_masses, 
                                        required_diameter_sf10, 
                                        required_diameter_sf5):
    print(f"{name.replace(chr(10), ' '):30s}: {mass:6.1f} tons → "
          f"{diam_10:5.1f} mm (SF=10), {diam_5:5.1f} mm (SF=5)")
print("-" * 70)

plt.show()
