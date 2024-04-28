import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load the adjacency matrix from the CSV file
df = pd.read_csv('graph.csv', header=None)

# Create a directed graph from the adjacency matrix
G = nx.from_pandas_adjacency(df, create_using=nx.DiGraph())

# Draw the graph
nx.draw(G, with_labels=True, arrows=True)
plt.show()