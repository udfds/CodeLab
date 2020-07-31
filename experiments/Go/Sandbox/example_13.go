package main

import "fmt"

func main() {
	// Slice-Range
	numbers := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	for index := range numbers {
		fmt.Println("Number:", numbers[index])
	}
	fmt.Println("-")

	// Map-Hash
	regions := map[string]string{"Norte": "N", "Oeste": "O", "Leste": "L", "Sul": "S"}
	for region := range regions {
		fmt.Println("Region ", region, " is ", regions[region])
	}
	fmt.Println("-")

	for key, value := range regions {
		fmt.Println("Key:", key, "Value:", value)
	}

}
