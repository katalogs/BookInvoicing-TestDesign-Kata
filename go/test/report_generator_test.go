package test

import (
	. "book_invoicing/domain/book"
	. "book_invoicing/domain/country"
	. "book_invoicing/purchase"
	"book_invoicing/report"
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestReportGenerator_ComputesTotals(t *testing.T) {

	var repo = NewInMemoryRepository()

	generator := report.NewReportGenerator(&repo)

	book := NewEducationalBook(
		"Clean Code",
		25,
		Author{
			Name: "Uncle Bob",
			Nationality: Country{
				Name:     "USA",
				Currency: Dollar,
				Language: English,
			},
		},
		English,
		Computer,
	)

	purchase := NewPurchasedBook(book, 2)

	invoice := NewInvoice("John Doe", Country{
		Name:     "USA",
		Currency: Dollar,
		Language: English,
	})
	invoice.AddPurchasedBook(purchase)

	repo.AddInvoice(invoice)

	assert.InDelta(t, 57.49, generator.GetTotalAmount(), 0.001)
	assert.Equal(t, 1, generator.GetNumberOfIssuedInvoices())
	assert.Equal(t, 2, generator.GetTotalSoldBooks())
}
