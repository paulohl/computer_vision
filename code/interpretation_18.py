import zipfile

# Recreate the diagram image since the session was reset
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Generate the diagram again
fig, ax = plt.subplots(figsize=(10, 8))
ax.axis('off')

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

fill_color = "#E0F2F1"
edge_color = "#00796B"

for label, y in blocks:
    rect = patches.FancyBboxPatch((3.5, y), 5, 0.6,
                                  boxstyle="round,pad=0.02",
                                  edgecolor=edge_color, facecolor=fill_color, linewidth=1.5)
    ax.add_patch(rect)
    ax.text(6, y + 0.3, label, ha='center', va='center', fontsize=10)

for i in range(len(blocks) - 1):
    y1 = blocks[i][1]
    y2 = blocks[i + 1][1]
    ax.annotate("", xy=(6, y2 + 0.6), xytext=(6, y1),
                arrowprops=dict(arrowstyle="->", lw=1.2, color='black'))

img_path = "/mnt/data/Figure_3_4_GPT_Architecture_Vertical.png"
plt.tight_layout()
plt.savefig(img_path, dpi=300, bbox_inches='tight')
plt.close()

# Create the ZIP archive
zip_path = "/mnt/data/Figure_3_4_GPT_Architecture.zip"
with zipfile.ZipFile(zip_path, 'w') as zipf:
    zipf.write(img_path, arcname="Figure_3_4_GPT_Architecture_Vertical.png")

zip_path
