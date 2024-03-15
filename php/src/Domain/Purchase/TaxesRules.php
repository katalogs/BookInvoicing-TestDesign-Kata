<?php

namespace Katalogs\BookInvoicing\Domain\Purchase;

use InvalidArgumentException;
use Katalogs\BookInvoicing\Domain\Books\Book;
use Katalogs\BookInvoicing\Domain\Books\Novel;
use Katalogs\BookInvoicing\Domain\Country\Country;
use Katalogs\BookInvoicing\Domain\Country\Language;

class TaxesRules
{

    const TaxRates = [
        'USA' => 1.15,
        'France' => 1.25,
        'UK' => 1.2,
        'Spain' =>1.1,
        'China' => 1.35,
        'Japan' => 1.3,
        'Australia' => 1.13,
        'Germany' => 1.22,
    ];

    public static function getApplicableRate(Country $country, Book $book): float
    {
        if ($country->name == 'Germany' && $book->author->nationality->name == 'Germany') {
            return 1.05;
        }

        if ($country->name == 'USA' && $book instanceof Novel) {
            return self::getTaxRate($country->name) * 0.98;
        }

        if ($country->name == 'UK' && $book instanceof Novel) {
            return self::getTaxRate($country->name) * 0.93;
        }

        if ($country->name == 'China' && $book->language != Language::Mandarin) {
            return 1;
        }

        if ($country->name == 'Spain' && $book->language != Language::Spanish) {
            return 1;
        }

        return self::getTaxRate($country->name);
    }

    private static function getTaxRate(string $name): float
    {
        if (array_key_exists($name, self::TaxRates)) {
            return self::TaxRates[$name];
        }
        throw new InvalidArgumentException("Unhandled country name $name");
    }
}