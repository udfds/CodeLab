package com.codelab.serviceorders.api.controllers;

import java.util.List;

import com.codelab.serviceorders.api.models.Client;
import com.codelab.serviceorders.api.repositories.ClientRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/clients")
public class ClientsController {

    @Autowired
    private ClientRepository clientRepository;

    @GetMapping
    public List<Client> getClients() {
        List<Client> clients = clientRepository.findAll();

        return clients;
    }

    @GetMapping("/{id}")
    public ResponseEntity<Client> getClient(@PathVariable Long id) {
        Client client = clientRepository.findById(id).orElse(null);

        if (client == null) {
            return ResponseEntity.notFound().build();

        } else {
            return ResponseEntity.ok(client);
        }
    }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public Client createClient(@RequestBody Client client) {
        return clientRepository.save(client);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Client> updateClient(@PathVariable Long id, @RequestBody Client draftClient) {
        Client client = clientRepository.findById(id).orElse(null);

        if (client == null) {
            return ResponseEntity.notFound().build();

        } else {
            draftClient.setId(id);
            clientRepository.save(draftClient);

            return ResponseEntity.ok(draftClient);
        }
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteClient(@PathVariable Long id) {
        Client client = clientRepository.findById(id).orElse(null);

        if (client == null) {
            return ResponseEntity.notFound().build();

        } else {
            clientRepository.deleteById(id);

            return ResponseEntity.noContent().build();
        }
    }

}