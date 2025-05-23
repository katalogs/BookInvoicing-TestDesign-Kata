package finance

import (
	. "book_invoicing/domain/book"
	. "book_invoicing/domain/country"
)

var taxRates = map[string]float64{
	"USA":       1.15,
	"France":    1.25,
	"UK":        1.2,
	"Spain":     1.1,
	"China":     1.35,
	"Japan":     1.3,
	"Australia": 1.13,
	"Germany":   1.22,
}

func getTaxRate(countryName string) float64 {
	rate, ok := taxRates[countryName]
	if !ok {
		panic("Unhandled country name: " + countryName)
	}
	return rate
}

func GetApplicableRate(invoiceCountry Country, book Book) float64 {
	switch invoiceCountry.Name {
	case "Germany":
		if book.GetAuthor().Nationality.Name == "Germany" {
			return 1.05
		}
	case "USA":
		if IsNovel(book) {
			return getTaxRate(invoiceCountry.Name) * 0.98
		}
	case "UK":
		if IsNovel(book) {
			return getTaxRate(invoiceCountry.Name) * 0.93
		}
	case "China":
		if book.GetLanguage() != Mandarin {
			return 1.0
		}
	case "Spain":
		if book.GetLanguage() != Spanish {
			return 1.0
		}
	}
	return getTaxRate(invoiceCountry.Name)
}
