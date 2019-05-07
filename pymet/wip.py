from bs4 import BeautifulSoup
import os
import requests

from pymet import collection
from pymet.utils import constants


paintings = collection.MetPaintings()
works = paintings.get_works_by_artist('gogh')

path = os.path.join(constants.Urls.MET_ROOT, str(works[1].object_id))

res = requests.get(path)

soup = BeautifulSoup(res.text, 'xml')

for img_src in soup.find_all('img'):
    print(img_src)
