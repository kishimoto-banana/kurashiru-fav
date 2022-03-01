from urllib.parse import urljoin

from bs4 import BeautifulSoup
from crawler.selenium import fetch_fav_html
from infrastructure.spreadsheet import update

from domain.recipe import Recipe

KURACHIRU_BASE_URL = "https://www.kurashiru.com/"


def absolute_kurashiru_url(url):
    return urljoin(KURACHIRU_BASE_URL, url)


def generate_recipe(html):
    title = html.get_text(strip=True)
    url = absolute_kurashiru_url(html.get("href"))
    image_url = html.find("img")["src"]

    return Recipe(title=title, url=url, image_url=image_url)


def save_recipes(recipes):
    update(recipes)


def get_favs():
    html = fetch_fav_html()
    soup = BeautifulSoup(html, "html.parser")
    elements = [
        elem
        for elem in soup.select(
            "#account > div.section.user-contents > div > div > div > a"
        )
    ]

    recipes = [generate_recipe(elem) for elem in elements[::-1]]
    return recipes
