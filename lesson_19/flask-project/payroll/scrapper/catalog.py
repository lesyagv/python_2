# flask-project/payroll/scraper/catalog.py

import requests
from .pages import Pages

url = 'https://news.ycombinator.com'


class Catalog:
    _books = []

    def __init__(self) -> None:
        self.page_content = requests.get(url).content
        self.page = Pages(self.page_content)
        self._books = self.books()

    def books(self):
        books = []

        for page_num in range(self.page.page_count):
            URL = f'{url}/catalogue/page-{page_num + 1}.html'
            page_content = requests.get(URL).content
            page = Pages(page_content)
            books.extend(page.books)

        return books

    def best_books(self):
        best_books = sorted(self._books, key=lambda x: x.rating * -1)[:10]
        return best_books

    def cheapest_books(self):
        cheapest_books = sorted(self._books, key=lambda x: x.price)[:10]
        return cheapest_books
