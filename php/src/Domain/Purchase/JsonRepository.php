<?php

namespace Katalogs\BookInvoicing\Domain\Purchase;

class JsonRepository implements Repository
{

    public function __construct()
    {
    }

    public function addInvoice(Invoice $invoice): void
    {
        // TODO: Implement addInvoice() method.
    }

    public function getInvoices(): array
    {
        return [];
    }
}