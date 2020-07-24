package com.codelab.ecommerce.catalog.controllers;

import java.util.List;

import com.codelab.ecommerce.catalog.models.Product;
import com.codelab.ecommerce.catalog.models.ProductOrder;
import com.codelab.ecommerce.catalog.services.OrderSenderService;
import com.codelab.ecommerce.catalog.services.ProductsRestService;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.util.MultiValueMap;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

@Controller
public class CatalogController {

    @Autowired
    private ProductsRestService productsRestService;

    @Autowired
    private OrderSenderService orderSenderService;

    @GetMapping("/catalog")
    public String showCatalog(Model model) {
        List<Product> products = productsRestService.getProducts();

        model.addAttribute("products", products);

        return "catalog";
    }

    @GetMapping("/checkout/{uuid}")
    public String showCheckout(Model model, @PathVariable String uuid) {
        List<Product> products = productsRestService.getProducts();

        for (Product product : products) {
            if (product.getUuid().equalsIgnoreCase(uuid)) {
                model.addAttribute("product", product);
            }
        }

        return "checkout";
    }

    @PostMapping(value = "/order", consumes = MediaType.APPLICATION_FORM_URLENCODED_VALUE)
    public String create(Model model, @RequestBody MultiValueMap<String, String> formData) {
        ProductOrder productOrder = new ProductOrder();
        productOrder.setEmail(formData.getFirst("email"));
        productOrder.setQuantity(Integer.parseInt(formData.getFirst("quantity")));
        productOrder.setProductUuid(formData.getFirst("productUuid"));

        try {
            ObjectMapper objectMapper = new ObjectMapper();
            String message = objectMapper.writeValueAsString(productOrder);
            orderSenderService.send(message);

            List<Product> products = productsRestService.getProducts();
            model.addAttribute("products", products);
            
            return "catalog";

        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }
        
        return "error";
    }

}