package com.codelab.partymanager.controllers;

import com.codelab.partymanager.models.Guest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class GuestsController {

    @Autowired
    private com.codelab.partymanager.repository.Guests quests;

    @GetMapping("/guests")
    public ModelAndView Guests() {
        ModelAndView modelAndView = new ModelAndView("guests");

        modelAndView.addObject(new Guest());
        modelAndView.addObject("guests", this.quests.findAll());

        return modelAndView;
    }

    @PostMapping("/guests")
    public String Create(Guest guest) {
        this.quests.saveAndFlush(guest);
        return "redirect:/guests";
    }

}