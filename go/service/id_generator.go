package service

import "sync/atomic"

var currentID int64

func NextID() int64 {
	return atomic.AddInt64(&currentID, 1)
}
