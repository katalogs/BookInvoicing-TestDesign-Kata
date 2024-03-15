<?php

namespace Tests\Katalogs\BookInvoicing\Unit\Domain\Reporting;

use Katalogs\BookInvoicing\Domain\Books\Author;
use Katalogs\BookInvoicing\Domain\Books\Category;
use Katalogs\BookInvoicing\Domain\Books\EducationalBook;
use Katalogs\BookInvoicing\Domain\Country\Country;
use Katalogs\BookInvoicing\Domain\Country\Currency;
use Katalogs\BookInvoicing\Domain\Country\Language;
use Katalogs\BookInvoicing\Domain\Purchase\Invoice;
use Katalogs\BookInvoicing\Domain\Purchase\MainRepository;
use Katalogs\BookInvoicing\Domain\Purchase\PurchasedBook;
use Katalogs\BookInvoicing\Domain\Reporting\ReportGenerator;
use PHPUnit\Framework\Assert;
use PHPUnit\Framework\TestCase;
use Tests\Katalogs\BookInvoicing\Fixtures\InMemoryRepository;

class ReportGeneratorTest extends TestCase
{
    /**
     * @test
     * @return void
     */
    public function should_compute_total_amount_without_discount_and_without_tax_rate()
    {
        $repository = new InMemoryRepository();
        MainRepository::override($repository);

        $generator = new ReportGenerator();

        $book = new EducationalBook(
            'Clean code', 25,
            new Author('Uncle Bob', new Country('USA', Currency::Dollar, Language::English)),
            Language::English, Category::Computer
        );

        $purchase = new PurchasedBook($book, 2);

        $invoice = new Invoice(
            'John Doe',
            new Country('USA', Currency::Dollar, Language::English)
        );

        $invoice->addPurchase($purchase);

        $repository->addInvoice($invoice);

        Assert::assertEquals(57.5, $generator->getTotalAmount());
        Assert::assertEquals(1, $generator->getNumberOfIssuedInvoices());
        Assert::assertEquals(2, $generator->getTotalSoldBooks());

        MainRepository::reset();
    }

}
