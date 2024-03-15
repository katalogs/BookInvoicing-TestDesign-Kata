<?php

namespace Tests\Katalogs\BookInvoicing\Fixtures;

use Katalogs\BookInvoicing\Domain\Purchase\Invoice;
use Katalogs\BookInvoicing\Domain\Purchase\Repository;

class InMemoryRepository implements Repository
{
    private array $invoices = [];

    public function __construct()
    {
    }

    public function addInvoice(Invoice $invoice): void
    {
        $this->invoices[] = $invoice;
    }

    public function getInvoices(): array
    {
        return $this->invoices;
    }
}