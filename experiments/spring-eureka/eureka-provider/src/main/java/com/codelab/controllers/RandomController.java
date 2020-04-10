package com.codelab.controllers;

import com.codelab.services.RandomService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class RandomController {

    @Autowired
    private RandomService service;

    @GetMapping("/message")
    public String getMessage() {
        return service.getMessage();
    }
}