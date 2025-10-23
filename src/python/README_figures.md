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

### figure2.py - Tensile Strength Scaling
Generates a two-panel figure showing:
- Left panel: Rope breaking load vs diameter for Triumfetta cordifolia
- Right panel: Required rope diameter vs moai mass

**Output:** `figure2_tensile_strength_scaling.png`

### figure3.py - Hand Grip Capability
Shows the relationship between human hand grip capability and required rope diameters for moai of various sizes.

**Output:** `figure3_grip_limits.png`

### figure4.py - Transport Scenarios
Multi-axis bar chart comparing rope diameter, moai mass, and workforce requirements across different moai categories (quarry, road, platform, Paro).

**Output:** `figure4_transport_scenarios.png`

### figure5.py - Moai Progression
Comprehensive two-panel figure showing:
- Top panel: Bar chart of specific named moai specimens with rope requirements
- Bottom panel: Continuous relationship between moai mass and rope diameter

Demonstrates where rope technology reaches physical impossibility limits.

**Output:** `figure5_moai_progression.png`

## Usage

Run any script independently:
```bash
python3 figure2.py
python3 figure3.py
python3 figure4.py
python3 figure5.py
```

Each script will:
1. Generate the figure
2. Save it as a PNG file (300 DPI)
3. Display it on screen (if running interactively)
4. Print confirmation and data summary

## Customization

All scripts use publication-quality parameters set at the beginning:
- Font: Serif
- DPI: 300
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
- **Paro:** 82 tons
- **Ahu Tongariki (largest transported):** 86 tons
- **Te Tokanga (quarry, never moved):** 260 tons

## Notes

- All calculations assume optimal fiber processing (3-week water retting)
- Rope diameter calculations use the formula: d = 2 × √(Breaking_load / (σ × π × η))
  where σ = tensile strength, η = construction efficiency
- The scripts demonstrate that Te Tokanga (260 tons) would require rope diameter of 69 mm with standard safety factors, far exceeding human grip capability (~50 mm maximum)
