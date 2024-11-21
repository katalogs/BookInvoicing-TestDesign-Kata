package org.peaksys.gameoftechs.storage;


import org.peaksys.gameoftechs.purchase.Invoice;

import java.util.Map;

public interface Repository {
    void addInvoice(Invoice invoice);

    Map<Integer, Invoice> getInvoiceMap();
}
