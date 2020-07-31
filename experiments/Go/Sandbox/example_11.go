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

	PrintBook1(book1)
	fmt.Println("-")
	PrintBook2(&book2)
	fmt.Println("-")

}

func PrintBook1(book Books) {
	fmt.Println("Book1.title =", book.title)
	fmt.Println("Book1.author =", book.author)
	fmt.Println("Book1.subject =", book.subject)
}

func PrintBook2(book *Books) {
	fmt.Println("Book2.title =", book.title)
	fmt.Println("Book2.author =", book.author)
	fmt.Println("Book2.subject =", book.subject)
}
