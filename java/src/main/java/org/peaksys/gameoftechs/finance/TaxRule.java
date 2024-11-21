package org.peaksys.gameoftechs.finance;

import org.peaksys.gameoftechs.domain.book.Book;
import org.peaksys.gameoftechs.domain.book.Novel;
import org.peaksys.gameoftechs.domain.country.Country;
import org.peaksys.gameoftechs.domain.country.Language;

import java.util.Map;

public final class TaxRule {

    private static final Map<String, Double> TAX_RATES = Map.of(
            "USA", 1.15d,
            "France", 1.25d,
            "UK", 1.20d,
            "Spain", 1.10d,
            "China", 1.35d,
            "Japan", 1.30d,
            "Australia", 1.13d,
            "Germany", 1.22d
    );

    public static double getApplicableRate(Country invoiceCountry, Book book) {
        if (invoiceCountry.name().equals("Germany")) {
            if (book.author().nationality().name().equals("Germany")) {
                return 1.05;
            }
        }
        if (invoiceCountry.name().equals("USA")) {
            if (book.getClass().equals(Novel.class)) {
                return getTaxRate(invoiceCountry.name()) * 0.98;
            }
        }
        if (invoiceCountry.name().equals("UK")) {
            if (book.getClass().equals(Novel.class)) {
                return getTaxRate(invoiceCountry.name()) * 0.93;
            }
        }
        if (invoiceCountry.name().equals("China")) {
            if (!book.language().equals(Language.MANDARIN)) {
                return 1d;
            }
        }
        if (invoiceCountry.name().equals("Spain")) {
            if (!book.language().equals(Language.SPANISH)) {
                return 1d;
            }
        }
        return getTaxRate(invoiceCountry.name());
    }

    private static double getTaxRate(String country) {
        return TAX_RATES.get(country);
    }
}
