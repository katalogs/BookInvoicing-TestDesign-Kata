package org.peaksys.gameoftechs.purchase;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.EqualsAndHashCode;
import lombok.ToString;
import org.peaksys.gameoftechs.IdGenerator;
import org.peaksys.gameoftechs.domain.country.Country;
import org.peaksys.gameoftechs.finance.TaxRule;

import java.beans.ConstructorProperties;
import java.util.ArrayList;
import java.util.List;

@ToString
@EqualsAndHashCode
public final class Invoice {
    @ToString.Include
    @EqualsAndHashCode.Include
    private final int id;
    @ToString.Include
    @EqualsAndHashCode.Include
    private final String clientName;
    @ToString.Include
    @EqualsAndHashCode.Include
    private final List<PurchasedBook> purchasedBooks;
    @ToString.Include
    @EqualsAndHashCode.Include
    private final Country country;

    public Invoice(String clientName, Country country) {
        this(IdGenerator.nextId(), clientName, country);
    }

    @ConstructorProperties({"id", "client", "country"})
    public Invoice(int id, String clientName, Country country) {
        this.id = id;
        this.clientName = clientName;
        this.country = country;
        this.purchasedBooks = new ArrayList<>();
    }

    public int getId() {
        return id;
    }

    public String getClientName() {
        return clientName;
    }

    public Country getCountry() {
        return country;
    }

    @JsonProperty("booksInBasket")
    public void addPurchasedBooks(List<PurchasedBook> books) {
        purchasedBooks.addAll(books);
    }

    public void addPurchasedBook(PurchasedBook book) {
        this.purchasedBooks.add(book);
    }

    public double computeTotalAmount() {
        return purchasedBooks.stream()
                .mapToDouble(purchasedBook -> purchasedBook.getTotalPrice() * TaxRule.getApplicableRate(country, purchasedBook.book()))
                .sum();
    }

    public List<PurchasedBook> getPurchasedBooks() {
        return purchasedBooks;
    }

}
