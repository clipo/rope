"""
Figure 7: Rope Production Investment Analysis

This script generates a four-panel figure showing:
- Panel A: Fiber mass required vs moai mass
- Panel B: Production timeline (harvesting, retting, construction)
- Panel C: Person-days of labor vs moai mass
- Panel D: Cumulative investment vs transport distance

Based on experimental data from Folk (2018) and traditional
fiber processing techniques.
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

# Create figure with 2x2 subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 11))

# ============================================================================
# PARAMETERS FROM LITERATURE AND CALCULATIONS
# ============================================================================

# Rope requirements (from our analysis)
moai_masses = np.array([4.3, 18, 40, 60, 86])  # tons
moai_labels = ['Experimental\n4.3t', 'Typical\n18t', 'Large\n40t',
               'Very Large\n60t', 'Paro\n86t']

# Calculate rope diameter needed (SF=10, 916 MPa, 75% efficiency)
tensile_strength = 916  # MPa
efficiency = 0.75
safety_factor = 10
working_load = moai_masses * 1.0  # kN/ton
required_breaking_load = working_load * safety_factor
rope_diameter = 2 * np.sqrt(required_breaking_load * 1000 /
                            (tensile_strength * efficiency * np.pi))

# From Folk (2018): experimental rope data
# 6,000g fiber from 2 trees, 4m rope used 1,200g
# For 30.5m rope: ~9,150g needed, ~3 trees
# Scaling: 300g fiber per meter of rope for their diameter

# Estimate fiber mass per meter for different diameters
# Assuming linear density scales with cross-sectional area (diameter²)
experimental_diameter = 25  # mm (estimated from their experiment)
experimental_fiber_per_meter = 300  # g/m

# Scale to our rope diameters
fiber_per_meter = experimental_fiber_per_meter * (rope_diameter / experimental_diameter)**2

# Assume 3 ropes per moai (2 lateral, 1 stabilizing)
# Average rope length: 30m (from experiments)
rope_length = 30  # meters per rope
n_ropes = 3

# Total fiber mass needed (kg)
total_fiber_mass = (fiber_per_meter * rope_length * n_ropes) / 1000  # convert to kg

# ============================================================================
# PANEL 1 (TOP LEFT): Fiber Mass Required
# ============================================================================

ax1.bar(range(len(moai_masses)), total_fiber_mass, color='steelblue',
        alpha=0.7, edgecolor='black', linewidth=1.5)
ax1.set_ylabel('Total Fiber Mass Required (kg)', fontweight='bold')
ax1.set_xlabel('Moai Specimen', fontweight='bold')
ax1.set_xticks(range(len(moai_masses)))
ax1.set_xticklabels(moai_labels, fontsize=8)
ax1.set_title('A. Fiber Requirements for Rope Production',
              fontweight='bold', fontsize=12)
ax1.grid(True, alpha=0.3, axis='y')

# Add value labels on bars
for i, mass in enumerate(total_fiber_mass):
    ax1.text(i, mass + max(total_fiber_mass)*0.02, f'{mass:.1f} kg',
             ha='center', va='bottom', fontsize=8, fontweight='bold')

# ============================================================================
# PANEL 2 (TOP RIGHT): Production Timeline
# ============================================================================

# Time estimates (days) based on traditional practices and Lipo & Makowsky
# Harvesting: ~0.5 days per kg of fiber (with small team)
# Retting: 38 days (fixed, can be done in parallel for all fiber)
# Drying/preparation: ~3 days
# Rope construction: ~0.3 days per meter of finished rope (with 2-4 people)

harvesting_time = total_fiber_mass * 0.5
retting_time = 38  # fixed (from paper)
preparation_time = 3  # fixed
construction_time = (rope_length * n_ropes) * 0.3

# Create stacked bar chart
width = 0.6
x_pos = np.arange(len(moai_masses))

p1 = ax2.bar(x_pos, harvesting_time, width, label='Harvesting & Processing',
             color='darkgreen', alpha=0.7)
p2 = ax2.bar(x_pos, np.ones(len(moai_masses)) * retting_time, width,
             bottom=harvesting_time, label='Retting (can be parallel)',
             color='orange', alpha=0.7)
p3 = ax2.bar(x_pos, np.ones(len(moai_masses)) * preparation_time, width,
             bottom=harvesting_time + retting_time,
             label='Drying/Preparation', color='lightblue', alpha=0.7)
p4 = ax2.bar(x_pos, construction_time, width,
             bottom=harvesting_time + retting_time + preparation_time,
             label='Rope Construction', color='brown', alpha=0.7)

ax2.set_ylabel('Time (days)', fontweight='bold')
ax2.set_xlabel('Moai Specimen', fontweight='bold')
ax2.set_xticks(x_pos)
ax2.set_xticklabels(moai_labels, fontsize=8)
ax2.set_title('B. Production Timeline for Rope Sets',
              fontweight='bold', fontsize=12)
ax2.legend(loc='upper left', fontsize=8)
ax2.grid(True, alpha=0.3, axis='y')

# Add total time labels
total_time = harvesting_time + retting_time + preparation_time + construction_time
for i, tt in enumerate(total_time):
    ax2.text(i, tt + 2, f'{tt:.0f}d', ha='center', va='bottom',
             fontsize=8, fontweight='bold')

# ============================================================================
# PANEL 3 (BOTTOM LEFT): Labor Investment (Person-Days)
# ============================================================================

# Estimate person-days for each stage
# Harvesting: 3-4 people
# Retting: minimal supervision (0.5 person-days)
# Preparation: 2 people
# Construction: 2-4 people (scales with rope diameter)

people_harvesting = 3
people_retting = 0.5 / retting_time  # minimal daily supervision
people_preparation = 2
people_construction = 2 + (rope_diameter / 20)  # more people for thicker rope

# Person-days for each stage
pd_harvesting = harvesting_time * people_harvesting
pd_retting = retting_time * people_retting
pd_preparation = preparation_time * people_preparation
pd_construction = construction_time * people_construction

# Total person-days
total_person_days = pd_harvesting + pd_retting + pd_preparation + pd_construction

# Create grouped bar chart
x_pos = np.arange(len(moai_masses))
width = 0.15

p1 = ax3.bar(x_pos - 1.5*width, pd_harvesting, width,
             label='Harvesting', color='darkgreen', alpha=0.7)
p2 = ax3.bar(x_pos - 0.5*width, pd_retting, width,
             label='Retting (supervision)', color='orange', alpha=0.7)
p3 = ax3.bar(x_pos + 0.5*width, pd_preparation, width,
             label='Preparation', color='lightblue', alpha=0.7)
p4 = ax3.bar(x_pos + 1.5*width, pd_construction, width,
             label='Construction', color='brown', alpha=0.7)

ax3.set_ylabel('Person-Days of Labor', fontweight='bold')
ax3.set_xlabel('Moai Specimen', fontweight='bold')
ax3.set_xticks(x_pos)
ax3.set_xticklabels(moai_labels, fontsize=8)
ax3.set_title('C. Labor Investment for Rope Production',
              fontweight='bold', fontsize=12)
ax3.legend(loc='upper left', fontsize=8)
ax3.grid(True, alpha=0.3, axis='y')

# Set y-axis limit to accommodate labels
ax3.set_ylim(0, max(total_person_days) * 1.15)

# Add total person-days labels
for i, tpd in enumerate(total_person_days):
    ax3.text(i, tpd + max(total_person_days)*0.03, f'Total:\n{tpd:.0f}',
             ha='center', va='bottom', fontsize=7, fontweight='bold')

# ============================================================================
# PANEL 4 (BOTTOM RIGHT): Cumulative Investment vs Transport Distance
# ============================================================================

# Model: rope degradation requires replacement over distance
# Assume rope lasts for 1-2 km of transport, then needs replacement
# Transport distances from quarry: 1-18 km (average ~6 km)

distances = np.array([0.5, 1, 2, 5, 10, 15, 18])  # km
rope_lifetime_km = 1.5  # km per rope set (conservative estimate)

# Calculate cumulative person-days for each moai type over distance
colors_line = ['green', 'blue', 'purple', 'orange', 'red']

for i, (mass, label, color) in enumerate(zip(moai_masses, moai_labels, colors_line)):
    # Number of rope sets needed
    rope_sets_needed = np.ceil(distances / rope_lifetime_km)
    # Cumulative person-days
    cumulative_pd = rope_sets_needed * total_person_days[i]

    ax4.plot(distances, cumulative_pd, 'o-', linewidth=2, markersize=6,
             label=label.replace('\n', ' '), color=color, alpha=0.8)

ax4.set_xlabel('Transport Distance (km)', fontweight='bold')
ax4.set_ylabel('Cumulative Person-Days (Rope Production)', fontweight='bold')
ax4.set_title('D. Cumulative Labor Investment vs Transport Distance',
              fontweight='bold', fontsize=12)
ax4.legend(loc='upper left', fontsize=8)
ax4.grid(True, alpha=0.3)

# Add reference lines
ax4.axvline(x=6, color='gray', linestyle='--', linewidth=1, alpha=0.5)
ax4.text(6.2, ax4.get_ylim()[1]*0.95, 'Average transport\ndistance (~6 km)',
         fontsize=8, color='gray')

# ============================================================================
# SUMMARY STATISTICS
# ============================================================================

print("\n" + "="*70)
print("ROPE PRODUCTION INVESTMENT ANALYSIS")
print("="*70)
print("\nBased on experimental data from Folk (2018)")
print("Assumptions:")
print("  - 3 ropes per moai (2 lateral, 1 stabilizing)")
print("  - 30m average rope length")
print("  - Fiber requirements scale with rope diameter²")
print("  - Retting time: 38 days (can process multiple batches in parallel)")
print("  - Rope lifetime: ~1.5 km of transport")
print("\n" + "-"*70)
print(f"{'Moai Type':<20} {'Mass':<8} {'Fiber':<10} {'Days':<8} {'Person-Days':<12} {'Ropes/6km'}")
print("-"*70)

for i, (mass, label) in enumerate(zip(moai_masses, moai_labels)):
    label_clean = label.replace('\n', ' ')
    rope_sets_6km = np.ceil(6 / rope_lifetime_km)
    cumulative_6km = rope_sets_6km * total_person_days[i]
    print(f"{label_clean:<20} {mass:>6.1f}t {total_fiber_mass[i]:>8.1f}kg "
          f"{total_time[i]:>6.0f}d {total_person_days[i]:>10.0f}pd "
          f"{rope_sets_6km:.0f} sets ({cumulative_6km:.0f}pd)")

print("-"*70)
print("\nKey Insights:")
print("  • Rope production scales 2.8× from experimental to Paro")
print("  • Most time is spent in retting (38 days), which can be parallelized")
print("  • For average 6km transport, 4 rope sets needed (replacement every ~1.5km)")
print("  • Paro (86t) required ~" + f"{total_person_days[-1]:.0f}" +
      " person-days per rope set")
print("  • Total investment for Paro over 6km: ~" +
      f"{np.ceil(6/rope_lifetime_km) * total_person_days[-1]:.0f}" + " person-days")
print("="*70 + "\n")

# Save figure
plt.tight_layout()
import os
os.makedirs('figures', exist_ok=True)
plt.savefig('figures/figure7_rope_production_investment.png', dpi=600, bbox_inches='tight')
plt.savefig('figures/figure7_rope_production_investment.pdf', dpi=600, bbox_inches='tight')
print("Figure 7 saved: figures/figure7_rope_production_investment.png and .pdf\n")
plt.show()
