#(C)Tsubasa Kato at Inspire Search Corporation 2022/7/14.
#Some codes from: https://medium.com/@dakarabas/how-to-easily-visualize-your-internal-links-with-python-4467ef1e8c4d
import httplib2
from bs4 import BeautifulSoup
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

links_with_text = []

http = httplib2.Http()
#Reads urls.txt (one URL per line)
with open('urls.txt') as f:
    list_urls = f.read().splitlines()

for link_to_crawl in list_urls:
    response = http.request(link_to_crawl)
    soup = BeautifulSoup(str(response), "html.parser")
    for link in soup.findAll('a'):
        links_with_text.append([link_to_crawl, link.get('href')])
        print(link_to_crawl + " -> " + link.get('href'))


df = pd.DataFrame(links_with_text, columns=["from", "to"])

GA = nx.from_pandas_edgelist(df, source="from", target="to")
plt.figure(2)
nx.draw(GA,node_size=60,font_size=8,with_labels=True,font_color='darkgreen',edge_color='lightgray') 
plt.show()


