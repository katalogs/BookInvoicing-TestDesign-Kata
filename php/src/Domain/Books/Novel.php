<?php

namespace Katalogs\BookInvoicing\Domain\Books;

use Katalogs\BookInvoicing\Domain\Country\Language;

class Novel implements Book
{

    public function __construct(
        public readonly string $name,
        public readonly float $price,
        public readonly Author $author,
        public readonly Language $language,
        Genre ...$genres
    ) { }

    public function getAuthor(): Author
    {
        return $this->author;
    }
}