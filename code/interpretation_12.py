import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Set up the figure
fig, ax = plt.subplots(figsize=(12, 14))
ax.axis('off')
ax.set_facecolor("white")

# Box properties
box_style = dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="#ccffe5", linewidth=1)

# Helper to add text boxes
def add_box(text, xy, ax, size=10, ha="center", va="center"):
    ax.text(*xy, text, ha=ha, va=va, fontsize=size, bbox=box_style)

# Coordinates are in (x, y)
# Vertical layout of GPT Architecture

# Input layer
add_box("Input Text Sequence", (0.5, 0.95), ax)

# Positional Embedding
add_box("Calculate position-encoded\nembeddings for each word", (0.5, 0.88), ax)

# Token + Positional Embeddings stack
add_box("Word1_PosEmb_Embedding", (0.5, 0.81), ax)
add_box("Word2_PosEmb_Embedding", (0.5, 0.76), ax)
add_box("...", (0.5, 0.72), ax)
add_box("WordN_PosEmb_Embedding", (0.5, 0.68), ax)

# Self-attention block (grouped together with line)
ax.text(0.5, 0.62, "Self-Attention Layer", ha="center", fontsize=11, weight='bold')

add_box("Query, Key & Value vectors\nfor Word1", (0.5, 0.58), ax)
add_box("Query, Key & Value vectors\nfor Word2", (0.5, 0.53), ax)
add_box("...", (0.5, 0.49), ax)
add_box("Query, Key & Value vectors\nfor WordN", (0.5, 0.45), ax)
add_box("Calculate Self-attention output\nusing query, key & value vectors", (0.5, 0.40), ax)

# Output of Self-attention Layer
add_box("Self-attention Output Vector\nfor Word1", (0.5, 0.34), ax)
add_box("...", (0.5, 0.30), ax)
add_box("Self-attention Output Vector\nfor WordN", (0.5, 0.26), ax)

# Feed Forward Network and Prediction
add_box("Feed Forward Network (FFN)", (0.5, 0.20), ax)
add_box("Predict probability of\nnext word (Softmax)", (0.5, 0.14), ax)
add_box("Word(N+1)", (0.5, 0.08), ax)
add_box("Add to input sequence", (0.5, 0.03), ax)
add_box("New Input Sequence", (0.5, -0.03), ax)

# Arrows between each block
def draw_arrow(y1, y2):
    ax.annotate("", xy=(0.5, y2), xytext=(0.5, y1),
                arrowprops=dict(arrowstyle="->", color="black", lw=1.2))

ys = [0.95, 0.88, 0.81, 0.76, 0.72, 0.68, 0.62, 0.58, 0.53, 0.49, 0.45,
      0.40, 0.34, 0.30, 0.26, 0.20, 0.14, 0.08, 0.03, -0.03]

for i in range(len(ys)-1):
    draw_arrow(ys[i], ys[i+1])

# Save the figure
plt.tight_layout()
output_path = "/mnt/data/Figure_3_4_GPT_Architecture_Vertical_Fixed.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()

output_path
