package org.peaksys.gameoftechs.finance;

import org.peaksys.gameoftechs.domain.country.Currency;

import java.util.HashMap;
import java.util.Map;

import static org.peaksys.gameoftechs.domain.country.Currency.*;

public final class CurrencyConverter {

    private static final Map<Currency, Double> EXCHANGE_RATE = new HashMap<>() {
        {
            put(US_DOLLAR, 1.0d);
            put(EURO, 1.14d);
            put(POUND_STERLING, 1.27d);
            put(RENMINBI, 0.15d);
            put(YEN, 0.0093d);
            put(AUSTRALIAN_DOLLAR, 0.7d);
        }
    };

    public static double fromUSD(double input, Currency currency) {
        return input / EXCHANGE_RATE.get(currency);
    }

    public static double toUSD(double input, Currency currency) {
        return input * EXCHANGE_RATE.get(currency);
    }
}
