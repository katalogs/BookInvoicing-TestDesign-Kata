package book

import . "book_invoicing/domain/country"

type Author struct {
	Name        string
	Nationality Country
}

func NewAuthor(name string, nationality Country) *Author {
	return &Author{Name: name, Nationality: nationality}
}
