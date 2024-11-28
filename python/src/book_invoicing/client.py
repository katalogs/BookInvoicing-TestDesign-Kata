from abc import ABC, abstractmethod
from collections import defaultdict

from src.book_invoicing.domain.book import Book
from src.book_invoicing.domain.country import Country
from src.book_invoicing.domain.purchase import Invoice, PurchasedBook
from src.book_invoicing.storage import MainRepository


class OrderInterface(ABC):

    @abstractmethod
    def add_book(self, book: Book, quantity: int) -> None:
        pass

    def checkout(self) -> Invoice:
        pass

    def get_quantity_of(self, book: Book) -> int:
        pass


class BooksOrder(OrderInterface):
    def __init__(self, client):
        self._client = client
        self._books_in_basket = defaultdict(int)

    def add_book(self, book, quantity):
        existing_quantity = self._books_in_basket[book]
        self._books_in_basket[book] = existing_quantity + quantity

    def check_out(self):
        invoice = Invoice(self._client.name, self._client.country)

        for book, quantity in self._books_in_basket.items():
            invoice.add_purchased_book(PurchasedBook(book, quantity))

        MainRepository.get_configured_repository().add_invoice(invoice)
        return invoice

    def get_quantity_of(self, book):
        return self._books_in_basket.get(book, 0)


class Client:
    def __init__(self, name: str, country: Country):
        self._name = name
        self._country = country

    @property
    def name(self) -> str:
        return self._name

    @property
    def country(self) -> Country:
        return self._country

    def __str__(self):
        return f"Client [ Name: '{self._name}', Country: '{self._country}' ]"

    def __eq__(self, other):
        if not isinstance(other, Client):
            return False
        return self._name == other.name and self._country == other.country

    def __hash__(self):
        return hash((self._name, self._country))
