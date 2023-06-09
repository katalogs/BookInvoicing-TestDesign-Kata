import {Invoice} from "@app/purchase/Invoice";
import * as Immutable from "immutable";

export interface Repository {
  addInvoice(invoice: Invoice): void;

  getInvoiceMap(): Immutable.Map<number, Invoice>;
}
