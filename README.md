# Rapa Nui Moai Rope Production and Feasibility Analysis

This repository contains the analysis and figures for a research paper examining the mechanical properties of Triumfetta fiber ropes and their feasibility for transporting Rapa Nui moai statues using the experimental walking method.

## Project Overview

This study analyzes:
- Mechanical properties of Triumfetta species (hau hau) fiber
- Rope strength requirements for moai transport
- Production investment and labor costs
- Physical and organizational constraints on moai transport

## Repository Structure

```
.
├── figures/                    # Generated figures (600 dpi PNG and PDF)
│   ├── figure8_*.png/pdf      # Tensile strength scaling
│   ├── figure9_*.png/pdf      # Hand grip limits
│   ├── figure10_*.png/pdf     # Transport scenarios
│   ├── figure11_*.png/pdf     # Moai progression
│   ├── figure12_*.png/pdf     # Rope production investment
│   └── figure13_*.png/pdf     # Comparative labor investment
├── src/
│   └── python/                # Figure generation scripts
│       ├── figure8.py
│       ├── figure9.py
│       ├── figure10.py
│       ├── figure11.py
│       ├── figure12.py
│       └── figure13.py
├── rope_production_section.md  # Draft section on production feasibility
├── moai_rope.docx             # Main paper draft
└── README.md                  # This file
```

## Figures

All figures are generated at 600 dpi in both PNG and PDF formats.

### Figure 8: Tensile Strength Scaling
Two-panel figure showing rope breaking load vs diameter and required rope diameter vs moai mass.

### Figure 9: Human Hand Grip Capability
Comparison of human hand grip limits versus required rope diameters for different moai sizes.

### Figure 10: Transport Scenarios
Multi-axis comparison of rope diameter, moai mass, and workforce requirements across transport scenarios.

### Figure 11: Moai Progression Analysis
Two-panel figure showing rope requirements for specific moai specimens and continuous relationships across sizes.

### Figure 12: Rope Production Investment
Four-panel analysis showing:
- Fiber mass requirements
- Production timeline breakdown
- Person-days of labor by stage
- Cumulative investment vs transport distance

### Figure 13: Comparative Time and Labor Investment
Visual comparison of rope production requirements across moai categories, emphasizing the practical feasibility of rope production even for the largest transported specimens.

## Key Findings

- 10 mm diameter Triumfetta rope provides breaking loads of 32-36 kN (safety factors 8-12 for 4-ton moai)
- Largest transported moai (Paro, 86 tons) requires ~40 mm diameter rope, approaching the ~50 mm human grip limit
- Rope production for Paro's 6 km transport: ~871 person-days (1.2 days of community labor capacity)
- Moai transport limits reflect organizational/physiological constraints, not material scarcity

## Running the Scripts

To regenerate figures:

```bash
python src/python/figure8.py
python src/python/figure9.py
python src/python/figure10.py
python src/python/figure11.py
python src/python/figure12.py
python src/python/figure13.py
```

Figures will be saved to the `figures/` directory.

## Requirements

- Python 3.x
- matplotlib
- numpy

## References

- Folk, C.L. (2018). Moving Monoliths, Easter Island and Environmental Collapse. *EXARC Journal* 2018(3).
- Hunt, T.L. and Lipo, C.P. (2011). The Statues that Walked.
- Lipo, C.P. and Hunt, T.L. (2025). Archaeological evidence for moai transport patterns on Rapa Nui.

## Authors

[Author information to be added]

## License

[License information to be added]
