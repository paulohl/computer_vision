import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.lines import Line2D

# Helper function to draw a rounded rectangle with text
def draw_box(ax, xy, width, height, text, fontsize=9):
    box = FancyBboxPatch(xy, width, height,
                         boxstyle="round,pad=0.02,rounding_size=0.02",
                         fc="#a8dadc", ec="#457b9d", lw=1.2)
    ax.add_patch(box)
    ax.text(xy[0]+width/2, xy[1]+height/2, text, ha='center', va='center',
            fontsize=fontsize, wrap=True)

# Set up figure
fig, ax = plt.subplots(figsize=(14,7))
ax.set_xlim(0, 14)
ax.set_ylim(0, 7)
ax.axis('off')

# Coordinates and sizes
w, h = 2.0, 0.8
y_level = 4

# Blocks
draw_box(ax, (1, y_level), w, h, "Input Text\nSequence")
draw_box(ax, (4, y_level), w, h, "Positional Encoding\n& Embeddings")
draw_box(ax, (7, y_level+0.8), w, h*1.5, "Self-Attention Layer\n(Query, Key, Value → Output)")
draw_box(ax, (10, y_level), w, h, "Feed Forward\nNetwork (FFN)")
draw_box(ax, (12.5, y_level), w, h, "Softmax\nPrediction")
draw_box(ax, (12.5, y_level-2), w, h, "Output\nSequence")
draw_box(ax, (1, y_level-2), w, h, "New Input\nSequence")

# Arrows forward flow
arrow_args = dict(arrowstyle="->", color='black', lw=1.2)
ax.annotate("", xy=(3, y_level+0.4), xytext=(3.95, y_level+0.4), arrowprops=arrow_args)
ax.annotate("", xy=(6, y_level+0.4), xytext=(6.95, y_level+0.8), arrowprops=arrow_args)
ax.annotate("", xy=(9, y_level+0.4), xytext=(9.95, y_level+0.4), arrowprops=arrow_args)
ax.annotate("", xy=(11.9, y_level+0.4), xytext=(12.45, y_level+0.4), arrowprops=arrow_args)
ax.annotate("", xy=(13.5, y_level), xytext=(13.5, y_level-1.6), arrowprops=arrow_args)
ax.annotate("", xy=(2, y_level-1.6), xytext=(2, y_level-0.2), 
            arrowprops=dict(arrowstyle="->", lw=1.2, linestyle="dotted"))

# Labels
ax.text(7.5, y_level+2.6, "Output from Layer N goes to Layer N+1", ha='center', fontsize=10, color='#1d3557')
ax.text(7, y_level-3.2, "Autoregressive Loop: Previous outputs feed into next prediction", 
        ha='center', fontsize=10, color='#1d3557')

# Save as PNG and SVG
png_path = "/mnt/data/gpt_autoregressive_flow.png"
svg_path = "/mnt/data/gpt_autoregressive_flow.svg"
plt.tight_layout()
fig.savefig(png_path, dpi=400, bbox_inches='tight')
fig.savefig(svg_path, format='svg', bbox_inches='tight')

png_path, svg_path

