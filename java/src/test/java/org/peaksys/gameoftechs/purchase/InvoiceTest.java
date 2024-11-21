package org.peaksys.gameoftechs.purchase;

import org.junit.jupiter.api.Test;
import org.peaksys.gameoftechs.domain.book.Author;
import org.peaksys.gameoftechs.domain.book.Genre;
import org.peaksys.gameoftechs.domain.book.Novel;
import org.peaksys.gameoftechs.domain.country.Country;
import org.peaksys.gameoftechs.domain.country.Currency;
import org.peaksys.gameoftechs.domain.country.Language;

import java.util.Arrays;

import static org.assertj.core.api.Assertions.assertThat;

class InvoiceTest {

    @Test
    void Should_apply_tax_rules_when_computing_total_amount() {
        var book = new Novel("A mysterious adventure fiction",
                50,
                new Author(
                        "Some Guy",
                        new Country(
                                "France",
                                Currency.EURO,
                                Language.FRENCH
                        )
                ),
                Language.ENGLISH,
                Arrays.asList(Genre.MYSTERY,
                        Genre.ADVENTURE_FICTION)
        );

        var purchasedBook = new PurchasedBook(book, 1);
        var invoice = new Invoice("John Doe", new Country("USA", Currency.US_DOLLAR, Language.ENGLISH));

        invoice.addPurchasedBook(purchasedBook);

        assertThat(invoice.computeTotalAmount()).isEqualTo(56.35);
    }

}
