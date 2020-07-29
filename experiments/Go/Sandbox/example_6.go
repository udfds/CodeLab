package main

import "fmt"

var variable_a = 100

func main() {
	var variable_a = 5
	var local_variable_b = 10
	var local_variable_c = 15

	fmt.Printf("value of local_variable_a in main() = %d\n", variable_a);
	local_variable_c = sum( variable_a, local_variable_b);
	fmt.Printf("value of c in main() = %d\n",  local_variable_c);
}

func sum(value_a int, value_b int) int {
	fmt.Printf("value of a in sum() = %d\n",  value_a);
	fmt.Printf("value of b in sum() = %d\n",  value_b);
 
	return value_a + value_b;
 }