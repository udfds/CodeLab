package main

import "fmt"

type Books struct {
	title   string
	author  string
	subject string
}

func main() {
	var book1 Books
	book1.title = "title 1"
	book1.author = "author 1"
	book1.subject = "subject 1"

	var book2 Books
	book2.title = "title 2"
	book2.author = "author 2"
	book2.subject = "subject 2"

	fmt.Println("Book 1.title = ", book1.title)
	fmt.Println("Book 1.author = ", book1.author)
	fmt.Println("Book 1.subject = ", book1.subject)

	fmt.Println("-")

	fmt.Println("Book 2.title = ", book2.title)
	fmt.Println("Book 2.author = ", book2.author)
	fmt.Println("Book 2.subject = ", book2.subject)
}
