package main

import "fmt"

func main() {
	var countryMap map[string]string

	countryMap = make(map[string]string)

	countryMap["Brasil"] = "America do sul"
	countryMap["Canada"] = "America do norte"
	countryMap["Egito"] = "Africa"
	countryMap["Russia"] = "Europa"

	for country := range countryMap {
		fmt.Println("The country:", country, "is in the region:", countryMap[country])
	}

}
