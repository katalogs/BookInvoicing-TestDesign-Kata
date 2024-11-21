package org.peaksys.gameoftechs.domain.country;

public record Country(
        String name,
        Currency currency,
        Language language
) {
}
