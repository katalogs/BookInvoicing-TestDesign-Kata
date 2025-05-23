package storage

import (
	. "book_invoicing/purchase"
	"sync"
)

var (
	runningRepository Repository
	repoOnce          sync.Once
)

type MainRepository struct{}

func (m *MainRepository) AddInvoice(invoice *Invoice) {
	m.ConfiguredRepository().AddInvoice(invoice)
}

func (m *MainRepository) GetInvoiceMap() map[int64]*Invoice {
	return m.ConfiguredRepository().GetInvoiceMap()
}

func NewMainRepository() *MainRepository {
	return &MainRepository{}
}

func (m *MainRepository) ConfiguredRepository() Repository {
	repoOnce.Do(func() {
		runningRepository = NewJsonRepository()
	})
	return runningRepository
}

func (m *MainRepository) Override(newRepository Repository) {
	runningRepository = newRepository
}

func (m *MainRepository) Reset() {
	runningRepository = NewJsonRepository()
}
