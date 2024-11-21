package org.peaksys.gameoftechs.deserializer;

import com.fasterxml.jackson.core.JacksonException;
import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.databind.DeserializationContext;
import com.fasterxml.jackson.databind.JsonDeserializer;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;
import org.peaksys.gameoftechs.domain.book.Book;
import org.peaksys.gameoftechs.domain.book.EducationalBook;
import org.peaksys.gameoftechs.domain.book.Novel;
import org.peaksys.gameoftechs.purchase.PurchasedBook;

import java.io.IOException;

public class PurchasedBookDeserializer  extends JsonDeserializer<PurchasedBook> {
    @Override
    public PurchasedBook deserialize(JsonParser jsonParser, DeserializationContext deserializationContext) throws IOException, JacksonException {
        ObjectMapper mapper = (ObjectMapper) jsonParser.getCodec();

        JsonNode node = mapper.readTree(jsonParser);

        int quantity = node.get("quantity").asInt();
        ((ObjectNode) node).remove("quantity");

        Book book;
        if (node.has("category")) {
            book = mapper.treeToValue(node, EducationalBook.class);
        } else {
            book = mapper.treeToValue(node, Novel.class);
        }
        return new PurchasedBook(book, quantity);
    }
}
