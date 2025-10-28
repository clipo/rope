# Summary of Corrections to Rope Diameter Analysis

## Overview
Multiple errors were found and corrected in the figure generation scripts and captions. The primary issue was **systematic overestimation** of the rope diameter requirements for Paro and Ahu Tongariki, leading to misleading claims that these moai exceeded practical handling limits.

## Actual Rope Diameter Requirements (Safety Factor = 10)

| Moai | Mass (tons) | Required Diameter | Status |
|------|-------------|-------------------|---------|
| Experimental Replica | 4.3 | 8.9 mm | ✓ Comfortable |
| Ahu Akivi (typical) | 18.0 | 18.3 mm | ✓ Comfortable |
| **Paro** | **86.0** | **39.9 mm** | ✓ **Within practical limits** |
| **Ahu Tongariki (largest)** | **90.0** | **40.8 mm** | ✓ **Within practical limits** |
| Te Tokanga (quarry) | 260.0 | 69.4 mm | ✗ Exceeds practical limits |

**Key Finding**: The 50 mm practical handling limit is NOT exceeded by any successfully transported moai.

---

## Corrections Made

### 1. Figure 3 Caption (NOT in code - manuscript file)
**File**: Manuscript document (e.g., moai_rope.docx)

**Errors Found**:
- Stated Paro requires **57 mm** diameter rope (WRONG)
- Stated 45 mm rope has breaking load of **650 kN** (WRONG)

**Corrections**:
- Paro requires **40 mm** diameter rope (not 57 mm)
- 45 mm rope has breaking load of **1,093 kN** (not 650 kN)
- Changed "substantially exceeding the comfortable grip capability" to "approaching but not exceeding the comfortable grip capability"

**Corrected Caption**:
> Tensile strength scaling and required rope diameters for moai transport. (A) Breaking load increases quadratically with rope diameter for Triumfetta cordifolia rope (fiber strength of 916 MPa, 75% construction efficiency). The working load requirements for 4-ton and 80-ton moai are indicated, along with a safety margin assuming a factor of 8. Specific values marked for 10 mm (32 kN) and **45 mm (1,093 kN)** rope diameters. (B) Required rope diameter as a function of moai mass, assuming a safety factor of 10. The 50 mm practical handling limit is exceeded for moai weighing approximately 60 tons or more. **Paro (86 tons) requires a 40 mm-diameter rope** under these assumptions, **approaching but not exceeding the comfortable grip capability**.

---

### 2. Figure 4 (figure4.py)
**File**: `/Users/clipo/PycharmProjects/rope/src/python/figure4.py`

**Error**: Line 63-64 showed vertical line at 57 mm for Paro

**Fix** (lines 63-64):
```python
# BEFORE:
ax.axvline(x=57, color='darkred', linestyle=':', linewidth=2,
           label='57 mm (Paro, 86 tons)')

# AFTER:
ax.axvline(x=40, color='darkred', linestyle=':', linewidth=2,
           label='40 mm (Paro, 86 tons)')
```

---

### 3. Figure 5 (figure5.py)
**File**: `/Users/clipo/PycharmProjects/rope/src/python/figure5.py`

**Error**: Lines 94-98 annotation claimed "Paro approaches practical handling limits" - misleading since Paro (40 mm) is still 10 mm below the 50 mm limit

**Fix** (lines 94-98):
```python
# BEFORE:
ax1.annotate('Paro approaches\npractical\nhandling limits',
             xy=(3, paro_diameter), xytext=(2.5, 55),
             arrowprops=dict(arrowstyle='->', color='orange', lw=1.5),
             fontsize=9, color='darkorange', weight='bold',
             bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.3))

# AFTER:
ax1.annotate('Paro (40 mm)\nstill within\npractical limits',
             xy=(3, paro_diameter), xytext=(2.5, 30),
             arrowprops=dict(arrowstyle='->', color='green', lw=1.5),
             fontsize=9, color='darkgreen', weight='bold',
             bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.3))
```

---

### 4. Figure 6 (figure6.py) - TOP PANEL
**File**: `/Users/clipo/PycharmProjects/rope/src/python/figure6.py`

**Error**: Lines 109-111 annotation pointed to wrong coordinates (3, 57) and claimed "Approached physical limits" - completely incorrect

**Fix** (lines 109-111):
```python
# BEFORE:
ax_top.annotate('Approached\nphysical limits', xy=(3, 57), xytext=(3.5, 80),
                arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
                fontsize=8, ha='center', color='red', fontweight='bold')

# AFTER:
ax_top.annotate('Largest transported\n(still within limits)', xy=(3, 41), xytext=(3.5, 55),
                arrowprops=dict(arrowstyle='->', color='orange', lw=1.5),
                fontsize=8, ha='center', color='darkorange', fontweight='bold')
```

**Issues Fixed**:
1. Y-coordinate corrected from 57 mm to 41 mm (actual value for Ahu Tongariki)
2. Text changed from "Approached physical limits" (FALSE) to "Largest transported (still within limits)" (TRUE)
3. Arrow color changed from red to orange to reflect less severe constraint

---

### 5. Figure 6 (figure6.py) - BOTTOM PANEL
**File**: `/Users/clipo/PycharmProjects/rope/src/python/figure6.py`

**Error**: Lines 175-177 zone label said "DIFFICULT (maximum effort)" for 40-50mm range, which is misleading since Paro and Ahu Tongariki (both in this range) were successfully transported

**Fix** (lines 175-177):
```python
# BEFORE:
ax_bottom.text(150, 45, 'DIFFICULT\n(maximum effort)',
               ha='center', fontsize=9, fontweight='bold', color='darkorange',
               bbox=dict(boxstyle='round', facecolor='orange', alpha=0.2))

# AFTER:
ax_bottom.text(150, 45, 'CHALLENGING\n(approaching limits)',
               ha='center', fontsize=9, fontweight='bold', color='darkorange',
               bbox=dict(boxstyle='round', facecolor='orange', alpha=0.2))
```

---

## Implications for Analysis

### Previous (Incorrect) Interpretation:
- Paro and Ahu Tongariki **exceeded or approached** the practical limits of rope technology
- This suggested rope technology was a major constraint for large moai transport
- Implied that only the largest moai (Te Tokanga) were truly impossible to move

### Corrected Interpretation:
- Paro (86 tons) and Ahu Tongariki (90 tons) **remained comfortably within** practical rope handling limits (40-41 mm vs 50 mm limit)
- Both were successfully transported historically, **as expected** from the rope analysis
- **Only Te Tokanga** (260 tons, requiring 69.4 mm diameter) actually exceeds practical limits
- The rope technology constraint becomes significant only for moai **exceeding ~60 tons** (where diameter approaches 50 mm)

### What This Means:
The rope diameter requirements do NOT explain why moai transport stopped at ~90 tons. Other factors (logistics, workforce, terrain, etc.) must have been the limiting constraints, not rope technology itself.

---

## Calculation Verification

All calculations use the formula:
```
d = 2 × √(Breaking_load / (σ × π × η))
```

Where:
- σ = 916 MPa (tensile strength of Triumfetta cordifolia)
- η = 0.75 (rope construction efficiency)
- Breaking_load = Mass (tons) × 1 kN/ton × Safety_Factor

For Paro (86 tons, SF=10):
```
Working_load = 86 tons × 1 kN/ton = 86 kN
Required_breaking_load = 86 kN × 10 = 860 kN
d = 2 × √(860,000 N / (916 MPa × π × 0.75))
d = 2 × √(860,000 / 2,156.67)
d = 2 × √398.88
d = 2 × 19.97
d = 39.94 mm ≈ 40 mm
```

✓ Verified correct

---

## Files Modified

1. ✓ `figure3.py` - calculations were already correct
2. ✓ `figure4.py` - line 63-64 (Paro vertical line: 57→40 mm)
3. ✓ `figure5.py` - lines 94-98 (annotation text and positioning)
4. ✓ `figure6.py` - lines 109-111 (annotation coordinates and text)
5. ✓ `figure6.py` - lines 175-177 (zone label text)

## Files Requiring Manual Update

- **Manuscript caption for Figure 3** - needs correction from 57 mm to 40 mm (and 650 kN to 1,093 kN)

---

## Regenerated Figures

All corrected figures have been regenerated:
- ✓ `figures/figure3_tensile_strength_scaling.png` and `.pdf`
- ✓ `figures/figure4_grip_limits.png` and `.pdf`
- ✓ `figures/figure5_transport_scenarios.png` and `.pdf`
- ✓ `figures/figure6_moai_progression.png` and `.pdf`

The corrected figures now accurately represent the rope diameter requirements and do not overstate the constraints for Paro and Ahu Tongariki.
