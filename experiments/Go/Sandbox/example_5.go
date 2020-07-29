package main

import "fmt"

var global_variable = 10

func main() {
	var local_variable = 20

	fmt.Println("The value of global_variable is", global_variable)
	fmt.Println("The value of local_Variable is", local_variable)

	global_variable = local_variable
	fmt.Println("The value of global_variable, after set, is", global_variable)
}