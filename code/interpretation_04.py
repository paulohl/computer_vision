# Re-import libraries due to code execution environment reset
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# Set up the figure
fig, ax = plt.subplots(figsize=(12, 6))
ax.axis('off')
ax.set_facecolor("white")

# Define GPT versions and details
models = [
    {
        "title": "GPT-1",
        "year": "2018",
        "params": "117M",
        "highlights": [
            "Unsupervised learning on BookCorpus",
            "Baseline Transformer architecture",
            "Strong performance on LAMBADA, GLUE, SQuAD"
        ],
        "color": "#B0C4DE"
    },
    {
        "title": "GPT-2",
        "year": "2019",
        "params": "1.5B",
        "highlights": [
            "Larger dataset, improved sampling algorithm",
            "Better training objective",
            "Model not released initially due to safety concerns"
        ],
        "color": "#ADD8E6"
    },
    {
        "title": "GPT-3",
        "year": "2020",
        "params": "175B",
        "highlights": [
            "Few-shot, one-shot, zero-shot capabilities",
            "API access via OpenAI",
            "Massive scale brings coherence but also biases"
        ],
        "color": "#87CEEB"
    },
    {
        "title": "GPT-3.5",
        "year": "2022",
        "params": "1.3B, 6B, 175B",
        "highlights": [
            "Instruct-tuned models",
            "Used in ChatGPT (free-tier)",
            "Reinforcement Learning from Human Feedback (RLHF)"
        ],
        "color": "#4682B4"
    },
    {
        "title": "GPT-4",
        "year": "2023",
        "params": "est. 1T (not confirmed)",
        "highlights": [
            "Multimodal (text + image input)",
            "Improved factuality and steerability",
            "Used in ChatGPT Plus and Copilot"
        ],
        "color": "#5F9EA0"
    }
]

# Plot each model
for i, model in enumerate(models):
    x = i * 2.5
    y = 5
    # Title Box
    ax.add_patch(FancyBboxPatch((x, y), 2, 0.7, boxstyle="round,pad=0.02", fc=model["color"], ec="black", linewidth=1.5))
    ax.text(x + 1, y + 0.35, f"{model['title']} ({model['year']})", ha="center", va="center", fontsize=10, fontweight='bold')

    # Parameters
    ax.text(x + 1, y - 0.2, f"Parameters: {model['params']}", ha="center", va="center", fontsize=9)

    # Highlights
    for j, highlight in enumerate(model["highlights"]):
        ax.text(x + 1, y - 0.6 - 0.35 * j, f"• {highlight}", ha="center", va="top", fontsize=8)

plt.tight_layout()
plt.savefig("/mnt/data/Figure_3_5_GPT_Timeline_Cleaned.png", dpi=300, bbox_inches="tight")
plt.show()

