import xml.etree.ElementTree as ET
import networkx as nx

# XML data
xml_data = """
<pages>
    <page id="A">
        <link>B</link>
        <link>C</link>
    </page>
    <page id="B">
        <link>C</link>
    </page>
    <page id="C">
        <link>A</link>
    </page>
</pages>
"""

# Parse XML
root = ET.fromstring(xml_data)

# Create web graph
G = nx.DiGraph()

for page in root.findall("page"):

    source = page.get("id")

    for link in page.findall("link"):
        destination = link.text
        G.add_edge(source, destination)

# Calculate PageRank
rank = nx.pagerank(G)

# Display results
print("Web Graph:", list(G.edges()))

print("\nPageRank Results:")

for page, score in rank.items():
    print(page, ":", round(score, 4))