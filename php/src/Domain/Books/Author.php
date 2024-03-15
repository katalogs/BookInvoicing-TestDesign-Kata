<?php

namespace Katalogs\BookInvoicing\Domain\Books;

use Katalogs\BookInvoicing\Domain\Country\Country;

class Author
{
    public function __construct(
        public readonly string  $name,
        public readonly Country $nationality
    ) { }
}