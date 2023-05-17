import {Currency} from "@app/domain/country/Currency";
import {Language} from "@app/domain/country/Language";

export class Country {
  readonly name: string;
  readonly currency: Currency;
  readonly language: Language;

  public constructor(name: string, currency: Currency, language: Language) {
    this.name = name;
    this.currency = currency;
    this.language = language;
  }
}
