from enum import StrEnum


class Currency(StrEnum):
    US_DOLLAR = "UsDollar"
    AUSTRALIAN_DOLLAR = "AustralianDollar"
    EURO = "Euro"
    POUND_STERLING = "PoundSterling"
    YEN = "Yen"
    RENMINBI = "Renminbi"


class Language(StrEnum):
    ENGLISH = "English"
    FRENCH = "French"
    SPANISH = "Spanish"
    JAPANESE = "Japanese"
    MANDARIN = "Mandarin"
    ARABIC = "Arabic"
    GERMAN = "German"


class Country:
    def __init__(self, name, currency, language):
        self._name = name
        self._currency = currency
        self._language = language

    @property
    def name(self) -> str:
        return self._name

    @property
    def currency(self) -> Currency:
        return self._currency

    @property
    def language(self) -> Language:
        return self._language

    def __str__(self):
        return f"Country [ Name: '{self.name}', Currency: '{self.currency}', Language: '{self.language}' ]"

    def __eq__(self, other):
        if not isinstance(other, Country):
            return False
        return self.name == other.name and self.currency == other.currency and self.language == other.language

    def __hash__(self):
        return
