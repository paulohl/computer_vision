import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# GPT Architecture stages
gpt_layers = [
    "Input Token Embedding",
    "Positional Encoding",
    "Layer Normalization",
    "Multi-Head Self-Attention",
    "Residual Connection",
    "Feedforward Layer",
    "Residual Connection",
    "Layer Normalization",
    "Output Logits (Vocab Size)",
    "Softmax Probabilities"
]

# Define colors
box_color = "#B0E0E6"
text_color = "black"
edge_color = "#4682B4"

# Create figure
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor("white")
ax.axis("off")

# Draw boxes with labels
box_width = 0.8
box_height = 0.6
y_start = len(gpt_layers) - 1
for i, layer in enumerate(gpt_layers):
    y_pos = y_start - i
    ax.add_patch(FancyBboxPatch(
        (0.1, y_pos), box_width, box_height,
        boxstyle="round,pad=0.02",
        facecolor=box_color,
        edgecolor=edge_color,
        linewidth=1.5
    ))
    ax.text(0.5, y_pos + box_height / 2, layer,
            ha='center', va='center', fontsize=12, color=text_color)

# Arrows between layers
for i in range(len(gpt_layers) - 1):
    y_pos = y_start - i
    ax.annotate("",
                xy=(0.5, y_pos),
                xytext=(0.5, y_pos - 0.4),
                arrowprops=dict(arrowstyle="->", color=edge_color, lw=1.5))

# Add a title
plt.title("Figure 3.4 – GPT Architecture: Layer-by-Layer Vertical View", fontsize=14, weight='bold')

# Save and display
output_path = "/mnt/data/Figure_3_4_GPT_Architecture_Improved.png"
plt.tight_layout()
plt.savefig(output_path, dpi=300)
plt.show()
