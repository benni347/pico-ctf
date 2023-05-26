import re
import matplotlib.pyplot as plt
from PIL import Image

# G-code string
with open("gcode.txt", "r") as f:
    gcode = f.read()
    f.close()

# Split into lines and process each one
lines = gcode.split('\n')

# Lists to hold X and Y coordinates
X = []
Y = []

# Regular expression to match coordinates
coord_re = re.compile('([XYZ])([0-9.-]+)')

# Process each line
for line in lines:
    # Check if line starts with G0 or G1
    if line.startswith(('G0', 'G1')):
        x = None
        y = None
        # Extract coordinates
        for match in coord_re.finditer(line):
            if match.group(1) == 'X':
                x = float(match.group(2))
            elif match.group(1) == 'Y':
                y = float(match.group(2))
        # If both X and Y coordinates are present, add them to the lists
        if x is not None and y is not None:
            X.append(x)
            Y.append(y)

# Plot the path
plt.figure(figsize=(10,10))
plt.plot(X, Y, 'k-')
plt.axis('equal')
plt.gca().invert_yaxis()  # Invert Y axis, as CNC coordinates are typically oriented with positive Y upwards
plt.axis('off')  # Hide axes
plt.savefig('gcode.png', format='png', dpi=300)

# Convert to grayscale and save as PNG
img = Image.open('gcode.png').convert('L')
img.save('gcode.png')

