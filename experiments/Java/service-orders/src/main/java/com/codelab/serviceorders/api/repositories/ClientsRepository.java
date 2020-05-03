package com.codelab.serviceorders.api.repositories;

import java.util.List;

import com.codelab.serviceorders.api.models.Client;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ClientsRepository extends JpaRepository<Client, Long> {

    List<Client> findByName(String name);

    Client findByEmail(String name);
    
}