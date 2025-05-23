package country

type Currency int

const (
	Dollar Currency = iota
	AustralianDollar
	Euro
	PoundSterling
	Yen
	Renminbi
)

func (c Currency) String() string {
	return [...]string{
		"Dollar",
		"AustralianDollar",
		"Euro",
		"PoundSterling",
		"Yen",
		"Renminbi",
	}[c]
}
