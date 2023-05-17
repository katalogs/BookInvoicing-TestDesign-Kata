import {Author} from "@app/domain/book/Author";
import {Language} from "@app/domain/country/Language";

export interface Book {
  readonly name: string;
  readonly price: number;
  readonly author: Author;
  readonly language: Language;

  equals(other: any): boolean;
  hashCode(): number;
}
