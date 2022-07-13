# url-network-visualizer
(C)Tsubasa Kato at Inspire Search Corporation 2022/7/14

Add one URL per line in urls.txt. 

visualize-links-with-label.py will use httplib2 to connect to the sites in the urls.txt and Beautiful Soup will extract all links.

This will be put into Panda dataframe and then to networkx for network study.
This will then be put into matplotlib for visualization.

