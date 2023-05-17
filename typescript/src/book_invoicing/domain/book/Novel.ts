import {Language} from "@app/domain/country/Language";
import {Author} from "@app/domain/book/Author";
import {Book} from "@app/domain/book/Book";
import {Genre} from "@app/domain/book/Genre";
import * as Immutable from "immutable";
import hash from "hash-it";
import equal = require("fast-deep-equal");

export function isNovel(book: Book): boolean {
  return (book as Novel).genres !== undefined;
}

export class Novel implements Book {
  readonly name: string;
  readonly price: number;
  readonly author: Author;
  readonly language: Language;
  readonly genres: Immutable.Set<Genre>;

  public constructor(
    name: string,
    price: number,
    author: Author,
    language: Language,
    genres: Immutable.Set<Genre>
  ) {
    this.name = name;
    this.price = price;
    this.author = author;
    this.language = language;
    this.genres = genres;
  }

  equals(other: any): boolean {
    return equal(this, other);
  }
  hashCode(): number {
    return hash(this);
  }
}
