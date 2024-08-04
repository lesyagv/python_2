from bs4 import BeautifulSoup
from .locators import PageLocators
from .parsers import BookParser
import re


class Pages:

    def __init__(self, page) -> None:
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def page_count(self):
        content = self.soup.select_one(PageLocators.PAGER).string

        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))

        return pages

    @property
    def books(self):
        return [BookParser(e) for e in self.soup.select(PageLocators.BOOKS)]