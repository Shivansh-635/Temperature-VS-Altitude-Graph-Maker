# Temperature vs Altitude Graph using International Standard Atmosphere (ISA) Model

## 1. Introduction

This project implements a Python-based model to calculate and visualize the variation of atmospheric temperature with altitude using a simplified version of the International Standard Atmosphere (ISA). The program is designed to help understand how temperature changes across different atmospheric layers and to provide a graphical representation of these variations.

The model is particularly useful for students and professionals in aerospace engineering, atmospheric science, and physics, where understanding temperature gradients is essential for flight dynamics, propulsion, and environmental analysis.

---

## 2. Objectives

The primary objectives of this project are:

- To compute atmospheric temperature at a given altitude using piecewise-defined equations
- To visualize the temperature distribution across different atmospheric layers
- To highlight and annotate the temperature corresponding to a user-defined altitude
- To provide a simple and interactive educational tool for understanding ISA temperature profiles

---

## 3. Features

- Accepts user input for altitude (in kilometers)
- Computes temperature based on ISA-defined atmospheric layers
- Plots a Temperature vs Altitude graph using matplotlib
- Displays key atmospheric boundary points
- Highlights the user input point on the graph
- Annotates both predefined points and user-specific values for clarity

---

## 4. Requirements

### Software Requirements

- Python 3.x
- Matplotlib library

### Installation

Install the required library using pip:

```bash
pip install matplotlib
