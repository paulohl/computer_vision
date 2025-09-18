import matplotlib.pyplot as plt
import numpy as np

# Dark theme setup
plt.style.use('dark_background')

# Data
models = ["GPT-1","GPT-2","GPT-3","GPT-3.5","GPT-4"]
years = [2018, 2019, 2020, 2022, 2023]
params = [1.17e8, 1.5e9, 1.75e11, 1.75e11, 1e12]  # parameters
context = [512, 1024, 2048, 8192, 32000]          # tokens

# Plot
fig, ax1 = plt.subplots(figsize=(10,6))
ax2 = ax1.twinx()

# Parameters (log scale)
ax1.plot(years, params, marker='o', color='cyan', linewidth=2, label='Parameters')
ax1.set_yscale('log')
ax1.set_ylabel('Parameters (log scale)', color='cyan', fontsize=10)
ax1.tick_params(axis='y', colors='cyan')

# Context length
ax2.plot(years, context, marker='s', color='orange', linewidth=2, label='Context Length')
ax2.set_ylabel('Context Length (tokens)', color='orange', fontsize=10)
ax2.tick_params(axis='y', colors='orange')

# X-axis
ax1.set_xticks(years)
ax1.set_xticklabels(models, rotation=30, fontsize=9)
ax1.set_xlabel('Model Release', fontsize=10)

# Title and grid
plt.title('Figure 3.6 – GPT Scaling Timeline: Parameters vs Context Length', fontsize=12, fontweight='bold')
ax1.grid(alpha=0.3, linestyle='--')

# Annotations
for x,y,m in zip(years, params, models):
    ax1.text(x, y*1.2, m, color='cyan', fontsize=8, ha='center')

plt.tight_layout()
plt.show()
