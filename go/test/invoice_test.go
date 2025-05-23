package test

import (
	. "book_invoicing/domain/book"
	. "book_invoicing/domain/country"
	. "book_invoicing/purchase"
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestInvoice_ShouldApplyTaxRules_WhenComputingTotalAmount(t *testing.T) {
	var book = NewNovel(
		"Beautiful novel",
		50,
		Author{
			Name: "An author",
			Nationality: Country{
				Name:     "USA",
				Currency: Dollar,
				Language: English,
			},
		},
		English,
		map[int64]Genre{1: Mystery},
	)
	purchase := NewPurchasedBook(book, 1)

	invoice := NewInvoice("John Doe", Country{
		Name:     "USA",
		Currency: Dollar,
		Language: English,
	})

	invoice.AddPurchasedBook(purchase)

	assert.InDelta(t, 57.50, invoice.ComputeTotalAmount(), 0.001)
}
