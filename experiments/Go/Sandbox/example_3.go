package main

import "fmt"

func main() {
	var a, b, c = 3, 4.0, "foo"

	fmt.Println("The value of A is", a)
	fmt.Println("The value of B is", b)
	fmt.Println("The value of C is", c)
	fmt.Printf("The type of A is %T\n", a)
	fmt.Printf("The type of B is %T\n", b)
	fmt.Printf("The type of C is %T\n", c)
}