import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

# Get topic from user
topic = input("Enter topic: ")

# Search news using Google News RSS
url = "https://news.google.com/rss/search?q=" + quote(topic)

response = requests.get(url)
soup = BeautifulSoup(response.content, "xml")

print("\nNews Stories:")

count = 0

for item in soup.find_all("item"):

    title = item.title.text
    link = item.link.text

    print("\nTitle:", title)
    print("Link:", link)

    count += 1

    if count == 10:
        break

print("\nTotal News Stories:", count)