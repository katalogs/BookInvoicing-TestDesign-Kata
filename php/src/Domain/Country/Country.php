<?php

namespace Katalogs\BookInvoicing\Domain\Country;

class Country
{
    public function __construct(
        public readonly string   $name,
        public readonly Currency $currency,
        public readonly Language $language
    ) { }
}