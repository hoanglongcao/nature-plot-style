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

# FIGURE 1: Nature-branded colors
# Creating a plot using Nature-branded colors
plt.figure(figsize=(width_in_inches, height_in_inches))
plt.plot(x, y1, label='sin(x)', color=nps.nature_colors['Blue'][3])
plt.plot(x, y2, label='cos(x)', color=nps.nature_colors['Red'][3])
plt.plot(x, y3, label='log(x+1)', color=nps.nature_colors['Green'][3])
plt.plot(x, y4, label='x^0.5', color=nps.nature_colors['Purple'][3])
# Adding title and labels
plt.title('Nature')
plt.xlabel('X axis')
plt.ylabel('Y axis')
# EXPORT
# Save to PDF
plt.savefig('test.pdf', bbox_inches='tight', pad_inches=0.05)


# FIGURE 2: Batlow colors
# Generating a color palette from the 'batlow' colormap
n_colors = 4  # Number of colors in the palette
colors = [cmc.batlow(i/n_colors) for i in range(n_colors)]

# Creating a plot using batlow colors
plt.figure(figsize=(width_in_inches, height_in_inches))
plt.plot(x, y1, label='sin(x)', color=colors[0])
plt.plot(x, y2, label='cos(x)', color=colors[1])
plt.plot(x, y3, label='log(x+1)', color=colors[2])
plt.plot(x, y4, label='x^0.5', color=colors[3])
# Adding title and labels
plt.title('Batlow')
plt.xlabel('X axis')
plt.ylabel('Y axis')

#FIGURE 3: The Economist-branded colors
# Source: https://design-system.economist.com/foundations/colour/palettes
# Color palletes
economist_colors = {
    'Brand': {
        'Economist Red': '#E3120B',
        'Economist Red 60': '#F6423C'
    },
    'Accent': {
        'Primary': {
            'Chicago 20': '#141F52',
            'Chicago 30': '#1F2E7A',
            'Chicago 45': '#2E45B8',
            'Chicago 55': '#475ED1',
            'Chicago 90': '#D6DBF5',
            'Chicago 95': '#EBEDFA'
        },
        'Secondary': {
            'Hong Kong 45': '#1DC9A4',
            'Hong Kong 55': '#36E2BD',
            'Hong Kong 90': '#D2F9F0',
            'Hong Kong 95': '#E9FCF8',
            'Tokyo 45': '#C91D42',
            'Tokyo 55': '#E2365B',
            'Tokyo 90': '#F9D2DB',
            'Tokyo 95': '#FCE9ED'
        },
        'Tertiary': {
            'Singapore 55': '#F97A1F',
            'Singapore 65': '#FB9851',
            'Singapore 75': '#FCB583',
            'Singapore 90': '#FEE1CD',
            'New York 55': '#F9C31F',
            'New York 65': '#FBD051',
            'New York 75': '#FCDE83',
            'New York 90': '#FEF2CD'
        }
    },
    'Greyscale': {
        'London 5': '#0D0D0D',
        'London 10': '#1A1A1A',
        'London 20': '#333333',
        'London 35': '#595959',
        'London 70': '#B3B3B3',
        'London 85': '#D9D9D9',
        'London 95': '#F2F2F2',
        'London 100': '#FFFFFF'
    },
    'Canvas': {
        'Los Angeles 85': '#E1DFD0',
        'Los Angeles 90': '#EBE9E0',
        'Los Angeles 95': '#F5F4EF',
        'Paris 85': '#D0E1E1',
        'Paris 90': '#E0EBEB',
        'Paris 95': '#EFF5F5'
    }
}

# Creating a plot using batlow colors
plt.figure(figsize=(width_in_inches, height_in_inches))
plt.plot(x, y1, label='sin(x)', color=economist_colors['Accent']['Primary']['Chicago 30'])
plt.plot(x, y2, label='cos(x)', color=economist_colors['Accent']['Secondary']['Hong Kong 55'])
plt.plot(x, y3, label='log(x+1)', color=economist_colors['Accent']['Secondary']['Tokyo 55'])
plt.plot(x, y4, label='x^0.5', color=economist_colors['Accent']['Tertiary']['Singapore 65'])
# Adding title and labels
plt.title('The Economist')
plt.xlabel('X axis')
plt.ylabel('Y axis')

# Display the plot
plt.show()