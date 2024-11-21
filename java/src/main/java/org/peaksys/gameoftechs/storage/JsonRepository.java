package org.peaksys.gameoftechs.storage;


import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.peaksys.gameoftechs.purchase.Invoice;

import java.io.File;
import java.io.IOException;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public final class JsonRepository implements Repository {
    private static final String REPOSITORY_FILE = "repository.json";
    private final Map<Integer, Invoice> invoiceMap;

    private static final ObjectMapper objectMapper = new ObjectMapper();

    public JsonRepository() {
        invoiceMap = new HashMap<>();
        loadJsonData(getJsonReader());
    }

    private File getJsonReader() {
        try {
            return Paths.get(this.getClass().getClassLoader().getResource(REPOSITORY_FILE).toURI()).toFile();
        } catch (Exception exp) {
            System.out.println("*********************WARNING*********************");
            System.out.printf("Error reading the file '%s'%s", REPOSITORY_FILE, ".\n");
            System.out.println(exp);
            System.out.println("*************************************************");
            System.out.println("\n\n");
        }
        System.exit(0);
        return null;
    }

    private void loadJsonData(File jsonReader) {
        try {
            List<Invoice> invoices = objectMapper.readValue(jsonReader, new TypeReference<List<Invoice>>() {});
            invoices.forEach(this::addInvoice);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public void addInvoice(Invoice invoice) {
        invoiceMap.put(invoice.getId(), invoice);
    }

    @Override
    public Map<Integer, Invoice> getInvoiceMap() {
        return invoiceMap;
    }
}
