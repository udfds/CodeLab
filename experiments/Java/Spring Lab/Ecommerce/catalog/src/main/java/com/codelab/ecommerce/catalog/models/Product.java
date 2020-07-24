package com.codelab.ecommerce.catalog.models;

import com.fasterxml.jackson.annotation.JsonProperty;

import lombok.AllArgsConstructor;

@AllArgsConstructor
public class Product {

    @JsonProperty("uuid")
    private String uuid;

    @JsonProperty("product")
    private String name;

    @JsonProperty("price")
    private String price;

    public String getUuid() {
        return uuid;
    }

    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setUuid(String uuid) {
        this.uuid = uuid;
    }

}