package storage

import (
	. "book_invoicing/domain/book"
	. "book_invoicing/domain/country"
	. "book_invoicing/purchase"
	"encoding/json"
	"fmt"
	"os"
)

type Repository interface {
	AddInvoice(invoice *Invoice)
	GetInvoiceMap() map[int64]*Invoice
}

type JsonRepository struct {
	invoices map[int64]*Invoice
}

func NewJsonRepository() *JsonRepository {
	repo := &JsonRepository{
		invoices: make(map[int64]*Invoice),
	}
	repo.loadJsonData()
	return repo
}

func (r *JsonRepository) AddInvoice(invoice *Invoice) {
	r.invoices[invoice.ID] = invoice
}

func (r *JsonRepository) GetInvoiceMap() map[int64]*Invoice {
	return r.invoices
}

func (r *JsonRepository) loadJsonData() {

	data, err := os.ReadFile("repository.json")

	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	var jsonInvoices []map[string]interface{}
	if err := json.Unmarshal(data, &jsonInvoices); err != nil {
		fmt.Println("Error unmarshalling JSON:", err)
		return
	}

	for _, jsonInvoice := range jsonInvoices {
		country := toCountry(jsonInvoice["country"].(map[string]interface{}))
		invoice := NewInvoice(jsonInvoice["client"].(string), *country, int64(jsonInvoice["id"].(float64)))

		booksInBasket := jsonInvoice["booksInBasket"].([]interface{})
		for _, jsonPurchasedBook := range booksInBasket {
			purchasedBookData := jsonPurchasedBook.(map[string]interface{})
			authorData := purchasedBookData["author"].(map[string]interface{})
			author := NewAuthor(authorData["name"].(string), *toCountry(authorData["nationality"].(map[string]interface{})))

			var book Book
			if genreData, exists := purchasedBookData["genre"]; exists {
				var genres map[int64]Genre = make(map[int64]Genre)
				for _, jsonGenre := range genreData.([]interface{}) {
					genres[int64(len(genres))] = toGenre(jsonGenre.(string))
				}
				book = NewNovel(purchasedBookData["name"].(string), purchasedBookData["price"].(float64), *author, toLanguage(purchasedBookData["language"].(string)), genres)
			} else {
				book = NewEducationalBook(purchasedBookData["name"].(string), purchasedBookData["price"].(float64), *author, toLanguage(purchasedBookData["language"].(string)), toCategory(purchasedBookData["category"].(string)))
			}

			purchasedBook := NewPurchasedBook(book, int(purchasedBookData["quantity"].(float64)))
			invoice.AddPurchasedBook(purchasedBook)
		}

		r.AddInvoice(invoice)
	}
}

func toCountry(data map[string]interface{}) *Country {
	return NewCountry(
		data["name"].(string),
		toCurrency(data["currency"].(string)),
		toLanguage(data["language"].(string)),
	)
}

func toLanguage(language string) Language {
	switch language {
	case "ARABIC":
		return Arabic
	case "ENGLISH":
		return English
	case "FRENCH":
		return French
	case "GERMAN":
		return German
	case "JAPANESE":
		return Japanese
	case "MANDARIN":
		return Mandarin
	case "SPANISH":
		return Spanish
	default:
		panic("Unhandled language name: " + language)
	}
}

func toCurrency(currency string) Currency {
	switch currency {
	case "US_DOLLAR":
		return Dollar
	case "EURO":
		return Euro
	case "RENMINBI":
		return Renminbi
	case "POUND_STERLING":
		return PoundSterling
	case "AUSTRALIAN_DOLLAR":
		return AustralianDollar
	case "YEN":
		return Yen
	default:
		panic("Unhandled currency name: " + currency)
	}
}

func toCategory(category string) Category {
	switch category {
	case "BUSINESS":
		return Business
	case "COMPUTER":
		return Computer
	case "LANGUAGE":
		return Languages
	default:
		panic("Unhandled category name: " + category)
	}
}

func toGenre(genre string) Genre {
	switch genre {
	case "HORROR_FICTION":
		return HorrorFiction
	case "THRILLER":
		return Thriller
	case "DARK_FANTASY":
		return DarkFantasy
	case "MYSTERY":
		return Mystery
	case "ADVENTURE_FICTION":
		return AdventureFiction
	case "NON_FICTION":
		return NonFiction
	case "ROMANCE":
		return Romance
	default:
		panic("Unhandled genre name: " + genre)
	}
}
