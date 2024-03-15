<?php

namespace Katalogs\BookInvoicing\Domain\Reporting;

use Katalogs\BookInvoicing\Domain\Finance\CurrencyConverter;
use Katalogs\BookInvoicing\Domain\Purchase\Invoice;
use Katalogs\BookInvoicing\Domain\Purchase\MainRepository;
use Katalogs\BookInvoicing\Domain\Purchase\PurchasedBook;
use Katalogs\BookInvoicing\Domain\Purchase\Repository;

class ReportGenerator
{
    private readonly Repository $repository;

    public function __construct()
    {
        $this->repository = MainRepository::configuredRepository();
    }

    public function getTotalAmount(): float {
        $invoices = $this->repository->getInvoices();
        $totalAmount = 0.0;

        /** @var Invoice $invoice */
        foreach ($invoices as $invoice) {
            $totalAmount += CurrencyConverter::toUSD(
                $invoice->computeTotalAmount(),
                $invoice->country->currency
            );
        }
        return $this->getRoundedAmount($totalAmount);
    }

    private function getRoundedAmount(float $totalAmount): float
    {
        return round($totalAmount * 100) / 100;
    }

    public function getTotalSoldBooks(): float {
        $invoices = $this->repository->getInvoices();
        $totalSoldBooks = 0;

        /** @var Invoice $invoice */
        foreach ($invoices as $invoice) {
            /** @var PurchasedBook $purchasedBook */
            foreach ($invoice->getPurchasedBooks() as $purchasedBook) {
                $totalSoldBooks = $totalSoldBooks + $purchasedBook->quantity;
            }
        }
        return $totalSoldBooks;
    }

    public function getNumberOfIssuedInvoices(): int {
        $invoices = $this->repository->getInvoices();
        return count($invoices);
    }
}