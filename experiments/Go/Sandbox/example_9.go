package main

import "fmt"

func main() {
	var a = 10
	var b = 'c'
	var c = "abc"
	var pointer *int
	var null_pointer *int

	fmt.Printf("Address of variable a is: %x \n", &a)
	fmt.Printf("Address of variable b is: %x \n", &b)
	fmt.Printf("Address of variable c is: %x \n", &c)

	fmt.Println("---")

	pointer = &a
	fmt.Printf("Address of variable pointer is: %x \n", &pointer)
	fmt.Printf("Address stored in pointer is: %x \n", pointer)
	fmt.Printf("Value of address stored in pointer is: %x \n", *pointer)

	fmt.Println("---")

	fmt.Printf("Address of variable null_pointer is: %x \n", &null_pointer)
	fmt.Printf("Address stored in null_pointer is: %x \n", null_pointer)

	if null_pointer != nil {
		fmt.Printf("Value of address stored in null_pointer is: %x \n", *null_pointer)
	} else {
		fmt.Println("Is not possible to display the value of address stored in null_pointer")
	}

	fmt.Println("---")
}
