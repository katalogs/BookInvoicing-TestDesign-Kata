package country

type Language int

const (
	English Language = iota
	French
	Spanish
	Japanese
	Mandarin
	Arabic
	German
)

func (l Language) String() string {
	return [...]string{
		"English",
		"French",
		"Spanish",
		"Japanese",
		"Mandarin",
		"Arabic",
		"German",
	}[l]
}
