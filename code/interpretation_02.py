# Create Figure 3.6 – GPT Scaling Timeline: Parameters vs Context Length
# Generates both high-resolution PNG and SVG assets.

import matplotlib.pyplot as plt
import numpy as np

# Data
models = ["GPT-1","GPT-2","GPT-3","GPT-3.5","GPT-4"]
years = [2018, 2019, 2020, 2022, 2023]
params = [1.17e8, 1.5e9, 1.75e11, 1.75e11, 1e12]  # parameters
context = [512, 1024, 2048, 8192, 32000]          # tokens

# Plot
fig, ax1 = plt.subplots(figsize=(12, 7))
ax2 = ax1.twinx()

# Parameters (log scale) - using default matplotlib colors (per tool guidance)
line1, = ax1.plot(years, params, marker='o', linewidth=2, label='Parameters')
ax1.set_yscale('log')
ax1.set_ylabel('Parameters (log scale)')
ax1.tick_params(axis='y')

# Context length
line2, = ax2.plot(years, context, marker='s', linewidth=2, label='Context Length')
ax2.set_ylabel('Context Length (tokens)')
ax2.tick_params(axis='y')

# X-axis
ax1.set_xticks(years)
ax1.set_xticklabels(models, rotation=0, fontsize=11)
ax1.set_xlabel('Model Release')

# Title and grid
plt.title('Figure 3.6 – GPT Scaling Timeline: Parameters vs Context Length', fontsize=14, fontweight='bold')
ax1.grid(alpha=0.25, linestyle='--')

# Legend
lines = [line1, line2]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left')

# Annotations for key milestones
for x, y, m in zip(years, params, models):
    ax1.annotate(m, (x, y), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10)

# Layout
plt.tight_layout()

# Save high-resolution PNG and SVG
png_path = '/mnt/data/figure_3_6_gpt_scaling_timeline.png'
svg_path = '/mnt/data/figure_3_6_gpt_scaling_timeline.svg'
fig.savefig(png_path, dpi=400, bbox_inches='tight')
fig.savefig(svg_path, format='svg', bbox_inches='tight')

png_path, svg_path

