package org.peaksys.gameoftechs.purchase;

import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import org.peaksys.gameoftechs.deserializer.PurchasedBookDeserializer;
import org.peaksys.gameoftechs.domain.book.Book;

@JsonDeserialize(using = PurchasedBookDeserializer.class)
public record PurchasedBook(
        Book book,
        int quantity
) {

    public double getTotalPrice() {
        return book.price() * quantity;
    }
}
