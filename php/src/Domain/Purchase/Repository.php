<?php

namespace Katalogs\BookInvoicing\Domain\Purchase;

interface Repository
{
    public function addInvoice(Invoice $invoice): void;

    public function getInvoices(): array;
}