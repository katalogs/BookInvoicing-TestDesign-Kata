package org.peaksys.gameoftechs.client;

import org.peaksys.gameoftechs.MainRepository;
import org.peaksys.gameoftechs.domain.book.Book;
import org.peaksys.gameoftechs.purchase.Invoice;
import org.peaksys.gameoftechs.purchase.PurchasedBook;

import java.util.HashMap;
import java.util.Map;

public final class BooksOrder implements Order {
    private final Map<Book, Integer> booksInBasket;
    private final Client client;

    public BooksOrder(Client client) {
        this.client = client;
        booksInBasket = new HashMap<>();
    }

    @Override
    public void addBook(Book book, int quantity) {
        booksInBasket.putIfAbsent(book, 0);
        booksInBasket.put(book, booksInBasket.get(book) + quantity);
    }

    @Override
    public Invoice checkOut() {
        Invoice invoice = new Invoice(client.name(), client.country());
        booksInBasket.forEach((book, quantity) -> invoice.addPurchasedBook(new PurchasedBook(book, quantity)));
        MainRepository.configuredRepository().addInvoice(invoice);
        return invoice;
    }

    @Override
    public Integer getQuantityOf(Book book) {
        return booksInBasket.getOrDefault(book, 0);
    }
}
