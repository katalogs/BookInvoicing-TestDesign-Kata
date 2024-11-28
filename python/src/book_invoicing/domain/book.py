from enum import StrEnum
from typing import List

from src.book_invoicing.domain.country import Country, Language
from abc import ABC, abstractmethod


class Category(StrEnum):
    BUSINESS = "Business"
    LANGUAGE = "Language"
    COMPUTER = "Computer"


class Genre(StrEnum):
    HORROR_FICTION = "HorrorFiction"
    THRILLER = "Thriller"
    DARK_FANTASY = "DarkFantasy"
    MYSTERY = "Mystery"
    ADVENTURE_FICTION = "AdventureFiction"
    NON_FICTION = "NonFiction"
    ROMANCE = "Romance"


class Author:
    _name: str
    _nationality: Country

    def __init__(self, name, nationality: Country):
        self._name = name
        self._nationality = nationality

    def __str__(self):
        return f"Author [ Name: '{self._name}', Nationality: '{self._nationality}' ]"

    def __eq__(self, other):
        if not isinstance(other, Author):
            return False
        return self._name == other.name and self.nationality == other.nationality

    def __hash__(self):
        return hash((self._name, self.nationality))

    @property
    def name(self) -> str:
        return self._name

    @property
    def nationality(self) -> Country:
        return self._nationality


class Book(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @property
    @abstractmethod
    def author(self):
        pass

    @property
    @abstractmethod
    def language(self):
        pass


class EducationalBook(Book):
    def __init__(self, name: str, price: float, author: Author, language: Language, category: Category):
        self._name = name
        self._price = price
        self._author = author
        self._language = language
        self._category = category

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self):
        return self._price;

    @property
    def author(self) -> Author:
        return self._author

    @property
    def language(self) -> Language:
        return self._language

    @property
    def category(self) -> Category:
        return self._category

    def __str__(self):
        return (f"EducationalBook [ Name: {self._name}, "
                f"Price: '{self.price}', "
                f"Author: '{self.author}', "
                f"Language: '{self.language}', "
                f"Category: '{self.category}' ]")

    def __eq__(self, other):
        if not isinstance(other, EducationalBook):
            return False
        return (self.name == other.name and
                self.price == other.price and
                self.author == other.author and
                self.language == other.language and
                self.category == other.category)

    def __hash__(self):
        return hash((self._name, self.price, self.author, self.language, self.category))


class Novel(Book):
    def __init__(self, name: str, price: float, author: Author, language: Language, genres: List[Genre]):
        self._name = name
        self._price = price
        self._author = author
        self._language = language
        self._genres = genres

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price

    @property
    def author(self) -> Author:
        return self._author

    @property
    def language(self) -> Language:
        return self._language

    @property
    def genres(self) -> List[Genre]:
        return self._genres

    def __str__(self):
        return (f"Novel [ Name: '{self.name}', "
                f"Price: '{self.price}', "
                f"Author: '{self.author}', "
                f"Language: '{self.language}', "
                f"Genres: '{self.genres}' ]")

    def __eq__(self, other):
        if not isinstance(other, Novel):
            return False
        return (self.name == other.name and
                self.price == other.price and
                self.author == other.author and
                self.language == other.language and
                self.genres == other.genres)

    def __hash__(self):
        return hash((self.name, self.price, self.author, self.language, tuple(self.genres)))
