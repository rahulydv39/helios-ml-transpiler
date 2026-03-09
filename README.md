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
