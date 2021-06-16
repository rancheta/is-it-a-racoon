import requests
from fastbook import *
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import os
import sys

subscription_key = key = os.environ.get('AZURE_KEY')
search_url = "https://api.bing.microsoft.com/v7.0/images/search"
search_term = sys.argv[1]
count = sys.argv[2] or 10
print("Retrieving Images For Term: ", search_term)
print("Count: ", count)

results = search_images_bing(key, search_term, min_sz=128, max_images=count)
ims = results.attrgot('contentUrl')
print("Results: ", results)

path = Path("./images/" + search_term)

if not path.exists():
    path.mkdir()
    download_images(path, urls=ims)
    print("Images downloaded into ", path)
else:
    print("Directory already exists.")

print("Terminating")
