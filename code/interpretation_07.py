import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# Set up figure
fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 20)
ax.set_ylim(0, 12)
ax.axis('off')

# Helper to add a box
def add_box(x, y, text, color, width=2.5, height=1.2, fontsize=9, bold=False):
    box = FancyBboxPatch((x, y), width, height,
                         boxstyle="round,pad=0.02", fc=color, ec='black', lw=1.2)
    ax.add_patch(box)
    ax.text(x + width / 2, y + height / 2, text, ha='center', va='center',
            fontsize=fontsize, weight='bold' if bold else 'normal')

# Helper to draw an arrow
def draw_arrow(start, end):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle='->', mutation_scale=12, lw=1.2, color='black'))

# Colors
color_input = "#ccffe5"
color_embed = "#aee1f9"
color_transformer = "#e0e0ff"
color_output = "#ffe4cc"

# Step 1: Vertical Input Layer Stack (Left)
add_box(1, 9.5, "Input\nToken", color_input)
add_box(1, 7.5, "Positional\nEncoding", color_embed)
add_box(1, 5.5, "Token + Position\nEmbeddings", color_embed)

# Arrow to Transformer Block
draw_arrow((3.6, 6.1), (5, 6.1))

# Step 2: Horizontal Transformer Blocks (Center)
x_start = 5
layer_y = 5.3
block_width = 2.6

add_box(x_start, layer_y, "Multi-Head\nAttention", color_transformer)
add_box(x_start + block_width, layer_y, "Add & Norm", color_transformer)
add_box(x_start + block_width * 2, layer_y, "Feedforward", color_transformer)
add_box(x_start + block_width * 3, layer_y, "Add & Norm", color_transformer)

# Label "Stacked N Times"
ax.text(x_start + block_width * 1.5, 7.2, "Transformer Block\n(repeated N times)", ha='center', fontsize=9, weight='bold')

# Arrows between sublayers
for i in range(3):
    draw_arrow((x_start + block_width * (i) + 2.6, 6.1), (x_start + block_width * (i+1), 6.1))

# Arrow to Output
draw_arrow((x_start + block_width * 4, 6.1), (x_start + block_width * 4 + 2, 6.1))

# Step 3: Output Layers
add_box(x_start + block_width * 4 + 2, 5.5, "Linear", color_output)
add_box(x_start + block_width * 4 + 2, 3.5, "Softmax", color_output)
add_box(x_start + block_width * 4 + 2, 1.5, "Predicted\nToken", color_output)

# Vertical arrows down from output
draw_arrow((x_start + block_width * 4 + 3.25, 5.5), (x_start + block_width * 4 + 3.25, 4.2))
draw_arrow((x_start + block_width * 4 + 3.25, 3.5), (x_start + block_width * 4 + 3.25, 2.2))

# Loopback arrow to input (autoregression)
draw_arrow((x_start + block_width * 4 + 2.8, 1.5), (2.2, 10.3))

# Caption
ax.text(10, 0.5, "Figure 3.4: GPT model architecture. Tokens are passed through a stack of transformer blocks\nthat include self-attention and feedforward sublayers. The output token is autoregressively fed back into the model.",
        ha='center', fontsize=9, style='italic')

# Save final version
final_path = "/mnt/data/Figure_3_4_GPT_Architecture_Final.png"
plt.savefig(final_path, dpi=300, bbox_inches='tight')
plt.close()

final_path
