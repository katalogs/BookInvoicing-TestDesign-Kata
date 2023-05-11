using System;
using System.Collections.Generic;
using System.Linq;
using BookInvoicing.Finance;
using BookInvoicing.Purchase;
using BookInvoicing.Storage;

namespace BookInvoicing.Report
{
    public class ReportGenerator
    {
        private readonly IRepository _repository = MainRepository.ConfiguredRepository;

        public double GetTotalAmount()
        {
            var invoices = _repository.GetInvoiceMap().Values;
            var totalAmount = invoices.Sum(invoice =>
                CurrencyConverter.ToUsd(invoice.ComputeTotalAmount(), invoice.Country.Currency));
            return GetRoundedAmount(totalAmount);
        }

        public int GetTotalSoldBooks()
        {
            var invoices = _repository.GetInvoiceMap().Values;
            var totalSoldBooks = invoices
                .Sum(invoice => invoice.PurchasedBooks.Sum(purchasedBook => purchasedBook.Quantity));

            return totalSoldBooks;
        }

        private double GetRoundedAmount(double totalAmount) => Math.Round(totalAmount, 2);

        public long GetNumberOfIssuedInvoices() => _repository.GetInvoiceMap().Count;
    }
}
