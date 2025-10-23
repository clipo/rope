"""
Figure 5: Rope Requirements Across Moai Transport Scenarios

This script generates a multi-axis bar chart comparing rope diameter requirements,
moai mass, and workforce requirements across different moai categories.
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
fig, ax1 = plt.subplots(figsize=(10, 8))

# ============================================================================
# Data for Different Moai Categories
# ============================================================================

categories = ['Quarry\n(incomplete)', 'Road\n(abandoned)', 
              'Platform\n(transported)', 'Paro\n(transported)']

# Typical values for each category
typical_mass = [15, 12, 14, 86]  # tons

# Calculate rope diameter consistently with other figures
# Using: working_load = mass * 1.0 kN/ton, SF=10, 916 MPa, 75% efficiency
tensile_strength = 916  # MPa
efficiency = 0.75
safety_factor = 10
rope_diameter_required = []
for mass in typical_mass:
    working_load = mass * 1.0  # kN
    required_breaking_load = working_load * safety_factor
    diameter = 2 * np.sqrt(required_breaking_load * 1000 / (tensile_strength * efficiency * np.pi))
    rope_diameter_required.append(diameter)

people_required = [10, 8, 10, 60]  # estimated people per rope team

x = np.arange(len(categories))
width = 0.25

# ============================================================================
# Create Three Y-Axes
# ============================================================================

# Second y-axis (mass)
ax2 = ax1.twinx()

# Third y-axis (people) - offset to the right
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))

# ============================================================================
# Plot Bars for Each Variable
# ============================================================================

# Rope diameter (left y-axis)
bars1 = ax1.bar(x - width, rope_diameter_required, width, 
                label='Rope diameter (mm)', 
                color='steelblue', alpha=0.8)

# Moai mass (right y-axis 1)
bars2 = ax2.bar(x, typical_mass, width, 
                label='Moai mass (tons)', 
                color='coral', alpha=0.8)

# People per rope (right y-axis 2)
bars3 = ax3.bar(x + width, people_required, width, 
                label='People per rope', 
                color='lightgreen', alpha=0.8)

# ============================================================================
# Add Handling Limit Reference Line
# ============================================================================

ax1.axhline(y=50, color='red', linestyle='--', linewidth=2, alpha=0.5)
ax1.text(0.5, 52, 'Practical handling limit (50 mm)', 
         fontsize=9, color='red')

# ============================================================================
# Add Annotation for Paro
# ============================================================================

paro_diameter = rope_diameter_required[3]  # Paro is 4th category
ax1.annotate('Paro approaches\npractical\nhandling limits',
             xy=(3, paro_diameter), xytext=(2.5, 55),
             arrowprops=dict(arrowstyle='->', color='orange', lw=1.5),
             fontsize=9, color='darkorange', weight='bold',
             bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.3))

# ============================================================================
# Labels and Formatting
# ============================================================================

# X-axis
ax1.set_xlabel('Moai Category', fontsize=11)
ax1.set_xticks(x)
ax1.set_xticklabels(categories)

# Y-axes labels
ax1.set_ylabel('Rope Diameter (mm)', color='steelblue', fontsize=11)
ax2.set_ylabel('Moai Mass (tons)', color='coral', fontsize=11)
ax3.set_ylabel('People per Rope Team', color='green', fontsize=11)

# Title
ax1.set_title('Rope Requirements Across Moai Transport Scenarios', 
              fontsize=13, weight='bold')

# Tick colors
ax1.tick_params(axis='y', labelcolor='steelblue')
ax2.tick_params(axis='y', labelcolor='coral')
ax3.tick_params(axis='y', labelcolor='green')

# Y-axis limits
ax1.set_ylim(0, 70)
ax2.set_ylim(0, 100)
ax3.set_ylim(0, 70)

# Grid
ax1.grid(True, alpha=0.3, axis='y')

# ============================================================================
# Combined Legend
# ============================================================================

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
ax1.legend(lines1 + lines2 + lines3, labels1 + labels2 + labels3, 
           loc='upper left', fontsize=9)

# Save figure
plt.tight_layout()
import os
os.makedirs('figures', exist_ok=True)
plt.savefig('figures/figure5_transport_scenarios.png', dpi=600, bbox_inches='tight')
plt.savefig('figures/figure5_transport_scenarios.pdf', dpi=600, bbox_inches='tight')
print("Figure 5 saved: figures/figure5_transport_scenarios.png and .pdf")
plt.show()
