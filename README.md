# url-network-visualizer
![url-network-visualizer screenshot](https://github.com/stingraze/url-network-visualizer/blob/main/url-visualize-links.jpg?raw=true)
(C)Tsubasa Kato at Inspire Search Corporation 2022/7/14

Add one URL per line in urls.txt. 

visualize-links-with-label.py will use httplib2 to connect to the sites in the urls.txt and Beautiful Soup will extract all links.

This will be put into pandas dataframe and then to networkx for network study.
This will then be put into matplotlib for visualization.

Error handling when df value is None was implemented on 10/26/2022 17:30PM.

Last updated on 4/12/2023 (Added 2 more scripts)
