import {Book} from "@app/domain/book";
import {Invoice, PurchasedBook} from "@app/purchase";
import {MainRepository} from "../MainRepository";
import {Client, Order} from ".";

export class BooksOrder implements Order {
  private readonly client: Client;
  private readonly booksInBasket = new Map<Book, number>();

  constructor(client: Client) {
    this.client = client;
  }

  addBook(book: Book, quantity: number): void {
    const alreadySold = this.booksInBasket.get(book) || 0;
    this.booksInBasket.set(book, alreadySold + quantity);
  }

  checkOut(): Invoice {
    const invoice = new Invoice(this.client.name, this.client.country);

    this.booksInBasket.forEach((quantity: number, book: Book) => {
      invoice.addPurchasedBook(new PurchasedBook(book, quantity));
    });
    MainRepository.configuredRepository().addInvoice(invoice);
    return invoice;
  }

  getQuantityOf(book: Book): number {
    return this.booksInBasket.get(book) || 0;
  }
}
