package com.codelab.partymanager.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.codelab.partymanager.models.Guest;

public interface Guests extends JpaRepository<Guest, Long> {

}