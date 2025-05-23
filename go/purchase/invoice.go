package purchase

import (
	. "book_invoicing/domain/country"
	. "book_invoicing/finance"
	. "book_invoicing/service"
)

type Invoice struct {
	ID             int64
	ClientName     string
	Country        Country
	PurchasedBooks []PurchasedBook
}

func NewInvoice(clientName string, country Country, id ...int64) *Invoice {
	invoiceID := NextID()
	if len(id) > 0 {
		invoiceID = id[0]
	}
	return &Invoice{
		ID:             invoiceID,
		ClientName:     clientName,
		Country:        country,
		PurchasedBooks: []PurchasedBook{},
	}
}

func (i *Invoice) AddPurchasedBook(purchasedBook PurchasedBook) {
	i.PurchasedBooks = append(i.PurchasedBooks, purchasedBook)
}

func (i *Invoice) AddPurchasedBooks(purchasedBooks []PurchasedBook) {
	for _, pb := range purchasedBooks {
		i.AddPurchasedBook(pb)
	}
}

func (i *Invoice) ComputeTotalAmount() float64 {
	var sum float64
	for _, pb := range i.PurchasedBooks {
		totalPrice := pb.TotalPrice() * GetApplicableRate(i.Country, pb.Book)
		sum += totalPrice
	}
	return sum
}
