from abc import ABC, abstractmethod
from typing import Dict
from src.book_invoicing.domain.purchase import Invoice


class Repository(ABC):
    @abstractmethod
    def add_invoice(self, invoice: Invoice) -> None:
        pass

    @abstractmethod
    def get_invoice_map(self) -> Dict[int, Invoice]:
        pass
