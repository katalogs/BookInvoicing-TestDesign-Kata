package org.peaksys.gameoftechs.domain.book;


import com.fasterxml.jackson.annotation.JsonProperty;
import org.peaksys.gameoftechs.domain.country.Language;

import java.util.List;

public record Novel(
        String name,
        double price,
        Author author,
        Language language,
        @JsonProperty("genre")
        List<Genre> genres
) implements Book {
}
