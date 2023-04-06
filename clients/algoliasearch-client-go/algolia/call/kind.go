package call

type Kind int

const (
	Read Kind = iota
	Write
)

func IsRead(k Kind) bool      { return k == Read }
func IsWrite(k Kind) bool     { return k == Write }
func IsReadWrite(k Kind) bool { return IsRead(k) || IsWrite(k) }
