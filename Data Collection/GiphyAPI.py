# python
import json
from urllib import parse, request

url = "http://api.giphy.com/v1/gifs/search"

params = parse.urlencode({
  "q": "mr bean",
  "api_key": "1gPMgQWU9fDU9PPHW2Kr917sPJlo3n2g",
  "limit": "10"
})
path = "".join((url, "?", params))

response = request.urlopen(path)
data = json.load(response)
data = data['data']
for i in range(len(data)):
    print("Downloading Image...")
    img = data[i]
    images = img['images']
    img_url = images["original"]["url"]
    request.urlretrieve(img_url, f"toj_{i}.gif")




