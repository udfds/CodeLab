package com.codelab.ecommerce.catalog.services;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import com.codelab.ecommerce.catalog.models.Product;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class ProductsRestService {

    @Autowired
    RestTemplate restTemplate;

    private String serviceURI = "http://127.0.0.1:8081/products";

    public List<Product> getProducts() {
        String url = this.serviceURI;
        ResponseEntity<Product[]> response = restTemplate.getForEntity(url, Product[].class);

        List<Product> products = new ArrayList<Product>();
        if (response.getBody() != null) {
            products = Arrays.asList(response.getBody());
        }
        
        return products;
    }

    public Product getProduct(String uuid) {
        String url = this.serviceURI + "/{uuid}";
        ResponseEntity<Product> response = restTemplate.getForEntity(url, Product.class, uuid);

        return response.getBody();
    }

}