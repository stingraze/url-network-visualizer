#(C) Tsubasa Kato 2023 4/12/2023 9:15AM JST Modified script using ChatGPT GPT-4.
import httplib2
from bs4 import BeautifulSoup
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from urllib.parse import urljoin

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
        
        # Convert relative URLs to full URLs
        full_url = urljoin(link_to_crawl, link.get('href'))
        
        links_with_text.append([link_to_crawl, full_url])
        print(link_to_crawl + " -> " + full_url)

# Create a DataFrame and clean up missing data
df = pd.DataFrame(links_with_text, columns=["from", "to"])
df = df.dropna(how='all').dropna(how='all', axis=1)

# Save the edges as a CSV file
df.to_csv('edges.csv', index=False)

# Create a graph from the DataFrame
GA = nx.from_pandas_edgelist(df, source="from", target="to")

# Plot the graph
plt.figure(2)
nx.draw(GA, node_size=60, font_size=8, with_labels=True, font_color='darkgreen', edge_color='lightgray')
plt.show()
