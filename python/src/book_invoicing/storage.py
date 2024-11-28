import json
import os
from typing import Dict, List

from src.book_invoicing.domain.book import Book, EducationalBook, Novel, Author, Category, Genre
from src.book_invoicing.domain.country import Country, Currency, Language
from src.book_invoicing.domain.purchase import Invoice, PurchasedBook
from src.book_invoicing.domain.repository import Repository


class Record:
    def __init__(self, id: int, client: str, country: Dict, books_in_basket: List[Dict]):
        self.id = id
        self.client = client
        self.country = country
        self.booksInBasket = books_in_basket


class JsonLoader:

    def load(self, filename: str) -> List[Record]:
        content = JsonLoader.get_json_content(filename)
        return JsonLoader.deserialize_json(content)

    @staticmethod
    def get_json_content(filename: str) -> str:
        try:
            with open(filename, "r") as file:
                return file.read()
        except (FileNotFoundError, OSError):
            print("\n***** ERROR : JSON file was not found.\n")
            return "[]"

    @staticmethod
    def deserialize_json(json_content: str) -> List[Record]:
        return json.loads(json_content)


class InvoiceMapper:
    def create_invoice(self, record: Record) -> Invoice:
        invoice = Invoice(
            record['client'],
            self.create_country(record['country']), int(record['id'])
        )
        purchased_books = [
            PurchasedBook(
                self.create_book(book),
                book['quantity']
            ) for book in record['booksInBasket']
        ]
        invoice.add_purchased_books(purchased_books)
        return invoice

    @staticmethod
    def create_country(record) -> Country:
        return Country(record['name'], Currency[record['currency']], Language[record['language']])

    def create_book(self, book: Dict) -> Book:
        author = self.create_author(book['author'])
        if 'category' in book and book['category'] is not None:
            return EducationalBook(
                book['name'], book['price'], author,
                Language[book['language']], Category[book['category']]
            )
        else:
            return Novel(
                book['name'], book['price'], author,
                Language[book['language']], [Genre[genre] for genre in book.get('_genre', [])]
            )

    def create_author(self, author: Dict) -> Author:
        return Author(author['name'], self.create_country(author['nationality']))


class JsonRepository(Repository):
    def __init__(self):
        self.loader = JsonLoader()
        self.mapper = InvoiceMapper()
        self.invoices: Dict[int, Invoice] = {}
        self.load_json_data()

    def get_invoice_map(self) -> Dict[int, Invoice]:
        return self.invoices

    def load_json_data(self) -> None:
        filename = os.path.join(os.getcwd(), "src/book_invoicing/repository.json")
        records = self.loader.load(filename)

        for record in records:
            invoice = self.mapper.create_invoice(record)
            self.add_invoice(invoice)

    def add_invoice(self, invoice: Invoice) -> None:
        self.invoices[invoice.id] = invoice


class MainRepository:
    _configured_repository = None

    @classmethod
    def get_configured_repository(cls):
        if cls._configured_repository is None:
            cls._configured_repository = JsonRepository()
        return cls._configured_repository

    @classmethod
    def override(cls, new_repository):
        """
        Override the current repository with a new one.
        For testing purposes only.
        """
        cls._configured_repository = new_repository

    @classmethod
    def reset(cls):
        """
        Reset the repository to the default JsonRepository.
        For testing purposes only.
        """
        cls._configured_repository = JsonRepository()
