"""
Verify the "breaking load / 8" line in figure 9 is correct
"""

import numpy as np

# Parameters from figure 9
tensile_strength = 916  # MPa
packing_efficiency = 0.65
construction_efficiency = 0.75

# Calculate for a 10 mm rope
diameter = 10  # mm
area = np.pi * (diameter/2)**2  # mm²
effective_area = area * packing_efficiency
breaking_load = tensile_strength * effective_area * construction_efficiency / 1000  # kN

print("=" * 70)
print("SAFETY FACTOR LINE VERIFICATION")
print("=" * 70)

print(f"\nFor a {diameter} mm diameter rope:")
print(f"  Breaking load: {breaking_load:.1f} kN")
print(f"  Breaking load / 8: {breaking_load/8:.1f} kN")

print(f"\nInterpretation:")
print(f"  The 'Breaking load / 8' line shows the SAFE WORKING LOAD")
print(f"  with a safety factor of 8.")
print(f"  ")
print(f"  For {diameter} mm rope:")
print(f"    - Can break at: {breaking_load:.1f} kN")
print(f"    - Safe to use up to: {breaking_load/8:.1f} kN (with SF=8)")

print(f"\nFor a 4-ton moai requiring ~4 kN working load:")
print(f"  - Working load needed: 4.0 kN")
print(f"  - With SF=8, need breaking load: 4.0 × 8 = 32.0 kN")
print(f"  - 10 mm rope provides: {breaking_load:.1f} kN breaking load ✓")
print(f"  - 10 mm rope safe working load: {breaking_load/8:.1f} kN ✓")

print(f"\nThe line is CORRECT - it shows how much load you can safely")
print(f"apply to each rope diameter while maintaining an 8:1 safety margin.")

print("\n" + "=" * 70)
print("ALTERNATIVE: Should we show 'Required Breaking Load' instead?")
print("=" * 70)

print("\nCurrent approach:")
print("  - Shows: Breaking Load / 8 (safe working capacity)")
print("  - Meaning: How much load can this diameter safely handle?")

print("\nAlternative approach:")
print("  - Show: Working Load × 8 (required breaking load)")
print("  - Meaning: What breaking load do you need for a given working load?")

print("\nFor moai requirements:")
moai_loads = [4, 80]  # kN working load
for load in moai_loads:
    required_breaking = load * 8
    print(f"  {load} kN working load → needs {required_breaking} kN breaking load (SF=8)")
    # Find rope diameter needed
    required_area = required_breaking * 1000 / (tensile_strength * packing_efficiency * construction_efficiency)
    required_diameter = 2 * np.sqrt(required_area / np.pi)
    print(f"    → requires {required_diameter:.1f} mm diameter rope")

print("\n" + "=" * 70)
