"""
Figure 13: Comparative Time and Labor Investment for Rope Production Across Moai Categories

This script generates a clear visual comparison showing how rope production requirements
scale with moai size, emphasizing the practical feasibility of rope production even
for the largest transported specimens.
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

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
fig = plt.figure(figsize=(15, 10))

# Create grid for layout: top row for moai silhouettes, bottom row for 3 panels
gs = fig.add_gridspec(2, 3, height_ratios=[1.2, 1.3], hspace=0.4, wspace=0.35)

# ============================================================================
# DATA FOR MOAI SPECIMENS
# ============================================================================

moai_data = {
    'names': ['Experimental\nReplica\n(Hunt & Lipo)',
              'Typical\nPlatform\nMoai',
              'Large\nPlatform\nMoai',
              'Very Large\n(Near Limit)',
              'Paro\n(Largest\nTransported)'],
    'masses': np.array([4.3, 18, 40, 60, 86]),
    'diameters': np.array([8.9, 18.3, 27.2, 33.3, 39.9]),
    'colors': ['#2ecc71', '#3498db', '#9b59b6', '#e67e22', '#e74c3c']
}

# Calculate derived metrics
fiber_mass = np.array([3.4, 14.4, 32.0, 48.0, 68.9])  # kg
production_days = np.array([70, 75, 84, 92, 102])  # days
person_days = np.array([78, 107, 145, 178, 218])  # person-days per rope set
person_days_6km = np.array([311, 427, 581, 710, 871])  # cumulative for 6km transport

# ============================================================================
# TOP PANEL: Moai Silhouettes with Rope Requirements
# ============================================================================

ax_top = fig.add_subplot(gs[0, :])  # Spans all 3 columns in top row

# Scale moai heights for visualization (relative to largest)
max_mass = max(moai_data['masses'])
moai_heights = moai_data['masses'] / max_mass * 8  # scale for plotting
moai_widths = moai_heights * 0.35  # approximate width ratio

x_positions = np.arange(len(moai_data['names'])) * 2.5

for i, (x, h, w, name, mass, diam, fiber, color) in enumerate(
    zip(x_positions, moai_heights, moai_widths,
        moai_data['names'], moai_data['masses'], moai_data['diameters'],
        fiber_mass, moai_data['colors'])):

    # Draw simplified moai shape (rectangle for body, trapezoid for head)
    body_height = h * 0.7
    head_height = h * 0.3

    # Body
    body = Rectangle((x - w/2, 0), w, body_height,
                     facecolor=color, edgecolor='black', linewidth=2, alpha=0.7)
    ax_top.add_patch(body)

    # Head (simplified as rectangle)
    head = Rectangle((x - w/2.5, body_height), w/1.25, head_height,
                     facecolor=color, edgecolor='black', linewidth=2, alpha=0.7)
    ax_top.add_patch(head)

    # Add labels
    ax_top.text(x, -0.8, name, ha='center', va='top', fontsize=9, fontweight='bold')
    ax_top.text(x, -1.6, f'{mass:.1f} tons', ha='center', va='top', fontsize=8)

    # Rope requirements on statue
    ax_top.text(x, h + 0.3, f'Rope Ø: {diam:.1f} mm\nFiber: {fiber:.1f} kg',
                ha='center', va='bottom', fontsize=8,
                bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                         edgecolor=color, linewidth=2, alpha=0.9))

ax_top.set_xlim(-1, max(x_positions) + 1)
ax_top.set_ylim(-2.5, 11)
ax_top.set_aspect('equal')
ax_top.axis('off')
ax_top.set_title('Moai Size and Corresponding Rope Requirements',
                 fontsize=14, fontweight='bold', pad=20)

# ============================================================================
# PANEL A (BOTTOM LEFT): Production Timeline Comparison
# ============================================================================

ax_ml = fig.add_subplot(gs[1, 0])

# Stacked horizontal bar chart showing timeline breakdown
stages = ['Harvesting\n& Processing', 'Retting\n(38 days)',
          'Drying &\nPreparation', 'Rope\nConstruction']

# Time breakdown (days) for each stage
harvesting = fiber_mass * 0.5
retting = np.ones(len(moai_data['names'])) * 38
preparation = np.ones(len(moai_data['names'])) * 3
construction = np.array([27, 27, 29, 32, 41])

y_positions = np.arange(len(moai_data['names']))

# Create stacked horizontal bars
ax_ml.barh(y_positions, harvesting, color='#27ae60', alpha=0.8,
           label=stages[0], edgecolor='black', linewidth=0.5)
ax_ml.barh(y_positions, retting, left=harvesting, color='#f39c12', alpha=0.8,
           label=stages[1], edgecolor='black', linewidth=0.5)
ax_ml.barh(y_positions, preparation, left=harvesting+retting,
           color='#3498db', alpha=0.8, label=stages[2],
           edgecolor='black', linewidth=0.5)
ax_ml.barh(y_positions, construction, left=harvesting+retting+preparation,
           color='#8e44ad', alpha=0.8, label=stages[3],
           edgecolor='black', linewidth=0.5)

# Add total time labels
for i, total in enumerate(production_days):
    ax_ml.text(total + 2, i, f'{total}d', va='center', fontsize=9,
               fontweight='bold')

ax_ml.set_yticks(y_positions)
ax_ml.set_yticklabels([name.replace('\n', ' ') for name in moai_data['names']],
                       fontsize=8)
ax_ml.set_xlabel('Production Time (days)', fontweight='bold')
ax_ml.set_title('A. Production Timeline per Rope Set', fontweight='bold')
ax_ml.legend(loc='lower right', fontsize=7, framealpha=0.9)
ax_ml.grid(True, alpha=0.3, axis='x')
ax_ml.set_xlim(0, 120)

# Add note about parallelization
ax_ml.text(0.98, 0.05, 'Note: Retting can be\nparallelized across batches',
           transform=ax_ml.transAxes, ha='right', va='bottom',
           fontsize=7, style='italic',
           bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.3))

# ============================================================================
# PANEL B (BOTTOM MIDDLE): Labor Investment per Rope Set
# ============================================================================

ax_mr = fig.add_subplot(gs[1, 1])

# Bar chart of person-days
bars = ax_mr.bar(range(len(moai_data['names'])), person_days,
                 color=moai_data['colors'], alpha=0.8,
                 edgecolor='black', linewidth=1.5)

# Add value labels
for i, (pd, mass) in enumerate(zip(person_days, moai_data['masses'])):
    ax_mr.text(i, pd + 8, f'{pd:.0f}\nperson-days',
               ha='center', va='bottom', fontsize=8, fontweight='bold')

ax_mr.set_xticks(range(len(moai_data['names'])))
ax_mr.set_xticklabels([name.replace('\n', ' ') for name in moai_data['names']],
                       rotation=45, ha='right', fontsize=8)
ax_mr.set_ylabel('Person-Days of Labor', fontweight='bold')
ax_mr.set_title('B. Labor Investment per Rope Set', fontweight='bold')
ax_mr.grid(True, alpha=0.3, axis='y')
ax_mr.set_ylim(0, max(person_days) * 1.2)

# Add comparison annotation
ax_mr.annotate('', xy=(4, person_days[4]), xytext=(0, person_days[0]),
               arrowprops=dict(arrowstyle='<->', color='red', lw=2))
ax_mr.text(2, (person_days[0] + person_days[4])/2,
           f'{person_days[4]/person_days[0]:.1f}×\nincrease',
           ha='center', va='center', fontsize=9, color='red', fontweight='bold',
           bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

# ============================================================================
# PANEL C (BOTTOM RIGHT): Cumulative Investment for 6km Transport
# ============================================================================

ax_bl = fig.add_subplot(gs[1, 2])

# Grouped bar comparison: single set vs 6km transport
x_pos = np.arange(len(moai_data['names']))
width = 0.35

bars1 = ax_bl.bar(x_pos - width/2, person_days, width,
                  label='Single Rope Set', color='lightblue',
                  alpha=0.7, edgecolor='black', linewidth=1)
bars2 = ax_bl.bar(x_pos + width/2, person_days_6km, width,
                  label='6 km Transport (4 sets)', color='darkblue',
                  alpha=0.7, edgecolor='black', linewidth=1)

ax_bl.set_xticks(x_pos)
ax_bl.set_xticklabels([f'{m:.0f}t' for m in moai_data['masses']], fontsize=9)
ax_bl.set_xlabel('Moai Mass (tons)', fontweight='bold')
ax_bl.set_ylabel('Cumulative Person-Days', fontweight='bold')
ax_bl.set_title('C. Single Set vs 6 km Transport Investment', fontweight='bold')
ax_bl.legend(loc='upper left', fontsize=8)
ax_bl.grid(True, alpha=0.3, axis='y')

# Add callout for Paro
ax_bl.annotate('Paro: 871 person-days\nfor 6 km transport',
               xy=(4, person_days_6km[4]), xytext=(3, person_days_6km[4] + 200),
               arrowprops=dict(arrowstyle='->', color='red', lw=2),
               fontsize=9, color='red', fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.5))


# ============================================================================
# SAVE AND SUMMARY
# ============================================================================

plt.suptitle('Rope Production Investment: Time and Labor Requirements Across Moai Categories',
             fontsize=14, fontweight='bold', y=0.98)

plt.tight_layout()
import os
os.makedirs('figures', exist_ok=True)
plt.savefig('figures/figure13_rope_investment_comparison.png', dpi=600, bbox_inches='tight')
plt.savefig('figures/figure13_rope_investment_comparison.pdf', dpi=600, bbox_inches='tight')

# Print summary table
print("\n" + "="*90)
print("ROPE PRODUCTION INVESTMENT COMPARISON")
print("="*90)
print(f"\n{'Moai Type':<25} {'Mass':<8} {'Rope Ø':<9} {'Days':<7} {'PD/Set':<9} {'PD/6km':<10} {'% Daily Labor'}")
print("-"*90)

for i, name in enumerate(moai_data['names']):
    name_clean = name.replace('\n', ' ')
    pct_daily = (person_days_6km[i] / 700) * 100  # assuming 700 pd/day capacity (3,500 pop)
    print(f"{name_clean:<25} {moai_data['masses'][i]:>6.1f}t "
          f"{moai_data['diameters'][i]:>7.1f}mm {production_days[i]:>5.0f}d "
          f"{person_days[i]:>7.0f}pd {person_days_6km[i]:>8.0f}pd {pct_daily:>10.1f}%")

print("-"*90)
print("\nKey Metrics:")
print(f"  • Production time range: {min(production_days):.0f}-{max(production_days):.0f} days")
print(f"  • Labor per set range: {min(person_days):.0f}-{max(person_days):.0f} person-days")
print(f"  • 6km transport range: {min(person_days_6km):.0f}-{max(person_days_6km):.0f} person-days")
print(f"  • Scaling factor: {person_days[-1]/person_days[0]:.1f}× (Paro vs Experimental)")
print(f"  • Max investment: {max(person_days_6km):.0f} pd = {max(person_days_6km)/700:.1%} of daily community capacity")
print("\nConclusion: Rope production was FEASIBLE for all transported moai.")
print("Size limits reflect organizational/physiological constraints, not production capacity.")
print("="*90 + "\n")

print("Figure 13 saved: figures/figure13_rope_investment_comparison.png and .pdf")
print("\nFEASIBILITY CONTEXT FOR CAPTION:")
print("=" * 70)
print("Population: ~3,000-4,000 people (peak period)")
print("Daily labor capacity: ~600-800 person-days (20% working age)")
print("\nRope investment for 6km transport as % of daily capacity:")
print("  • Experimental (4.3t): 311 pd = ~44% (~11 hours)")
print("  • Typical (18t): 427 pd = ~61% (~15 hours)")
print("  • Paro (86t): 871 pd = ~124% (~1.2 days)")
print("\nConclusion: All rope production requirements were well within")
print("community capacity. Size limits reflect organizational constraints")
print("(rope handling, coordination) not material or production capacity.")
print("=" * 70 + "\n")
plt.show()
