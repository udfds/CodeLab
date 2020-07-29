package main

import (
	"fmt"
	"strings"
)

func main() {
	var greeting = "Hello world!"
	var sampleText = "\xbd\xb2\x3d\xbc\x20\xe2\x8c\x98"

	fmt.Println("Normal string:")
	fmt.Printf("%s", greeting)
	fmt.Println("\n")

	fmt.Println("Hex bytes:")
	for index := 0; index < len(greeting); index++ {
		fmt.Printf("%x", greeting[index])
	}
	fmt.Println("\n")

	fmt.Println("Quoted string:")
	fmt.Printf("%q", sampleText)
	fmt.Println("\n")

	tokens := []string{"Hello", "world!"}
	fmt.Println("Join string:")
	fmt.Println(strings.Join(tokens, " "))
	fmt.Println("\n")
}
