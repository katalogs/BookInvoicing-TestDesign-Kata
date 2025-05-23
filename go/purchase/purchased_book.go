package purchase

import . "book_invoicing/domain/book"

type PurchasedBook struct {
	Book     Book
	Quantity int
}

func NewPurchasedBook(book Book, quantity int) PurchasedBook {
	return PurchasedBook{
		Book:     book,
		Quantity: quantity,
	}
}

func (pb PurchasedBook) TotalPrice() float64 {
	return pb.Book.GetPrice() * float64(pb.Quantity)
}
