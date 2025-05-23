package report

import (
	"book_invoicing/finance"
	"book_invoicing/storage"
)

type Generator struct {
	repository storage.Repository
}

func NewReportGenerator(repo storage.Repository) *Generator {
	return &Generator{repository: repo}
}

func (r Generator) GetTotalAmount() float64 {
	invoiceMap := r.repository.GetInvoiceMap()
	var totalAmount float64 = 0.0

	for _, invoice := range invoiceMap {
		totalAmount += finance.ToUSD(invoice.ComputeTotalAmount(), invoice.Country.Currency)
	}

	return r.getRoundedAmount(totalAmount)
}

func (r Generator) getRoundedAmount(totalAmount float64) float64 {
	return float64(int(totalAmount*100.0)) / 100
}

func (r Generator) GetTotalSoldBooks() int {
	invoiceMap := r.repository.GetInvoiceMap()
	var totalSoldBooks int = 0

	for _, invoice := range invoiceMap {
		for _, purchasedBook := range invoice.PurchasedBooks {
			totalSoldBooks += purchasedBook.Quantity
		}
	}

	return totalSoldBooks
}

func (r Generator) GetNumberOfIssuedInvoices() int {
	invoiceMap := r.repository.GetInvoiceMap()
	return len(invoiceMap)
}
