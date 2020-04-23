package com.codelab.serviceorders.api.controllers;

import java.util.ArrayList;
import java.util.List;

import javax.validation.Valid;

import com.codelab.serviceorders.api.models.Client;
import com.codelab.serviceorders.api.models.inputs.ClientInput;
import com.codelab.serviceorders.api.models.outputs.ClientOutput;
import com.codelab.serviceorders.api.services.ClientsService;

import org.modelmapper.ModelMapper;
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
    private ClientsService clientService;

    @Autowired
    private ModelMapper modelMapper;

    @GetMapping
    public List<ClientOutput> getClients() {
        return toOutput(clientService.list());
    }

    @GetMapping("/{id}")
    public ResponseEntity<ClientOutput> getClient(@PathVariable Long id) {
        Client client = clientService.get(id);

        if (client == null) {
            return ResponseEntity.notFound().build();

        } else {
            return ResponseEntity.ok(toOutput(client));
        }
    }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public ClientOutput createClient(@Valid @RequestBody ClientInput clientInput) {
        Client client = fromInput(clientInput);

        client = clientService.save(client);

        return toOutput(client);
    }

    @PutMapping("/{id}")
    public ResponseEntity<ClientOutput> updateClient(@Valid @PathVariable Long id, @RequestBody ClientInput clientInput) {
        Client client = clientService.get(id);
        Client draftClient = fromInput(clientInput);

        if (client == null) {
            return ResponseEntity.notFound().build();

        } else {

            draftClient.setId(id);
            clientService.save(draftClient);

            return ResponseEntity.ok(toOutput(draftClient));
        }
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteClient(@PathVariable Long id) {
        Client client = clientService.get(id);

        if (client == null) {
            return ResponseEntity.notFound().build();

        } else {
            clientService.delete(id);

            return ResponseEntity.noContent().build();
        }
    }

    // --------------------------------------------------------------------
    // Private functions
    // --------------------------------------------------------------------

    private Client fromInput(ClientInput clientInput) {
        return modelMapper.map(clientInput, Client.class);
    }

    private ClientOutput toOutput(Client client) {
        return modelMapper.map(client, ClientOutput.class);
    }

    private List<ClientOutput> toOutput(List<Client> clients) {
        List<ClientOutput> serviceOrderOuts = new ArrayList<>();
        for (Client client : clients) {
            serviceOrderOuts.add(toOutput(client));
        }

        return serviceOrderOuts;
    }

}