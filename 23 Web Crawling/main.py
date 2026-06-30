import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()

@app.get("/news")
def get_news():
    url = "https://indianexpress.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = []

    for item in soup.find_all("a", class_ = "topblockNews_sidebarLink"):
        title.append(item.text)

        return{
            "news": title[:5]
        }