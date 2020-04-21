package com.codelab.ecommerce.catalog.controllers;

import java.util.List;

import com.codelab.ecommerce.catalog.models.Product;
import com.codelab.ecommerce.catalog.services.ProductsRestService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class CatalogController {

    @Autowired
    private ProductsRestService service;

    @GetMapping("/catalog")
    public String getCatalog(Model model) {
        List<Product> products = service.getProducts();

        model.addAttribute("products", products);
        
        return "catalog";
    }

}