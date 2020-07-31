package main

import "fmt"

func main() {
	var array = make([]int, 3, 5)

	fmt.Println("Array lenght:", len(array))
	fmt.Println("Array capacity:", cap(array))
	fmt.Println("Array slice:", array)

	fmt.Println("-")

	array = []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

	fmt.Println("Array lenght:", len(array))
	fmt.Println("Array capacity:", cap(array))
	fmt.Println("Array slice:", array)
	fmt.Println("Array subslicing:", array[4:8])
	fmt.Println("Array subslicing:", array[:6])

	fmt.Println("-")

	array = append(array, 10)
	array = append(array, 11)
	array = append(array, 12)

	fmt.Println("Array lenght:", len(array))
	fmt.Println("Array capacity:", cap(array))
	fmt.Println("Array slice:", array)
	fmt.Println("Array subslicing:", array[4:8])
	fmt.Println("Array subslicing:", array[:6])

	fmt.Println("-")

	new_array := make([]int, len(array), (cap(array))*2)

	fmt.Println("Array lenght:", len(new_array))
	fmt.Println("Array capacity:", cap(new_array))
	fmt.Println("Array slice:", new_array)
	fmt.Println("Array subslicing:", new_array[4:8])
	fmt.Println("Array subslicing:", new_array[:6])

	fmt.Println("-")

	copy(new_array, array)

	fmt.Println("Array lenght:", len(new_array))
	fmt.Println("Array capacity:", cap(new_array))
	fmt.Println("Array slice:", new_array)
	fmt.Println("Array subslicing:", new_array[4:8])
	fmt.Println("Array subslicing:", new_array[:6])
}
