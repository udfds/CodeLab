package main

import "fmt"

func main() {
	var result_max = max(100, 200)
	var swap_1, swap_2 = swap("Hello", "world!")

	fmt.Printf("The max value from (100, 200) is: %d\n", result_max)
	fmt.Printf("The swap from 'Hello word!' is: '" + swap_1 + " " + swap_2 + "'")
}

func max(number_1 int, number_2 int) int {
	if (number_1 > number_2) {
		return number_1
	} else {
		return number_2
	}
}

func swap(value_1 string, value_2 string) (string, string) {
	return value_2, value_1
}