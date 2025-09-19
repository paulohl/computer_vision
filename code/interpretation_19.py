# Regenerate the vertical GPT architecture diagram in a landscape-oriented figure with improved scaling
fig, ax = plt.subplots(figsize=(10, 8))
ax.axis('off')

# Adjusted block positions and spacing for better visibility
blocks = [
    ("User Input (Token Sequence)", 10.8),
    ("Token Embedding", 10.0),
    ("Positional Encoding", 9.2),
    ("Transformer Decoder Stack (×N)", 8.4),
    ("LayerNorm", 7.6),
    ("Multi-Head Attention", 6.8),
    ("Add & Norm (Residual)", 6.0),
    ("Feedforward Network", 5.2),
    ("Add & Norm (Residual)", 4.4),
    ("⋮ (Repeated for N Layers)", 3.6),
    ("Final Linear + Softmax", 2.8),
    ("Output Probabilities", 2.0),
    ("Next Predicted Token", 1.2)
]

# Colors for aesthetics
fill_color = "#E0F2F1"  # Light teal background
edge_color = "#00796B"  # Dark teal border

# Draw each block as a rounded rectangle with labels
for label, y in blocks:
    rect = patches.FancyBboxPatch((3.5, y), 5, 0.6,
                                  boxstyle="round,pad=0.02",
                                  edgecolor=edge_color, facecolor=fill_color, linewidth=1.5)
    ax.add_patch(rect)
    ax.text(6, y + 0.3, label, ha='center', va='center', fontsize=10)

# Add vertical arrows between blocks
for i in range(len(blocks) - 1):
    y1 = blocks[i][1]
    y2 = blocks[i + 1][1]
    ax.annotate("", xy=(6, y2 + 0.6), xytext=(6, y1),
                arrowprops=dict(arrowstyle="->", lw=1.2, color='black'))

plt.tight_layout()
plt.savefig("/mnt/data/Figure_3_4_GPT_Architecture_Vertical.png", dpi=300, bbox_inches='tight')
plt.show()
