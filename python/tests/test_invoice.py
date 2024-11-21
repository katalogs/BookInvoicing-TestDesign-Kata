import pytest
from src.book_invoicing.domain.book import Novel, Author, Genre
from src.book_invoicing.domain.country import Country, Currency, Language
from src.book_invoicing.domain.purchase import PurchasedBook, Invoice


class TestInvoice:
    def test_should_apply_tax_rules_when_computing_total_amount(self):
        book = Novel(
            "A mysterious adventure fiction",
            50,
            Author("Some Guy", Country("France", Currency.EURO, Language.FRENCH)),
            Language.ENGLISH,
            [Genre.MYSTERY, Genre.ADVENTURE_FICTION]
        )
        invoice = Invoice("John Doe", Country("USA", Currency.US_DOLLAR, Language.ENGLISH))

        invoice.add_purchased_book(PurchasedBook(book, 1))

        # Assert the total amount of the invoice is 56.35 : 15% of taxes plus a 2% reduction on novels
        assert invoice.compute_total_amount() == pytest.approx(56.35, rel=1e-2)
