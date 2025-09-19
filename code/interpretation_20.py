# Adjust the figure to use smaller font and compress vertical spacing for full label visibility
fig, ax = plt.subplots(figsize=(6, 12))
ax.axis('off')

# Adjusted blocks with tighter spacing
blocks = [
    ("User Input (Token Sequence)", 11.8),
    ("Token Embedding", 11.0),
    ("Positional Encoding", 10.2),
    ("Transformer Decoder Stack (×N)", 9.4),
    ("LayerNorm", 8.6),
    ("Multi-Head Attention", 7.8),
    ("Add & Norm (Residual)", 7.0),
    ("Feedforward Network", 6.2),
    ("Add & Norm (Residual)", 5.4),
    ("⋮ (Repeated for N Layers)", 4.6),
    ("Final Linear + Softmax", 3.8),
    ("Output Probabilities", 3.0),
    ("Next Predicted Token", 2.2)
]

# Colors
fill_color = "#E0F2F1"  # Light teal
edge_color = "#00796B"  # Deep teal

# Draw blocks
for label, y in blocks:
    rect = patches.FancyBboxPatch((1.5, y), 6, 0.6,
                                  boxstyle="round,pad=0.02",
                                  edgecolor=edge_color, facecolor=fill_color, linewidth=1.5)
    ax.add_patch(rect)
    ax.text(4.5, y + 0.3, label, ha='center', va='center', fontsize=8.5)

# Draw arrows
for i in range(len(blocks) - 1):
    y1 = blocks[i][1]
    y2 = blocks[i + 1][1]
    ax.annotate("", xy=(4.5, y2 + 0.6), xytext=(4.5, y1),
                arrowprops=dict(arrowstyle="->", lw=1.2, color='black'))

plt.tight_layout()
plt.show()
