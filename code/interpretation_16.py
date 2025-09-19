# Regenerate the vertical GPT architecture diagram with centered layout
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# New centered figure
fig, ax = plt.subplots(figsize=(6, 10))
ax.axis('off')

# Define new centered block positions (x=1.5 to 5.5)
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

fill_color = "#E0F2F1"
edge_color = "#00796B"

for label, y in blocks:
    rect = patches.FancyBboxPatch((1.5, y), 4, 0.6,
                                  boxstyle="round,pad=0.02",
                                  edgecolor=edge_color, facecolor=fill_color, linewidth=1.5)
    ax.add_patch(rect)
    ax.text(3.5, y + 0.3, label, ha='center', va='center', fontsize=10)

# Arrows centered along x = 3.5
for i in range(len(blocks) - 1):
    y1 = blocks[i][1]
    y2 = blocks[i + 1][1]
    ax.annotate("", xy=(3.5, y2 + 0.6), xytext=(3.5, y1),
                arrowprops=dict(arrowstyle="->", lw=1.2, color='black'))

# Save corrected image
corrected_path = "/mnt/data/Figure_3_4_GPT_Architecture_Centered.png"
plt.tight_layout()
plt.savefig(corrected_path, dpi=300, bbox_inches='tight')
plt.show()
