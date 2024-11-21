from src.book_invoicing.domain.finance import CurrencyConverter
from src.book_invoicing.storage import MainRepository  # Assurez-vous que le module storage contient MainRepository


class ReportGenerator:
    def __init__(self):
        self._repository = MainRepository.get_configured_repository()

    def get_total_amount(self):
        invoices = self._repository.get_invoice_map().values()
        total_amount = sum(
            CurrencyConverter.to_usd(invoice.compute_total_amount(), invoice.country.currency)
            for invoice in invoices
        )
        return self.get_rounded_amount(total_amount)

    def get_total_sold_books(self):
        invoices = self._repository.get_invoice_map().values()
        total_sold_books = sum(
            sum(purchased_book.quantity for purchased_book in invoice.purchased_books)
            for invoice in invoices
        )
        return total_sold_books

    def get_rounded_amount(self, total_amount):
        return round(total_amount, 2)

    def get_number_of_issued_invoices(self):
        return len(self._repository.get_invoice_map())
