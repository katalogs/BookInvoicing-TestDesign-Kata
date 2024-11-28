from src.book_invoicing.domain.book import Novel
from src.book_invoicing.domain.country import Currency, Language


class CurrencyConverter:
    exchange_rate = {
        Currency.US_DOLLAR: 1.0,
        Currency.EURO: 1.14,
        Currency.POUND_STERLING: 1.27,
        Currency.RENMINBI: 0.15,
        Currency.YEN: 0.0093,
        Currency.AUSTRALIAN_DOLLAR: 0.7
    }

    @staticmethod
    def from_usd(input_amount, currency) -> float:
        return input_amount / CurrencyConverter.exchange_rate[currency]

    @staticmethod
    def to_usd(input_amount, currency) -> float:
        return input_amount * CurrencyConverter.exchange_rate[currency]


class TaxRule:
    tax_rates = {
        "USA": 1.15,
        "France": 1.25,
        "UK": 1.20,
        "Spain": 1.10,
        "China": 1.35,
        "Japan": 1.30,
        "Australia": 1.13,
        "Germany": 1.22,
    }

    @staticmethod
    def get_applicable_rate(invoice_country, book):
        if invoice_country.name == "Germany":
            if book.author.nationality.name == "Germany":
                return 1.05

        if invoice_country.name == "USA":
            if isinstance(book, Novel):
                return TaxRule.get_tax_rate(invoice_country.name) * 0.98

        if invoice_country.name == "UK":
            if isinstance(book, Novel):
                return TaxRule.get_tax_rate(invoice_country.name) * 0.93

        if invoice_country.name == "China":
            if book.language != Language.MANDARIN:
                return 1

        if invoice_country.name == "Spain":
            if book.language != Language.SPANISH:
                return 1

        return TaxRule.get_tax_rate(invoice_country.name)

    @staticmethod
    def get_tax_rate(country):
        return TaxRule.tax_rates[country]
