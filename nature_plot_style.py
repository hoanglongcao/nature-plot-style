import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Configuration settings for Matplotlib plots
# STYLES: FROM NATURE JOURNAL
def set_nature_style():
    plt.rcParams.update({
        'pdf.fonttype': 42,
        'font.family': 'Arial',
        'font.size': 8,
        'axes.titlesize': 8,
        'axes.labelsize': 8,
        'xtick.labelsize': 7,
        'ytick.labelsize': 7,
        'legend.fontsize': 8,
        'axes.linewidth': 1,
        'xtick.major.width': 1,
        'ytick.major.width': 1,
        'xtick.minor.width': 1,
        'ytick.minor.width': 1,
        'axes.spines.top': False,
        'axes.spines.right': False,
        'figure.autolayout': True
    })

# Color palettes
# Source: https://www.nature.com/documents/natrev-artworkguide.pdf
nature_color_palettes = {
    'main_background': {
        'Stone': ['#f7f5efff', '#e4e0ceff', '#c6c2a6ff', '#a8a386ff', '#888366ff','#625f4aff'],
        'Grey': ['#e6e6edff', '#c8cedaff', '#99a3b4ff', '#6f7b91ff', '#49566dff','#253247ff']
    },
    'main_accents': {
        'Red': ['#fad0ceff', '#eda4a7ff', '#de6866ff', '#c93e3fff', '#9c2826ff', '#741915ff'],
        'Blue': ['#c8e7fbff', '#9dcbecff', '#5799d1ff', '#0272b2ff', '#014e91ff', '#012c5cff'],
        'Yellow': ['#fff1c3ff', '#f6dc8aff', '#ebc850ff', '#cca02cff', '#9c7717ff', '#6b5513ff']
    },
    'extended_palette': {
        'Olive': ['#f4f1b3ff', '#dfdc67ff', '#c9c700ff', '#9ba415ff', '#66771eff', '#36461aff'],
        'Green': ['#d9e8c6ff', '#a0ca79ff', '#62b347ff', '#459434ff', '#227130ff', '#163b1cff'],
        'Teal': ['#cce7eeff', '#97d2d4ff', '#4bbcbdff', '#019aa3ff', '#016879ff', '#00394eff'],
        'Blue': ['#c8e7fbff', '#9dcbecff', '#5799d1ff', '#0272b2ff', '#014e91ff', '#012c5cff'],
        'Purple': ['#ebd6e9ff', '#d3aad1ff', '#bb7cb4ff', '#a84e94ff', '#792c74ff', '#481951ff'],
        'Red': ['#fad0ceff', '#eda4a7ff', '#de6866ff', '#c93e3fff', '#9c2826ff', '#741915ff'],
        'Orange': ['#fde0bdff', '#fbc07fff', '#f59a45ff', '#ec6f00ff', '#b74f06ff', '#843200ff'],
        'Yellow': ['#fff1c3ff', '#f6dc8aff', '#ebc850ff', '#cca02cff', '#9c7717ff', '#6b5513ff'],
        'Skin tones': ['#f8e6d7ff', '#ddbda3ff', '#bf997dff', '#936a57ff', '#755040ff', '#442d1fff']

    }
}

# Create a new dictionary that combines colors under each color name
nature_colors = {}
for category in nature_color_palettes.values():
    for color_name, colors in category.items():
        if color_name not in nature_colors:
            nature_colors[color_name] = colors

def plot_palette(ax, palettes, title):
    num_palettes = len(palettes)
    for i, (name, colors) in enumerate(palettes.items()):
        for j, color in enumerate(colors):
            ax.add_patch(plt.Rectangle((j, num_palettes - i - 1), 1, 1, color=color, edgecolor='none'))
        ax.text(-0.5, num_palettes - i - 0.5, name, va='center', ha='right', fontsize=8)
    ax.set_xlim(-1, len(next(iter(palettes.values()))))
    ax.set_ylim(0, num_palettes)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(title, loc='center', fontsize=8, fontweight='bold')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

# Function to plot color palettes
def plot_color_palettes():
    set_nature_style()
    # Set width to inches for figure size
    figwidth = 90  # mm
    ratio = 4/3
    width_in_inches = figwidth / 25.4
    height_in_inches = width_in_inches / ratio  # Maintain an aspect ratio

    fig = plt.figure(figsize=(width_in_inches, height_in_inches))  # Adjust the figure size as needed
    gs = gridspec.GridSpec(2, 2, width_ratios=[1, 1], height_ratios=[1, 1])

    axes = [
        fig.add_subplot(gs[0, 0]),
        fig.add_subplot(gs[1, 0]),
        fig.add_subplot(gs[:, 1])
    ]
    titles = ['Main Background', 'Main Accents', 'Extended Palette']
    palettes = ['main_background', 'main_accents', 'extended_palette']

    for ax, palette, title in zip(axes, palettes, titles):
        plot_palette(ax, nature_color_palettes[palette], title)
    plt.show(block=False)



