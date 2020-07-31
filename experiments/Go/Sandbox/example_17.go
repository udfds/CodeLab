package main

import "fmt"

func main() {
	var sum int = 13
	var count int = 8
	var mean float32

	mean = float32(sum) / float32(count)
	fmt.Println("Mean =", mean)
}
