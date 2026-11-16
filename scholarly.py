import networkx as nx

# Create scholarly citation network
G = nx.DiGraph()

# Add citation relationships
citations = [
    ("Paper1", "Paper2"),
    ("Paper1", "Paper3"),
    ("Paper2", "Paper3"),
    ("Paper3", "Paper4"),
    ("Paper4", "Paper1"),
    ("Paper5", "Paper2"),
    ("Paper5", "Paper3")
]

G.add_edges_from(citations)

# Calculate PageRank
rank = nx.pagerank(G)

# Display citation network
print("Citation Network:")

for edge in G.edges():
    print(edge[0], "->", edge[1])

# Display PageRank
print("\nScholarly PageRank:")

for paper, score in sorted(
    rank.items(), key=lambda x: x[1], reverse=True
):
    print(paper, ":", round(score, 4))