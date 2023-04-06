package transport

import (
	"math/rand"
	"time"
)

func init() {
	rand.Seed(int64(time.Now().Nanosecond()))
}

func Shuffle(hosts []*StatefulHost) []*StatefulHost {
	if hosts == nil {
		return nil
	}
	shuffled := make([]*StatefulHost, len(hosts))
	for i, v := range rand.Perm(len(hosts)) {
		shuffled[i] = hosts[v]
	}
	return shuffled
}
