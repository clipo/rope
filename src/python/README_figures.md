# Figure Generation Scripts for Triumfetta Rope Analysis

This directory contains standalone Python scripts to regenerate the figures for the paper "Triumfetta Fiber Rope Performance and Application to Easter Island Moai Transport."

## Requirements

- Python 3.x
- matplotlib
- numpy

Install dependencies:
```bash
pip install matplotlib numpy
```

## Available Scripts

### figure8.py - Tensile Strength Scaling
Generates a two-panel figure showing:
- Left panel: Rope breaking load vs diameter for Triumfetta cordifolia
- Right panel: Required rope diameter vs moai mass

**Output:** `figure8_tensile_strength_scaling.png` and `.pdf`

### figure9.py - Hand Grip Capability
Shows the relationship between human hand grip capability and required rope diameters for moai of various sizes.

**Output:** `figure9_grip_limits.png` and `.pdf`

### figure10.py - Transport Scenarios
Multi-axis bar chart comparing rope diameter, moai mass, and workforce requirements across different moai categories (quarry, road, platform, Paro).

**Output:** `figure10_transport_scenarios.png` and `.pdf`

### figure11.py - Moai Progression
Comprehensive two-panel figure showing:
- Top panel: Bar chart of specific named moai specimens with rope requirements
- Bottom panel: Continuous relationship between moai mass and rope diameter

Demonstrates where rope technology reaches physical impossibility limits.

**Output:** `figure11_moai_progression.png` and `.pdf`

### figure12.py - Rope Production Investment
Four-panel analysis showing:
- Panel A: Fiber mass required vs moai mass
- Panel B: Production timeline (harvesting, retting, construction)
- Panel C: Person-days of labor vs moai mass
- Panel D: Cumulative investment vs transport distance

Based on experimental data from Folk (2018) and traditional fiber processing techniques.

**Output:** `figure12_rope_production_investment.png` and `.pdf`

### figure13.py - Comparative Time and Labor Investment
Visual comparison showing how rope production requirements scale with moai size, emphasizing the practical feasibility of rope production even for the largest transported specimens.

**Output:** `figure13_rope_investment_comparison.png` and `.pdf`

## Usage

Run any script independently:
```bash
python3 figure8.py
python3 figure9.py
python3 figure10.py
python3 figure11.py
python3 figure12.py
python3 figure13.py
```

Each script will:
1. Generate the figure
2. Save it as both PNG and PDF files (600 DPI)
3. Display it on screen (if running interactively)
4. Print confirmation and data summary

## Customization

All scripts use publication-quality parameters set at the beginning:
- Font: Serif
- DPI: 600
- Figure sizes optimized for academic papers

You can modify these parameters or any calculations by editing the scripts directly. Key parameters are clearly commented in each file.

## Key Parameters Used

- **Tensile strength:** 916 MPa (T. cordifolia)
- **Construction efficiency:** 0.75 (75%)
- **Safety factors:** 10 (standard) and 5 (reduced)
- **Working load estimate:** 1 kN per ton of moai mass
- **Grip limits:** 40 mm (comfortable), 50 mm (maximum), 70 mm (impossible)

## Moai Specimens Analyzed

- **Experimental replica:** 4.3 tons
- **Ahu Akivi (typical platform moai):** 18 tons
- **Large platform moai:** 40 tons
- **Very large moai:** 60 tons
- **Paro:** 86 tons
- **Ahu Tongariki (largest transported):** 90 tons
- **Te Tokanga (quarry, never moved):** 260 tons

## Notes

- All calculations assume optimal fiber processing (3-week water retting)
- Rope diameter calculations use the formula: d = 2 × √(Breaking_load / (σ × π × η))
  where σ = tensile strength, η = construction efficiency
- The scripts demonstrate that Te Tokanga (260 tons) would require rope diameter of 69 mm with standard safety factors, far exceeding human grip capability (~50 mm maximum)
