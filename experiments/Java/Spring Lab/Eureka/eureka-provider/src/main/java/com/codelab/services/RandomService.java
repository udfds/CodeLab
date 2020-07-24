package com.codelab.services;

import java.util.Arrays;
import java.util.List;
import java.util.Random;

import org.springframework.stereotype.Service;

@Service
public class RandomService {

    private final List<String> messages = Arrays.asList("Hi", "Hello", "Hey", "Ciao!");

    public String getMessage() {
       Random random = new Random();
       
       int index = random.nextInt(messages.size());

       return messages.get(index);
    }
}