"""
Calculate rope diameter for Paro at 82 tons instead of 86 tons
"""

import numpy as np

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

print("=" * 70)
print("PARO MASS CORRECTION: 86 tons → 82 tons")
print("=" * 70)

print("\nRope diameter calculations:")
print(f"Paro at 86 tons: {calc_rope_diameter(86):.1f} mm")
print(f"Paro at 82 tons: {calc_rope_diameter(82):.1f} mm")
print(f"Difference: {calc_rope_diameter(86) - calc_rope_diameter(82):.1f} mm")

print("\nComparison to handling limits:")
print(f"Paro at 82 tons: {calc_rope_diameter(82):.1f} mm")
print(f"Practical handling limit: 50.0 mm")
print(f"Distance from limit: {50.0 - calc_rope_diameter(82):.1f} mm")

print("\nInterpretation:")
if calc_rope_diameter(82) < 50:
    print(f"At 82 tons, Paro requires {calc_rope_diameter(82):.1f} mm diameter rope,")
    print("which is just BELOW the 50 mm practical handling limit.")
    print("This is still approaching the limit, but not quite at it.")
else:
    print(f"At 82 tons, Paro requires {calc_rope_diameter(82):.1f} mm diameter rope,")
    print("which is AT or ABOVE the 50 mm practical handling limit.")

print("\nOther moai for context:")
for mass in [80, 82, 85, 86, 90]:
    print(f"  {mass} tons: {calc_rope_diameter(mass):.1f} mm")

print("=" * 70)
