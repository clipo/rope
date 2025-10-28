"""
Verification Script: Rope Diameter Calculations
Confirms all moai rope diameter requirements are calculated correctly
"""

import numpy as np

# Parameters
tensile_strength = 916  # MPa for T. cordifolia
efficiency = 0.75  # rope construction efficiency
safety_factor = 10

# Moai data
moai_data = [
    ('Experimental Replica', 4.3),
    ('Ahu Akivi (typical)', 18.0),
    ('Paro', 86.0),
    ('Ahu Tongariki (largest transported)', 90.0),
    ('Te Tokanga (quarry, never moved)', 260.0)
]

print("=" * 80)
print("ROPE DIAMETER VERIFICATION - MOAI TRANSPORT ANALYSIS")
print("=" * 80)
print(f"\nParameters:")
print(f"  Tensile strength: {tensile_strength} MPa")
print(f"  Construction efficiency: {efficiency * 100}%")
print(f"  Safety factor: {safety_factor}")
print(f"  Working load estimate: 1 kN per ton")
print()
print("=" * 80)
print(f"{'Moai Specimen':<40} {'Mass':<10} {'Rope Ø':<12} {'Status'}")
print("=" * 80)

# Reference limits
limit_comfortable = 40  # mm
limit_practical = 50    # mm
limit_impossible = 70   # mm

for name, mass in moai_data:
    # Calculate rope diameter
    working_load = mass * 1.0  # kN
    required_breaking_load = working_load * safety_factor  # kN
    diameter = 2 * np.sqrt(required_breaking_load * 1000 /
                          (tensile_strength * efficiency * np.pi))

    # Determine status
    if diameter < limit_comfortable:
        status = "✓ Comfortable"
        color = "GREEN"
    elif diameter < limit_practical:
        status = "⚠ Approaching limit"
        color = "YELLOW"
    elif diameter < limit_impossible:
        status = "✗ Exceeds practical limit"
        color = "RED"
    else:
        status = "✗✗ Physically impossible"
        color = "DARK RED"

    print(f"{name:<40} {mass:>6.1f} t   {diameter:>6.1f} mm   {status}")

print("=" * 80)
print("\nKey Findings:")
print("-" * 80)
print(f"• Comfortable range (< {limit_comfortable} mm):")
print(f"  - Experimental Replica (4.3 t): 8.9 mm")
print(f"  - Ahu Akivi (18 t): 18.3 mm")
print()
print(f"• Approaching limit ({limit_comfortable}-{limit_practical} mm):")
print(f"  - Paro (86 t): 39.9 mm - STILL WITHIN LIMITS")
print(f"  - Ahu Tongariki (90 t): 40.8 mm - STILL WITHIN LIMITS")
print()
print(f"• Exceeds practical limit (> {limit_practical} mm):")
print(f"  - Te Tokanga (260 t): 69.4 mm - EXCEEDS LIMITS")
print()
print("=" * 80)
print("\nConclusion:")
print("-" * 80)
print("The largest successfully transported moai (Paro: 86t, Ahu Tongariki: 90t)")
print("required rope diameters of ~40 mm, which is WITHIN the 50 mm practical")
print("handling limit. This suggests that rope technology was NOT the limiting")
print("factor for moai transport at these sizes.")
print()
print("Only Te Tokanga (260 tons, never transported) would have required rope")
print("diameter (~69 mm) that exceeds practical human grip capability.")
print("=" * 80)

# Verify specific values mentioned in captions
print("\nCaption Value Verification:")
print("-" * 80)

# Check 45 mm rope breaking load
diameter_45 = 45
area_45 = np.pi * (diameter_45/2)**2
breaking_load_45 = tensile_strength * area_45 * efficiency / 1000
print(f"45 mm rope breaking load: {breaking_load_45:.0f} kN (caption should say 1,093 kN, NOT 650 kN)")

# Check Paro requirement
paro_mass = 86
working_load_paro = paro_mass * 1.0
required_breaking_load_paro = working_load_paro * safety_factor
diameter_paro = 2 * np.sqrt(required_breaking_load_paro * 1000 /
                            (tensile_strength * efficiency * np.pi))
print(f"Paro rope requirement: {diameter_paro:.1f} mm (caption should say 40 mm, NOT 57 mm)")

print("=" * 80)
