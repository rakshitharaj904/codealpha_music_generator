# AI Music Generator

A Python-based AI Music Generator developed as part of the CodeAlpha AI Internship – Task 3.

## Project Overview

This project generates a new musical melody programmatically using Python and the music21 library.

A structured note pattern is used to create a new melody, which is saved as a MIDI file.

## Features

- Generates a musical melody
- Uses structured musical patterns
- Creates MIDI output
- Automatically saves generated music
- Simple Python implementation

## Technologies Used

- Python
- music21
- NumPy

## How It Works

1. The program defines a set of musical notes.
2. NumPy is used to create a note pattern.
3. The pattern is repeated to generate a melody.
4. music21 converts the notes into a musical stream.
5. The generated music is saved as a MIDI file.

## How to Run

Install the required libraries:

```bash
pip install music21 numpy