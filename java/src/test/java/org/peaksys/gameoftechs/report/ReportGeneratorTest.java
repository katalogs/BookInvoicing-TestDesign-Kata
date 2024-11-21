package org.peaksys.gameoftechs.report;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.peaksys.gameoftechs.MainRepository;
import org.peaksys.gameoftechs.domain.book.*;
import org.peaksys.gameoftechs.domain.country.Country;
import org.peaksys.gameoftechs.domain.country.Currency;
import org.peaksys.gameoftechs.domain.country.Language;
import org.peaksys.gameoftechs.purchase.Invoice;
import org.peaksys.gameoftechs.purchase.PurchasedBook;
import org.peaksys.gameoftechs.storage.InMemoryRepository;

import java.util.Arrays;
import java.util.Collections;

import static org.assertj.core.api.Assertions.assertThat;

class ReportGeneratorTest {
    private InMemoryRepository inMemoryRepository;

    @BeforeEach
    void setUp() {
        this.inMemoryRepository = new InMemoryRepository();
        MainRepository.override(this.inMemoryRepository);
    }

    @AfterEach
    void tearDown() {
        MainRepository.reset();
    }

    @Test
    void ShouldComputeTotalAmount_WithoutTaxRate_WithoutDiscount() {
        // Arrange
        ReportGenerator generator = new ReportGenerator();

        var book = new EducationalBook(
                "Clean Code",
                25,
                new Author(
                        "Uncle Bob",
                        new Country(
                                "USA",
                                Currency.US_DOLLAR,
                                Language.ENGLISH
                        )
                ),
                Language.ENGLISH,
                Category.COMPUTER
        );

        var purchasedBook = new PurchasedBook(book, 2);

        var invoice = new Invoice("John Doe", new Country("USA", Currency.US_DOLLAR, Language.ENGLISH));
        invoice.addPurchasedBooks(Collections.singletonList(purchasedBook));

        // Act
        this.inMemoryRepository.addInvoice(invoice);

        // Assert
        assertThat(generator.getTotalAmount()).isEqualTo(57.5);
        assertThat(generator.getNumberOfIssuedInvoices()).isEqualTo(1);
        assertThat(generator.getTotalSoldBooks()).isEqualTo(2);

    }

    @Test
    void ShouldComputeTotalAmount_WithExchangeRate_WithoutTax() {
        // Arrange
        ReportGenerator generator = new ReportGenerator();

        var book = new Novel(
                "A mysterious adventure fiction",
                35.5,
                new Author(
                        "Some Guy",
                        new Country(
                                "France",
                                Currency.EURO,
                                Language.FRENCH
                        )
                ),
                Language.ENGLISH,
                Arrays.asList(Genre.MYSTERY, Genre.ADVENTURE_FICTION)
        );

        var purchasedBook = new PurchasedBook(book, 3);

        var invoice = new Invoice("John Doe",
                new Country("Spain", Currency.EURO, Language.SPANISH));
        invoice.addPurchasedBooks(Collections.singletonList(purchasedBook));

        // Act
        this.inMemoryRepository.addInvoice(invoice);

        // Assert
        assertThat(generator.getTotalAmount()).isEqualTo(121.41);
        assertThat(generator.getNumberOfIssuedInvoices()).isEqualTo(1);
        assertThat(generator.getTotalSoldBooks()).isEqualTo(3);

    }
}
