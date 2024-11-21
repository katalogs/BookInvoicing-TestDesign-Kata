package org.peaksys.gameoftechs.domain.book;

import org.peaksys.gameoftechs.domain.country.Language;

public record EducationalBook(
        String name,
        double price,
        Author author,
        Language language,
        Category category
) implements Book { }
