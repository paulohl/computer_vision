import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create the figure and axis
fig, ax = plt.subplots(figsize=(6, 10))
ax.axis('off')

# Define blocks as (label, y-position)
blocks = [
    ("User Input (Token Sequence)", 9.5),
    ("Token Embedding", 9.0),
    ("Positional Encoding", 8.4),
    ("Transformer Decoder Stack (×N)", 7.6),
    ("LayerNorm", 6.8),
    ("Multi-Head Attention", 6.2),
    ("Add & Norm (Residual)", 5.5),
    ("Feedforward Network", 4.8),
    ("Add & Norm (Residual)", 4.1),
    ("⋮ (Repeated for N Layers)", 3.3),
    ("Final Linear + Softmax", 2.6),
    ("Output Probabilities", 1.9),
    ("Next Predicted Token", 1.2)
]

# Colors
fill_color = "#E0F2F1"  # Light teal
edge_color = "#00796B"  # Deep teal

# Draw blocks
for label, y in blocks:
    rect = patches.FancyBboxPatch((1.5, y), 6, 0.5,
                                  boxstyle="round,pad=0.02",
                                  edgecolor=edge_color, facecolor=fill_color, linewidth=1.5)
    ax.add_patch(rect)
    ax.text(4.5, y + 0.25, label, ha='center', va='center', fontsize=9)

# Draw arrows between blocks
for i in range(len(blocks) - 1):
    y1 = blocks[i][1]
    y2 = blocks[i + 1][1]
    ax.annotate("", xy=(4.5, y2 + 0.5), xytext=(4.5, y1),
                arrowprops=dict(arrowstyle="->", lw=1.2, color='black'))

plt.tight_layout()
plt.show()
