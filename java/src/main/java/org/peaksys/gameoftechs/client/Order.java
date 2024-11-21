package org.peaksys.gameoftechs.client;

import org.peaksys.gameoftechs.domain.book.Book;
import org.peaksys.gameoftechs.purchase.Invoice;

public sealed interface Order permits BooksOrder {
    void addBook(Book book, int quantity);

    Invoice checkOut();

    Integer getQuantityOf(Book book);
}
