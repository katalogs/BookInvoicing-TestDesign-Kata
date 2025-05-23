package test

import (
	. "book_invoicing/purchase"
	"sync"
)

type InMemoryRepository struct {
	mu       sync.RWMutex
	invoices map[int64]*Invoice
}

func NewInMemoryRepository() InMemoryRepository {
	return InMemoryRepository{
		invoices: make(map[int64]*Invoice),
	}
}

func (r *InMemoryRepository) AddInvoice(invoice *Invoice) {
	r.invoices[invoice.ID] = invoice
}

func (r *InMemoryRepository) GetInvoiceMap() map[int64]*Invoice {
	// return a shallow cp to avoid external mutation
	cp := make(map[int64]*Invoice, len(r.invoices))
	for k, v := range r.invoices {
		cp[int64(k)] = v
	}
	return cp
}
