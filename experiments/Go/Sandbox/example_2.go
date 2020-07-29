package main

import "fmt"

func main() {
	var x float64

	x = 20.0
	y := 42

	fmt.Println("The value of X is", x)
	fmt.Println("The value of Y is", y)
	fmt.Printf("The type of X is %T\n", x)
	fmt.Printf("The type of Y is %T\n", y)
}