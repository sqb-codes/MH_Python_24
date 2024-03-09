import urllib.request as url
import bs4

path = "https://www.snapdeal.com/products/mens-footwear-sports-shoes"

# 1. Make HTTPRequest to the URL from where you want to scrap the data
response = url.urlopen(path)
# 2. If you get HTTPResponse in return then you need bs4 package

# 3. Pass your response inside bs4.BeautifulSoup
page = bs4.BeautifulSoup(response)
# In return you will get the whole HTML of the web page that you requested

# print(page)

# fetch one item at a time
# title = page.find('p', {'class' : 'product-title'})
# print("Title :",title.text)

# price = page.find('span', {'class' : 'product-price'})
# print("Price :",price.text)


# fetch all items
titleList = page.find_all('p', {'class' : 'product-title'})
priceList = page.find_all('span', {'class' : 'product-price'})

# print(len(titleList), len(priceList))
for i in range(len(titleList)):
    print("Title :",titleList[i].text)
    print("Price :",priceList[i].text)
    print("========================")

