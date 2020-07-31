package main

import "fmt"

func main() {
	countryMap := map[string]string{"Brasil": "America do sul", "Mexico": "America do norte", "India": "Asia", "Australia": "Oceonia"}

	fmt.Println("Original map:")
	for country := range countryMap {
		fmt.Println("-- Country:", country, " - Region:", countryMap[country])
	}

	delete(countryMap, "India")

	fmt.Println("Updated map:")
	for country := range countryMap {
		fmt.Println("-- Country:", country, " - Region:", countryMap[country])
	}

}
