package org.peaksys.gameoftechs.domain.book;

import org.peaksys.gameoftechs.domain.country.Country;

public record Author(
        String name,
        Country nationality
) { }
