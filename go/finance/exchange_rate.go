package finance

import (
	. "book_invoicing/domain/country"
	"errors"
)

var exchangeRates = map[Currency]float64{
	Euro:             1.14,
	Dollar:           1.0,
	PoundSterling:    1.27,
	Renminbi:         0.15,
	Yen:              0.0093,
	AustralianDollar: 0.7,
}

func getExchangeRateOrThrow(currency Currency) float64 {
	rate, ok := exchangeRates[currency]
	if !ok {
		panic(errors.New("Unexpected currency: " + currency.String()))
	}
	return rate
}

func FromUSD(input float64, currency Currency) float64 {
	exchangeRate := getExchangeRateOrThrow(currency)
	return input / exchangeRate
}

func ToUSD(input float64, currency Currency) float64 {
	exchangeRate := getExchangeRateOrThrow(currency)
	return input * exchangeRate
}
