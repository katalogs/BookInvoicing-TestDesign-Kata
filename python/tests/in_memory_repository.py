from typing import Dict
from src.book_invoicing.domain.purchase import Invoice
from src.book_invoicing.domain.repository import Repository


class InMemoryRepository(Repository):
    def __init__(self):
        self._invoice_map: Dict[int, Invoice] = {}

    def add_invoice(self, invoice: Invoice):
        self._invoice_map[invoice.id] = invoice

    def get_invoice_map(self) -> Dict[int, Invoice]:
        return self._invoice_map
