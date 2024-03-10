import urllib.request as url
import json

categories = {
        "2" : "business",
        "3" : "entertainment",
        "4" : "health",
        "5" : "science",
        "6" : "sports",
        "7" : "technology"
    }

print("""
1. Top Headlines
2. Business News
3. Entertainment News
4. Health News
5. Science News
6. Sports News
7. Technology News
""") 

choice = input("Enter your choice : ")

if choice == "1":
    PATH = "https://newsapi.org/v2/top-headlines?country=in&apiKey=695e07af402f4b119f0703e9b19f4683"

else:
    category = categories[choice]
    PATH = f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey=695e07af402f4b119f0703e9b19f4683"


response = url.urlopen(PATH)
data = json.load(response)

# print(data)
articles = data['articles']

for i in range(len(articles)):
    print(articles[i]['title'])
    print("========================")