import {ReportGenerator} from '@app/report/ReportGenerator';
import {MainRepository} from "@app/MainRepository";
import {Author, Category, EducationalBook} from "@app/domain/book";
import {Country, Currency, Language} from "@app/domain/country";
import {Invoice, PurchasedBook} from "@app/purchase";
import {InMemoryRepository} from "../storage/InMemoryRepository";

describe(ReportGenerator, () => {
    it("Computes total amount without discount and without tax rate", () => {
      const repository = new InMemoryRepository();
      MainRepository.override(repository);
      const generator = new ReportGenerator();

      const book = new EducationalBook(
          "Clean Code", 25, new Author(
              "Uncle Bob", new Country(
                  "USA", Currency.Dollar, Language.English
              )
          ), Language.English, Category.COMPUTER);

      const purchase = new PurchasedBook(book, 2);

      const invoice = new Invoice("John Doe", new Country("USA", Currency.Dollar, Language.English));
      invoice.addPurchasedBook(purchase);

      repository.addInvoice(invoice);

      expect(generator.getTotalAmount()).toBe(57.5);
      expect(generator.getNumberOfIssuedInvoices()).toBe(1);
      expect(generator.getTotalSoldBooks()).toBe(2);

      MainRepository.reset();
    });
});
