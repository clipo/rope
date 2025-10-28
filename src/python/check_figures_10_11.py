"""
Verify Figures 10 and 11 calculations against paper specifications
"""

import numpy as np

print("=" * 70)
print("FIGURES 10 AND 11 VERIFICATION")
print("=" * 70)

# Paper specifications
tensile_strength = 916  # MPa
packing_efficiency = 0.65  # 65% fiber packing efficiency
construction_efficiency = 0.75  # 75% construction efficiency
safety_factor = 10

print("\nPaper specifications:")
print(f"- Tensile strength: {tensile_strength} MPa")
print(f"- Packing efficiency: {packing_efficiency} (65%)")
print(f"- Construction efficiency: {construction_efficiency} (75%)")
print(f"- Safety factor: {safety_factor}")

# ============================================================================
# FIGURE 10 VERIFICATION
# ============================================================================

print("\n" + "=" * 70)
print("FIGURE 10: Hand Grip Capability")
print("=" * 70)

# Hardcoded values in figure10.py
figure10_values = {
    4: 10,    # 4 ton moai -> 10 mm
    15: 20,   # 10-20 ton moai -> 20 mm (using 15 as midpoint)
    80: 45,   # 80 ton moai -> 45 mm
    86: 40    # Paro (86 tons) -> 40 mm
}

print("\nHardcoded values in Figure 10:")
for mass, diameter in figure10_values.items():
    print(f"  {mass} ton moai: {diameter} mm")

print("\nCorrect values (with packing efficiency):")
for mass in figure10_values.keys():
    working_load = mass * 1.0  # kN
    required_breaking_load = working_load * safety_factor  # kN
    correct_diameter = 2 * np.sqrt(required_breaking_load * 1000 /
                                   (tensile_strength * packing_efficiency * construction_efficiency * np.pi))
    hardcoded = figure10_values[mass]
    print(f"  {mass} ton moai: {correct_diameter:.1f} mm (hardcoded: {hardcoded} mm, error: {hardcoded - correct_diameter:.1f} mm)")

# ============================================================================
# FIGURE 11 VERIFICATION
# ============================================================================

print("\n" + "=" * 70)
print("FIGURE 11: Transport Scenarios")
print("=" * 70)

# Categories from figure11.py
categories = ['Quarry (incomplete)', 'Road (abandoned)',
              'Platform (transported)', 'Paro (transported)']
typical_mass = [15, 12, 14, 86]  # tons

print("\nFigure 11 code calculations (WITHOUT packing efficiency):")
for i, mass in enumerate(typical_mass):
    working_load = mass * 1.0  # kN
    required_breaking_load = working_load * safety_factor
    diameter_wrong = 2 * np.sqrt(required_breaking_load * 1000 /
                                 (tensile_strength * construction_efficiency * np.pi))
    print(f"  {categories[i]}: {mass} tons -> {diameter_wrong:.1f} mm")

print("\nCorrected calculations (WITH packing efficiency):")
for i, mass in enumerate(typical_mass):
    working_load = mass * 1.0  # kN
    required_breaking_load = working_load * safety_factor
    diameter_correct = 2 * np.sqrt(required_breaking_load * 1000 /
                                   (tensile_strength * packing_efficiency * construction_efficiency * np.pi))
    diameter_wrong = 2 * np.sqrt(required_breaking_load * 1000 /
                                 (tensile_strength * construction_efficiency * np.pi))
    print(f"  {categories[i]}: {mass} tons -> {diameter_correct:.1f} mm (was {diameter_wrong:.1f} mm, error: {diameter_wrong - diameter_correct:.1f} mm)")

print("\n" + "=" * 70)
print("ISSUES IDENTIFIED:")
print("1. Figure 10: Hardcoded rope diameter values are incorrect")
print("   - Should calculate diameters using packing efficiency")
print("   - Paro value especially wrong: 40 mm -> should be ~50 mm")
print("2. Figure 11: Missing packing efficiency factor (0.65)")
print("   - Same issue as Figure 9 had before correction")
print("=" * 70)
