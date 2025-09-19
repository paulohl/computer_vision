import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patheffects import withStroke

# Helper to draw a labeled box
def draw_box(ax, text, xy, width=2.5, height=0.6, fontsize=10, bold=False):
    x, y = xy
    style = "round,pad=0.02"
    color = '#ccffe5'  # mint green
    weight = 'bold' if bold else 'normal'
    box = mpatches.FancyBboxPatch((x - width/2, y - height/2), width, height,
                                  boxstyle=style, linewidth=1, edgecolor='green',
                                  facecolor=color)
    ax.add_patch(box)
    ax.text(x, y, text, fontsize=fontsize, ha='center', va='center', weight=weight,
            path_effects=[withStroke(linewidth=0.5, foreground="black")])

# Helper to draw arrows
def draw_arrow(ax, start, end):
    ax.annotate('', xy=end, xytext=start, arrowprops=dict(arrowstyle="->", color='black'))

# Layout the improved vertical GPT architecture
fig, ax = plt.subplots(figsize=(6, 14))
ax.set_xlim(0, 10)
ax.set_ylim(0, 35)
ax.axis('off')

y = 34
dy = 2.3

# Box definitions (label, is_bold)
boxes = [
    ("Input Text Sequence", False),
    ("Calculate position-encoded embeddings", False),
    ("Word 1 Embedding", False),
    ("Word 2 Embedding", False),
    ("Word N Embedding", False),
    ("Self-Attention Layer", True),
    ("Query, Key, Value for Word 1", False),
    ("Query, Key, Value for Word 2", False),
    ("Query, Key, Value for Word N", False),
    ("Self-Attention Output for Words", False),
    ("Feed Forward Network (FFN)", False),
    ("Softmax: Predict Next Word", False),
    ("Word N+1", False),
    ("Add to Input Sequence", False),
    ("New Input Sequence", False)
]

positions = []

# Draw each box
for label, bold in boxes:
    draw_box(ax, label, (5, y), fontsize=10, bold=bold)
    positions.append((5, y))
    y -= dy

# Draw arrows between boxes
for i in range(len(positions) - 1):
    draw_arrow(ax, positions[i], positions[i + 1])

# Save output
output_path = "/mnt/data/Figure_3_4_GPT_Architecture_Vertical_Optimized_v2.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()

output_path
