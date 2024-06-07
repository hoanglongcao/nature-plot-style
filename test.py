import matplotlib.pyplot as plt
import numpy as np
import nature_plot_style as nps
import cmcrameri.cm as cmc

# Apply Nature Journal style settings
nps.set_nature_style()

# Visualize the Nature-branded color palettes
nps.plot_color_palettes()

# Set width to inches for figure size
figwidth= 90 # 90mm or 180mm
ratio = 16/9
width_in_inches = figwidth / 25.4
height_in_inches = width_in_inches /ratio  # Maintain a aspect ratio
# To be used when create a plot: figsize=(width_in_inches, height_in_inches)

# Create a simple plot using 4 colors
# Sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.log(x + 1)
y4 = x ** 0.5

# Creating a plot using Nature-branded colors
plt.figure(figsize=(width_in_inches, height_in_inches))
plt.plot(x, y1, label='sin(x)', color=nps.nature_colors['Blue'][3])
plt.plot(x, y2, label='cos(x)', color=nps.nature_colors['Red'][3])
plt.plot(x, y3, label='log(x+1)', color=nps.nature_colors['Green'][3])
plt.plot(x, y4, label='x^0.5', color=nps.nature_colors['Purple'][3])
plt.title('Nature')
# EXPORT
# Save to PDF
plt.savefig('test.pdf', bbox_inches='tight', pad_inches=0.05)


# Generating a color palette from the 'batlow' colormap
n_colors = 4  # Number of colors in the palette
colors = [cmc.batlow(i/n_colors) for i in range(n_colors)]

# Creating a plot using batlow colors
plt.figure(figsize=(width_in_inches, height_in_inches))
plt.plot(x, y1, label='sin(x)', color=colors[0])
plt.plot(x, y2, label='cos(x)', color=colors[1])
plt.plot(x, y3, label='log(x+1)', color=colors[2])
plt.plot(x, y4, label='x^0.5', color=colors[3])
plt.title('Batlow')

# Adding title and labels
plt.xlabel('X axis')
plt.ylabel('Y axis')

# Tight layout
plt.tight_layout()

# Display the plot
plt.show()