package country

type Country struct {
	Name     string
	Currency Currency
	Language Language
}

func NewCountry(name string, currency Currency, language Language) *Country {
	return &Country{Name: name, Currency: currency, Language: language}
}
