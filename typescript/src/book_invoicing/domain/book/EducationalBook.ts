import {Language} from "@app/domain/country/Language";
import {Author} from "@app/domain/book/Author";
import {Book} from "@app/domain/book/Book";
import {Category} from "@app/domain/book/Category";
import hash from "hash-it";
import equal = require("fast-deep-equal");

export class EducationalBook implements Book {
  readonly name: string;
  readonly price: number;
  readonly author: Author;
  readonly language: Language;
  readonly category: Category;

  public constructor(
    name: string,
    price: number,
    author: Author,
    language: Language,
    category: Category
  ) {
    this.name = name;
    this.price = price;
    this.author = author;
    this.language = language;
    this.category = category;
  }

  equals(other: any): boolean {
    return equal(this, other);
  }
  hashCode(): number {
    return hash(this);
  }
}
