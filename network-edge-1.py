import httplib2
from bs4 import BeautifulSoup
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

links_with_text = []

http = httplib2.Http()

# Reads urls.txt (one URL per line)
with open('urls.txt') as f:
    list_urls = f.read().splitlines()

# Loop through each URL
for link_to_crawl in list_urls:
    response = http.request(link_to_crawl)
    soup = BeautifulSoup(str(response), "html.parser")
    
    # Loop through each link found on the page
    for link in soup.findAll('a'):
        # If statement that handles error
        if (link.get('href') == None):
            continue
        
        links_with_text.append([link_to_crawl, link.get('href')])
        print(link_to_crawl + " -> " + str(link.get('href')))

# Save the edges as a file using an array, one line per array
with open('edges.txt', 'w') as f:
    for edge in links_with_text:
        f.write(str(edge) + '\n')

# Create a DataFrame and clean up missing data
df = pd.DataFrame(links_with_text, columns=["from", "to"])
df = df.dropna(how='all').dropna(how='all', axis=1)

# Create a graph from the DataFrame
GA = nx.from_pandas_edgelist(df, source="from", target="to")

# Plot the graph
plt.figure(2)
nx.draw(GA, node_size=60, font_size=8, with_labels=True, font_color='darkgreen', edge_color='lightgray')
plt.show()
