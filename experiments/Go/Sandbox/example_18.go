package main

import (
	"fmt"
	"math"
)

type Shape interface {
	area() float64
}

type Circle struct {
	x, y, radius float64
}

type Rectangle struct {
	width, height float64
}

func (circle Circle) area() float64 {
	return math.Pi * circle.radius * circle.radius
}

func (rectangle Rectangle) area() float64 {
	return rectangle.width * rectangle.width
}

func getArea(shape Shape) float64 {
	return shape.area()
}

func main() {
	circle := Circle{x: 1, y: 1, radius: 6}
	rectangle := Rectangle{width: 11, height: 6}

	fmt.Println("Circle area:", getArea(circle))
	fmt.Println("Rectangle area:", getArea(rectangle))
}
