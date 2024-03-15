<?php

namespace Katalogs\BookInvoicing\Domain\Finance;

use InvalidArgumentException;
use Katalogs\BookInvoicing\Domain\Country\Currency;

class CurrencyConverter
{
    private const EXCHANGE_RATES = [
        'EUR' => 1.14,
        'USD' => 1.0,
        'GBP' => 1.27,
        'CNY' => 0.15,
        'JPY' => 0.0093,
        'AUD' => 0.7,
    ];

    public static function fromUSD(float $amount, Currency $currency): float
    {
        return $amount / self::getExchangeRateOrThrow($currency);
    }

    public static function toUSD(float $amount, Currency $currency): float
    {
        return $amount * self::getExchangeRateOrThrow($currency);
    }

    private static function getExchangeRateOrThrow(Currency $currency): float
    {
        if (!array_key_exists($currency->value, self::EXCHANGE_RATES)) {
            throw new InvalidArgumentException("Unexpected currency " . $currency->value);
        }
        return self::EXCHANGE_RATES[$currency->value];
    }

}