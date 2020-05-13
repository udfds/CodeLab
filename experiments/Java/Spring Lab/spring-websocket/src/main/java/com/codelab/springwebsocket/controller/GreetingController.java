package com.codelab.springwebsocket.controller;

import com.codelab.springwebsocket.model.Message;
import com.codelab.springwebsocket.model.Greeting;

import java.util.concurrent.atomic.AtomicLong;

import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.handler.annotation.SendTo;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.util.HtmlUtils;

@Controller
public class GreetingController {

    private final AtomicLong counter = new AtomicLong();

    @MessageMapping("/hello")
    @SendTo("/topic/greetings")
    public Greeting greeting(Message message) throws Exception {
        Thread.sleep(1000);

        String name = HtmlUtils.htmlEscape(message.getValue());
        Greeting greeting = new Greeting("Hello, " + name + "!");

        return greeting;
    }

    @CrossOrigin(origins = "http://localhost:9000")
    @GetMapping("/greeting")
    public Greeting greetingCORS(@RequestParam(required = false, defaultValue = "World") String value) {
        return new Greeting(counter.incrementAndGet(), "Hello, " + value + "!");
    }

    @GetMapping("/greeting-javaconfig")
    public Greeting greetingWithJavaconfig(@RequestParam(required = false, defaultValue = "World") String value) {
        return new Greeting(counter.incrementAndGet(), "Hello, " + value + "!");
    }
}