<?php

namespace Katalogs\BookInvoicing\Domain\Country;

enum Currency: string
{
    case Dollar = 'USD';
    case AustralianDollar = 'AUD';
    case Euro = 'EUR';
    case PoundSterling = 'GBP';
    case Yen = 'JPY';
    case Renminbi = 'CNY';
}