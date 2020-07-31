package main

import (
	"errors"
	"fmt"
	"math"
)

func SquareRoot(value float64) (float64, error) {
	if value < 0 {
		return 0, errors.New("Math: valor não pode ser menor que zero")
	}

	return math.Sqrt(value), nil
}

func main() {
	result, error := SquareRoot(-1)
	if error != nil {
		fmt.Println(error)
	} else {
		fmt.Println("Raiz quadrada de -1 é:", result)
	}

	result, error = SquareRoot(16)
	if error != nil {
		fmt.Println(error)
	} else {
		fmt.Println("Raiz quadrada de 16 é:", result)
	}
}
