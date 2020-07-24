package com.codelab.serviceorders.api.services;

import java.util.List;

import com.codelab.serviceorders.api.exceptions.ModelException;
import com.codelab.serviceorders.api.models.Client;
import com.codelab.serviceorders.api.repositories.ClientsRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class ClientsService {

    @Autowired
    private ClientsRepository clientsRepository;

    public List<Client> list() {
        return clientsRepository.findAll();
    }

    public Client get(Long id) {
        return clientsRepository.findById(id).orElse(null);
    }

    public Client save(Client draftClient) {
        Client client = clientsRepository.findByEmail(draftClient.getEmail());

        if (client != null && client.getId() != draftClient.getId()) {
            throw new ModelException("Email in use by another client");
        }

        return clientsRepository.save(draftClient);
    }

    public void delete(Long id) {
        clientsRepository.deleteById(id);
    }
    
}