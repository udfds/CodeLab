package main

import "fmt"

func main() {
	var _array [10]int
	var index_i, index_j int

	for index_i = 0; index_i < 10; index_i++ {
		_array[index_i] = index_i + 100
	}

	for index_j = 0; index_j < 10; index_j++ {
		fmt.Printf("Element[%d] - Value: %d \n", index_j, _array[index_j])
	}
}
