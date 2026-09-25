from music21 import stream, note, chord, tempo
import random

# Create a new music piece
music = stream.Stream()

# Set tempo
music.append(tempo.MetronomeMark(number=100))

# Notes used by the AI-style generator
notes = ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5"]

# Generate a melody
for i in range(32):
    if random.random() < 0.15:
        # Add a simple chord
        chord_notes = random.sample(notes, 3)
        c = chord.Chord(chord_notes)
        c.quarterLength = 1
        music.append(c)
    else:
        # Add a melody note
        n = note.Note(random.choice(notes))
        n.quarterLength = 1
        music.append(n)

# Save the generated music
music.write("midi", fp="generated_music.mid")

print("AI music generated successfully!")
print("Saved as: generated_music.mid")