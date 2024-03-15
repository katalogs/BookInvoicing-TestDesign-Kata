<?php

namespace Katalogs\BookInvoicing\Domain\Purchase;

use Katalogs\BookInvoicing\Domain\Books\Book;

class PurchasedBook
{
    public function __construct(
        public readonly Book $book,
        public readonly int $quantity
    ) { }

    public function totalPrice(): float
    {
        return $this->book->price * $this->quantity;
    }
}