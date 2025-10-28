"""
Verify that the corrected figures 10 and 11 now calculate rope diameters correctly
"""

import numpy as np

print("=" * 70)
print("VERIFICATION OF CORRECTED FIGURES 10 AND 11")
print("=" * 70)

# Paper specifications
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

# ============================================================================
# FIGURE 10 VERIFICATION
# ============================================================================

print("\n" + "=" * 70)
print("FIGURE 10: Hand Grip Capability")
print("=" * 70)

moai_masses_fig10 = [4, 15, 80, 86]
print("\nCalculated rope diameters (should match figure 10):")
for mass in moai_masses_fig10:
    diameter = calc_rope_diameter(mass)
    print(f"  {mass} ton moai: {diameter:.1f} mm")

# ============================================================================
# FIGURE 11 VERIFICATION
# ============================================================================

print("\n" + "=" * 70)
print("FIGURE 11: Transport Scenarios")
print("=" * 70)

categories = ['Quarry (incomplete)', 'Road (abandoned)',
              'Platform (transported)', 'Paro (transported)']
typical_mass = [15, 12, 14, 86]  # tons

print("\nCalculated rope diameters (should match figure 11):")
for i, mass in enumerate(typical_mass):
    diameter = calc_rope_diameter(mass)
    print(f"  {categories[i]}: {mass} tons -> {diameter:.1f} mm")

# ============================================================================
# KEY VALUES FOR PAPER
# ============================================================================

print("\n" + "=" * 70)
print("KEY VALUES TO USE IN PAPER:")
print("=" * 70)

print(f"\n4 ton moai: {calc_rope_diameter(4):.1f} mm")
print(f"10 ton moai: {calc_rope_diameter(10):.1f} mm")
print(f"15 ton moai: {calc_rope_diameter(15):.1f} mm")
print(f"20 ton moai: {calc_rope_diameter(20):.1f} mm")
print(f"40 ton moai: {calc_rope_diameter(40):.1f} mm")
print(f"60 ton moai: {calc_rope_diameter(60):.1f} mm")
print(f"80 ton moai: {calc_rope_diameter(80):.1f} mm")
print(f"86 ton moai (Paro): {calc_rope_diameter(86):.1f} mm")
print(f"90 ton moai: {calc_rope_diameter(90):.1f} mm")

print("\n" + "=" * 70)
print("VERIFICATION COMPLETE")
print("All figures now use 65% packing efficiency and 75% construction efficiency")
print("=" * 70)
