package com.codelab.ecommerce.products.controllers;

import com.codelab.ecommerce.products.services.ProductsService;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ProductsController {

    @Autowired
    private ProductsService service;

    @RequestMapping(value="/products", method = RequestMethod.GET)
    public JSONArray getProducts() {
        return service.getProducts();
    }

    @RequestMapping(value="/products/{uuid}", method = RequestMethod.GET)
    public JSONObject getProduct(@PathVariable("uuid") String uuid) {
        return service.getProduct(uuid);
    }

}