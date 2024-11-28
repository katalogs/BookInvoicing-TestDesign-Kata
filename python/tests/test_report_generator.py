import pytest

from src.book_invoicing.domain.book import Genre, Author, Novel, Category, EducationalBook
from src.book_invoicing.domain.country import Language, Currency, Country
from src.book_invoicing.domain.purchase import Invoice, PurchasedBook
from src.book_invoicing.report_generator import ReportGenerator  # Assuming ReportGenerator is defined in report module
from src.book_invoicing.storage import MainRepository
from tests.in_memory_repository import InMemoryRepository


class TestReportGenerator:

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        self.in_memory_repository = InMemoryRepository()
        self.original_repository = MainRepository.get_configured_repository()
        MainRepository.override(self.in_memory_repository)

        yield

        # Teardown
        MainRepository.reset()

    def test_should_compute_total_amount_without_exchange_rate_with_tax_rate_without_discount(self):
        # Arrange
        generator = ReportGenerator()

        book = EducationalBook(
            "Clean Code", 25, Author(
                "Uncle Bob", Country("USA", Currency.US_DOLLAR, Language.ENGLISH)
            ),
            Language.ENGLISH, Category.COMPUTER
        )

        purchased_book = PurchasedBook(book, 2)

        invoice = Invoice("John Doe", Country("USA", Currency.US_DOLLAR, Language.ENGLISH))
        invoice.add_purchased_books([purchased_book])

        # Act
        self.in_memory_repository.add_invoice(invoice)

        # Assert
        assert generator.get_total_amount() == 57.5
        assert generator.get_number_of_issued_invoices() == 1
        assert generator.get_total_sold_books() == 2

    def test_should_compute_total_amount_with_exchange_rate_without_tax(self):
        # Arrange
        generator = ReportGenerator()

        book = Novel(
            "A mysterious adventure fiction", 35.5, Author(
                "Some Guy", Country("France", Currency.EURO, Language.FRENCH)
            ),
            Language.ENGLISH, [Genre.MYSTERY, Genre.ADVENTURE_FICTION]
        )

        purchased_book = PurchasedBook(book, 3)

        invoice = Invoice("John Doe", Country("Spain", Currency.EURO, Language.SPANISH))
        invoice.add_purchased_books([purchased_book])

        # Act
        self.in_memory_repository.add_invoice(invoice)

        # Assert
        assert generator.get_total_amount() == 121.41
        assert generator.get_number_of_issued_invoices() == 1
        assert generator.get_total_sold_books() == 3

