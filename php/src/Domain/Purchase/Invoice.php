<?php

namespace Katalogs\BookInvoicing\Domain\Purchase;

use Katalogs\BookInvoicing\Domain\Country\Country;

class Invoice
{
    private array $purchases = [];

    public function __construct(
        public readonly string $customerName,
        public readonly Country $country
    ) {
    }

    public function addPurchase(PurchasedBook $purchase): void
    {
        $this->purchases[] = $purchase;
    }

    public function computeTotalAmount(): float
    {
        $sum = 0;
        /** @var PurchasedBook $purchase */
        foreach ($this->purchases as $purchase) {
            $sum += $purchase->totalPrice() * TaxesRules::getApplicableRate($this->country, $purchase->book);
        }
        return $sum;
    }

    public function getPurchasedBooks(): array
    {
        return $this->purchases;
    }


}