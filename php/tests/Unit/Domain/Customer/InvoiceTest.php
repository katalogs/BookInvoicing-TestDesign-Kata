<?php

namespace Tests\Katalogs\BookInvoicing\Unit\Domain\Customer;

use Katalogs\BookInvoicing\Domain\Books\Author;
use Katalogs\BookInvoicing\Domain\Books\Genre;
use Katalogs\BookInvoicing\Domain\Books\Novel;
use Katalogs\BookInvoicing\Domain\Country\Country;
use Katalogs\BookInvoicing\Domain\Country\Currency;
use Katalogs\BookInvoicing\Domain\Country\Language;
use Katalogs\BookInvoicing\Domain\Purchase\Invoice;
use Katalogs\BookInvoicing\Domain\Purchase\PurchasedBook;
use PHPUnit\Framework\Assert;
use PHPUnit\Framework\TestCase;

class InvoiceTest extends TestCase
{
    /**
     * @test
     * @return void
     */
    public function should_apply_tax_rules_when_computing_total_amount(): void
    {
        $book = new Novel(
            "Beautiful novel", 50,
            new Author('An author', new Country('USA', Currency::Dollar, Language::English)),
            Language::English, Genre::Mystery
        );

        $purchase = new PurchasedBook($book, 1);

        $invoice = new Invoice(
            'John Doe',
            new Country('USA', Currency::Dollar, Language::English)
        );

        $invoice->addPurchase($purchase);

        Assert::assertEquals(56.35, $invoice->computeTotalAmount());


    }
}
