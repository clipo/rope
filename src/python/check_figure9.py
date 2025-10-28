"""
Verify Figure 9 calculations against paper specifications
"""

import numpy as np

print("=" * 70)
print("FIGURE 9 VERIFICATION")
print("=" * 70)

# Paper specifications
tensile_strength = 916  # MPa
packing_efficiency = 0.65  # 65% fiber packing efficiency
construction_efficiency = 0.75  # 75% construction efficiency

print("\nPaper specifications:")
print(f"- Tensile strength: {tensile_strength} MPa")
print(f"- Packing efficiency: {packing_efficiency} (65%)")
print(f"- Construction efficiency: {construction_efficiency} (75%)")
print(f"- Paper formula: Breaking Load (kN) = 0.35 × D²")

# Figure 9 code (LEFT PANEL)
print("\n" + "=" * 70)
print("LEFT PANEL: Breaking Load vs Diameter")
print("=" * 70)

diameters = [10, 20, 45]

print("\nFigure 9 code calculations (WITHOUT packing efficiency):")
for d in diameters:
    area = np.pi * (d/2)**2  # mm²
    breaking_load = tensile_strength * area * construction_efficiency / 1000  # kN
    print(f"  D = {d} mm: Breaking Load = {breaking_load:.1f} kN")

print("\nCorrected calculations (WITH packing efficiency):")
for d in diameters:
    area = np.pi * (d/2)**2  # mm²
    effective_area = area * packing_efficiency
    breaking_load = tensile_strength * effective_area * construction_efficiency / 1000  # kN
    print(f"  D = {d} mm: Breaking Load = {breaking_load:.1f} kN")

print("\nPaper formula (0.35 × D²):")
for d in diameters:
    breaking_load = 0.35 * d**2
    print(f"  D = {d} mm: Breaking Load = {breaking_load:.1f} kN")

# Figure 9 code (RIGHT PANEL)
print("\n" + "=" * 70)
print("RIGHT PANEL: Required Rope Diameter vs Moai Mass")
print("=" * 70)

moai_masses = [4, 80, 86]
safety_factor = 10

print(f"\nAssumptions: 1 kN per ton, safety factor = {safety_factor}")

print("\nFigure 9 code calculations (WITHOUT packing efficiency):")
for mass in moai_masses:
    force_per_rope = mass * 1000  # N
    required_breaking_load = force_per_rope * safety_factor / 1000  # kN
    required_diameter = 2 * np.sqrt(required_breaking_load * 1000 /
                                    (tensile_strength * construction_efficiency * np.pi))
    print(f"  {mass} ton moai: Required diameter = {required_diameter:.1f} mm")

print("\nCorrected calculations (WITH packing efficiency):")
for mass in moai_masses:
    force_per_rope = mass * 1000  # N
    required_breaking_load = force_per_rope * safety_factor / 1000  # kN
    required_diameter = 2 * np.sqrt(required_breaking_load * 1000 /
                                    (tensile_strength * packing_efficiency * construction_efficiency * np.pi))
    print(f"  {mass} ton moai: Required diameter = {required_diameter:.1f} mm")

print("\n" + "=" * 70)
print("ISSUE IDENTIFIED:")
print("Figure 9 is missing the fiber packing efficiency factor (0.65)")
print("This causes it to overestimate breaking load by ~54% (1/0.65)")
print("and underestimate required rope diameter by ~24% (1/sqrt(0.65))")
print("=" * 70)
