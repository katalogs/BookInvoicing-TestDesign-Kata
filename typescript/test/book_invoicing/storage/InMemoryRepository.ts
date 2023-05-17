import {Repository} from "@app/storage/Repository";
import {Invoice} from "@app/purchase";
import * as Immutable from "immutable";

export class InMemoryRepository implements Repository {
  private readonly invoices = new Map<number, Invoice>();

  addInvoice(invoice: Invoice): void {
    this.invoices.set(invoice.id, invoice);
  }

  getInvoiceMap(): Immutable.Map<number, Invoice> {
    return Immutable.Map<number, Invoice>(this.invoices);
  }
}
