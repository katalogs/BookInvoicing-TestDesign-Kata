package main

import (
	"book_invoicing/report"
	"book_invoicing/storage"
	"fmt"
)

func main() {
	reportGenerator := report.NewReportGenerator(storage.NewMainRepository())

	fmt.Println("****************************************************")
	fmt.Println("*****************Application Report*****************")
	fmt.Println("****************************************************")
	fmt.Println()
	fmt.Println("The total number of books sold is:", reportGenerator.GetTotalSoldBooks())
	fmt.Println("The total number of issued invoices is:", reportGenerator.GetNumberOfIssuedInvoices())
	fmt.Println("The total amount of all invoices in USD is:", reportGenerator.GetTotalAmount())
	fmt.Println()
	fmt.Println("****************************************************")
	fmt.Println("****************************************************")
}
