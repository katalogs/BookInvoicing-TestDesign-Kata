from src.book_invoicing.domain.book import Book
from src.book_invoicing.domain.country import Country
from src.book_invoicing.domain.finance import TaxRule
from src.book_invoicing.id_generator import IdGenerator


class PurchasedBook:
    def __init__(self, book: Book, quantity: int):
        self.book = book
        self.quantity = quantity

    @property
    def total_price(self) -> float:
        return self.book.price * self.quantity

    def __str__(self):
        return (f"PurchasedBook [ Book: '{self.book}', "
                f"Quantity: '{self.quantity}' ]")

    def __eq__(self, other):
        if not isinstance(other, PurchasedBook):
            return False
        return (self.book == other.book and
                self.quantity == other.quantity)

    def __hash__(self):
        return hash((self.book, self.quantity))


class Invoice:
    _purchased_books: [PurchasedBook]
    _country: Country
    _client_name: str

    def __init__(self, client_name: str, country: Country, invoice_id=None):
        self._id = invoice_id if invoice_id is not None else IdGenerator.next_id()
        self._client_name = client_name
        self._country = country
        self._purchased_books = []  # List of PurchasedBook instances

    @property
    def id(self) -> int:
        return self._id

    @property
    def client_name(self):
        return self._client_name

    @property
    def country(self):
        return self._country

    @property
    def purchased_books(self):
        return self._purchased_books

    def add_purchased_books(self, books: [PurchasedBook]):
        self.purchased_books.extend(books)

    def add_purchased_book(self, book):
        self.purchased_books.append(book)

    def compute_total_amount(self):
        total_amount = sum(book.total_price * TaxRule.get_applicable_rate(self.country, book.book)
                           for book in self.purchased_books)
        return total_amount

    def __str__(self):
        return (f"Invoice [ Id: '{self.id}', "
                f"ClientName: '{self.client_name}', "
                f"Country: '{self.country}', "
                f"PurchasedBooks: '{self.purchased_books}' ]")

    def __eq__(self, other):
        if not isinstance(other, Invoice):
            return False
        return (self.id == other.id and
                self.client_name == other.client_name and
                self.country == other.country and
                self.purchased_books == other.purchased_books)

    def __hash__(self) -> int:
        return hash((self.id, self.client_name, self.country, tuple(self.purchased_books)))
