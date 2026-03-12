# Helios: Bare-Metal Physical AI Compiler

Helios is a lightweight, zero-dependency transpiler that converts Python-based neural networks into statically allocated, $O(1)$ memory `C` code for highly constrained edge devices. 

## The Problem
Standard frameworks like TensorFlow Lite are too bloated for extreme edge deployment. An Arduino Uno has 2KB of SRAM. Running even basic physical AI models (like kinematics or anomaly detection) using standard libraries often causes memory overflows or unpredictable latency.

## The Solution
Helios rips the weights and architecture out of standard Python models and generates raw, dependency-free `C` code. 
* **Zero Dynamic Allocation:** No `malloc` or `free`. Safe for embedded systems.
* **Flash Memory Optimized:** Weights are statically compiled into ROM using `const float` arrays, preserving active SRAM for execution.
* **Deterministic Execution:** Raw matrix math guarantees predictable latency for real-time robotics.

## Current Benchmark (2-DoF Kinematics Model)
* **Standard Python Model:** ~100 KB
* **Helios Generated C Model:** 1.38 KB (Fits entirely in an Arduino Uno's memory with room to spare)
# Helios ML Transpiler

Tiny neural network transpiler that converts a trained TensorFlow model into pure C code.

## Architecture

2 → 16 → 16 → 2 MLP

## Pipeline

TensorFlow → JSON weights → Python transpiler → C inference engine

## Run

Compile:

gcc model.c -o model -lm

Run:

./model
