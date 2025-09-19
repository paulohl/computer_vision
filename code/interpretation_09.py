import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, ArrowStyle, FancyArrowPatch

# Setup
fig, ax = plt.subplots(figsize=(10, 14))
ax.set_xlim(0, 10)
ax.set_ylim(0, 20)
ax.axis('off')

# Utility function to add a box
def add_box(text, xy, width=2.4, height=0.8, fontsize=10, bold=False):
    x, y = xy
    box = FancyBboxPatch((x - width/2, y - height/2), width, height,
                         boxstyle="round,pad=0.02", fc="honeydew", ec="darkgreen")
    ax.add_patch(box)
    fontweight = 'bold' if bold else 'normal'
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize, fontweight=fontweight)

# Utility to draw arrow between boxes
def draw_arrow(start, end):
    arrow = FancyArrowPatch(start, end, arrowstyle=ArrowStyle("->", head_length=4, head_width=2),
                            color='black', linewidth=1.2)
    ax.add_patch(arrow)

# Add components of GPT architecture
layers = [
    ("Input Text Sequence", 17),
    ("Token + Positional Embeddings", 15.5),
    ("Transformer Block (repeated N times)", 14, True),
    ("Self-Attention", 12.5),
    ("Add & Norm", 11.2),
    ("Feedforward (FFN)", 10),
    ("Add & Norm", 8.8),
    ("Final Linear Layer", 7.3),
    ("Softmax", 6.1),
    ("Predicted Token", 4.8),
]

# Draw all boxes and arrows
prev_y = None
for text, y, *bold in layers:
    add_box(text, (5, y), bold=bold[0] if bold else False)
    if prev_y is not None:
        draw_arrow((5, prev_y - 0.4), (5, y + 0.4))
    prev_y = y

# Add caption at bottom
ax.text(5, 2, "Figure 3.4: GPT Model Architecture — Token flows through multiple stacked transformer blocks.",
        ha='center', fontsize=9, style='italic')

# Save image
output_path = "/mnt/data/Figure_3_4_GPT_Architecture_Clean.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()

output_path
