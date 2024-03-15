<?php

namespace Katalogs\BookInvoicing\Domain\Books;

interface Book
{
    public function getAuthor(): Author;
}