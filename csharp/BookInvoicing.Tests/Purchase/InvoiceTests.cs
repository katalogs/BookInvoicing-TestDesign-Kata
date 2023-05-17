using System.Collections.Generic;
using BookInvoicing.Domain.Book;
using BookInvoicing.Domain.Country;
using BookInvoicing.Purchase;
using FluentAssertions;
using Xunit;

namespace BookInvoicing.Tests.Purchase;

public class InvoiceTests
{
    [Fact]
    public void Should_apply_tax_rules_when_computing_total_amount()
    {
        var book = new Novel("A mysterious adventure fiction", 50, new Author(
                "Some Guy", new Country(
                    "France", Currency.Euro, Language.French
                )
            ),
            Language.English, new List<Genre> {Genre.Mystery, Genre.AdventureFiction }
        );

        var purchasedBook = new PurchasedBook(book, 1);

        Invoice invoice = new Invoice("John Doe", new Country("USA", Currency.UsDollar, Language.English));

        invoice.AddPurchasedBook(purchasedBook);

        // Assert the total amount of the invoice is 56,35 : 15% of taxes plus a 2% reduction on novels
        invoice.ComputeTotalAmount().Should().Be(56.35);
    }
}
