from graphviz import Digraph

# Initialize the diagram
dot = Digraph(format='png')
dot.attr(rankdir='TB', size='8,10', bgcolor='white')
dot.attr('node', style='filled', fillcolor='mintcream', fontname='Helvetica', fontsize='10')

# Input and Embeddings
dot.node('Input', 'Input Text Sequence')
dot.node('PosEnc', 'Calculate Position Embeddings')
dot.node('Embeddings', 'Token + Positional Embeddings')

# Self-Attention Layer
dot.attr('node', fillcolor='honeydew', fontsize='10')
dot.node('SelfAttentionHeader', 'Self-Attention Layer', shape='plaintext')
dot.node('QKV', 'Create Q, K, V vectors')
dot.node('AttentionScores', 'Compute Attention Scores\n(Q · Kᵀ / √dₖ)')
dot.node('WeightedSum', 'Generate Weighted Sum\n(Attention × V)')
dot.node('MultiHead', 'Concatenate Heads + Linear Projection')

# Feed Forward & Output
dot.attr('node', fillcolor='mintcream', fontsize='10')
dot.node('FFN', 'Feed Forward Network (FFN)')
dot.node('Softmax', 'Softmax to Predict Next Token')
dot.node('AppendToken', 'Append Predicted Token to Sequence')
dot.node('Output', 'Final Output Sequence')

# Connections
dot.edge('Input', 'PosEnc')
dot.edge('PosEnc', 'Embeddings')
dot.edge('Embeddings', 'QKV')
dot.edge('QKV', 'AttentionScores')
dot.edge('AttentionScores', 'WeightedSum')
dot.edge('WeightedSum', 'MultiHead')
dot.edge('MultiHead', 'FFN')
dot.edge('FFN', 'Softmax')
dot.edge('Softmax', 'AppendToken')
dot.edge('AppendToken', 'Output')

# Render the figure
output_path = "/mnt/data/Figure_3_4_GPT_Architecture_Definitive.png"
dot.render(filename=output_path, cleanup=False)

output_path
