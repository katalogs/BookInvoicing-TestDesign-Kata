package org.peaksys.gameoftechs.domain.book;

import org.peaksys.gameoftechs.domain.country.Language;

public sealed interface Book permits EducationalBook, Novel {

    String name();

    double price();

    Author author();

    Language language();
}
