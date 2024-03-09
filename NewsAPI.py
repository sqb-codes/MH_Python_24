import urllib.request as url
import json


API_KEY = "695e07af402f4b119f0703e9b19f4683"
path = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}"

response = url.urlopen(path)
data = json.load(response)

# print(data)
articles = data['articles']

for i in range(len(articles)):
    print(articles[i]['title'])
    print("========================")

