package com.codelab.serviceorders.api.services;

import java.util.List;

import com.codelab.serviceorders.api.models.Client;
import com.codelab.serviceorders.api.repositories.ClientRepository;
import com.codelab.serviceorders.api.utils.ModelException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class ClientsService {

    @Autowired
    private ClientRepository clientRepository;

    public List<Client> list() {
        return clientRepository.findAll();
    }

    public Client get(Long id) {
        return clientRepository.findById(id).orElse(null);
    }

    public Client save(Client draftClient) {
        Client client = clientRepository.findByEmail(draftClient.getEmail());

        if (client != null && client.getId() != draftClient.getId()) {
            throw new ModelException("Email in use by another client");
        }

        return clientRepository.save(draftClient);
    }

    public void delete(Long id) {
        clientRepository.deleteById(id);
    }
    
}