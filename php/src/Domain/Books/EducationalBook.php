<?php

namespace Katalogs\BookInvoicing\Domain\Books;

use Katalogs\BookInvoicing\Domain\Country\Language;

class EducationalBook implements Book
{
    public function __construct(
        public readonly string   $name,
        public readonly float    $price,
        public readonly Author   $author,
        public readonly Language $language,
        public readonly Category $category
    ) {}

    public function getAuthor(): Author
    {
        return $this->author;
    }
}