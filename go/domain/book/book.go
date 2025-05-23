package book

import (
	. "book_invoicing/domain/country"
	"bytes"
	"crypto/sha1"
	"encoding/gob"
	"reflect"
)

type Book interface {
	GetName() string
	GetPrice() float64
	GetAuthor() Author
	GetLanguage() Language
	Equals(other any) bool
	HashCode() int
}

type EducationalBook struct {
	Name     string
	Price    float64
	Author   Author
	Language Language
	Category Category
}

func NewEducationalBook(name string, price float64, author Author, language Language, category Category) *EducationalBook {
	return &EducationalBook{Name: name, Price: price, Author: author, Language: language, Category: category}
}

func (e EducationalBook) GetName() string       { return e.Name }
func (e EducationalBook) GetPrice() float64     { return e.Price }
func (e EducationalBook) GetAuthor() Author     { return e.Author }
func (e EducationalBook) GetLanguage() Language { return e.Language }

func (e EducationalBook) Equals(other any) bool {
	o, ok := other.(EducationalBook)
	if !ok {
		return false
	}
	return reflect.DeepEqual(e, o)
}

func (e EducationalBook) HashCode() int {
	var b bytes.Buffer
	enc := gob.NewEncoder(&b)
	_ = enc.Encode(e)
	hash := sha1.Sum(b.Bytes())
	return int(hash[0])
}

type Novel struct {
	Name     string
	Price    float64
	Author   Author
	Language Language
	Genres   map[int64]Genre
}

func NewNovel(name string, price float64, author Author, language Language, genres map[int64]Genre) *Novel {
	return &Novel{Name: name, Price: price, Author: author, Language: language, Genres: genres}
}

func (n Novel) GetName() string       { return n.Name }
func (n Novel) GetPrice() float64     { return n.Price }
func (n Novel) GetAuthor() Author     { return n.Author }
func (n Novel) GetLanguage() Language { return n.Language }

func (n Novel) Equals(other any) bool {
	o, ok := other.(Novel)
	if !ok {
		return false
	}
	return reflect.DeepEqual(n, o)
}

func (n Novel) HashCode() int {
	var b bytes.Buffer
	enc := gob.NewEncoder(&b)
	_ = enc.Encode(n)
	hash := sha1.Sum(b.Bytes())
	return int(hash[0])
}

func IsNovel(book Book) bool {
	_, ok := book.(Novel)
	return ok
}
