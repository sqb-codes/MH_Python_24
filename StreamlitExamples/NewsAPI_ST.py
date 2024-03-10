import streamlit as st
import urllib.request as url
import json

st.title("News Fetch Example")
st.write("This app can fetch news of any category")

choice = st.selectbox("Select Category", 
                       ["Top Headlines", 
                        "Sports News", 
                        "Business News", 
                        "Entertainment News", 
                        "Health News", 
                        "Technology News",
                        "Science News"])

btn = st.button("Fetch News")

if btn:

    categories = {
        "Business News" : "business",
        "Entertainment News" : "entertainment",
        "Health News" : "health",
        "Science News" : "science",
        "Sports News" : "sports",
        "Technology News" : "technology"
    }

    if choice == "Top Headlines":
        PATH = "https://newsapi.org/v2/top-headlines?country=in&apiKey=695e07af402f4b119f0703e9b19f4683"

    else:
        category = categories[choice]
        PATH = f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey=695e07af402f4b119f0703e9b19f4683"


    response = url.urlopen(PATH)
    data = json.load(response)

    # print(data)
    articles = data['articles']

    for i in range(len(articles)):
        st.write(articles[i]['title'])
        st.write("========================")

