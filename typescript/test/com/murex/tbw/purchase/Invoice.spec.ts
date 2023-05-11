import {Invoice} from "../../../../../src/com/murex/tbw/purchase/Invoice";
import {Author, Genre, Novel} from '../../../../../src/com/murex/tbw/domain/book';
import {Country, Currency, Language} from '../../../../../src/com/murex/tbw/domain/country';
import {PurchasedBook} from '../../../../../src/com/murex/tbw/purchase';
import {Set} from "immutable";

describe(Invoice, () => {
    it("should apply tax rules when computing total amount",
      () => {
        const book = new Novel(
            "Beautiful novel", 50, new Author(
                "An author", new Country(
                    "USA", Currency.Dollar, Language.English
                )
            ), Language.English, Set.of(Genre.MYSTERY));

        const purchase = new PurchasedBook(book, 1);

        const invoice = new Invoice(
            "John Doe",
            new Country("USA", Currency.Dollar, Language.English)
        );
        invoice.addPurchasedBook(purchase);

        expect(invoice.computeTotalAmount()).toBe(56.35)
      });
});
