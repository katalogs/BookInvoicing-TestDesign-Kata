import {Book} from "@app/domain/book/Book";
import {Invoice} from "@app/purchase/Invoice";

export interface Order {
  addBook(book: Book, quantity: number): void;

  checkOut(): Invoice;

  getQuantityOf(book: Book): number;
}
