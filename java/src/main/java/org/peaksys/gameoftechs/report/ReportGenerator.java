package org.peaksys.gameoftechs.report;

import org.peaksys.gameoftechs.MainRepository;
import org.peaksys.gameoftechs.finance.CurrencyConverter;
import org.peaksys.gameoftechs.purchase.Invoice;
import org.peaksys.gameoftechs.purchase.PurchasedBook;
import org.peaksys.gameoftechs.storage.Repository;

import java.util.List;
import java.util.Map;

public class ReportGenerator {

    private final Repository repository = MainRepository.configuredRepository();

    public double getTotalAmount() {
        Map<Integer, Invoice> invoiceMap = repository.getInvoiceMap();

        var totalAmount = invoiceMap
                .values()
                .stream()
                .mapToDouble(invoice -> CurrencyConverter.toUSD(invoice.computeTotalAmount(), invoice.getCountry().currency()))
                .sum();
        return getRoundedAmount(totalAmount);
    }

    private double getRoundedAmount(double totalAmount) {
        return Math.round(totalAmount * 100.0) / 100.0;
    }

    public int getTotalSoldBooks() {
        Map<Integer, Invoice> invoiceMap = repository.getInvoiceMap();
        return invoiceMap
                .values()
                .stream()
                .flatMap(invoice -> invoice.getPurchasedBooks().stream())
                .mapToInt(PurchasedBook::quantity)
                .sum();
    }

    public long getNumberOfIssuedInvoices() {
        Map<Integer, Invoice> invoiceMap = repository.getInvoiceMap();
        return invoiceMap.values().size();
    }
}
