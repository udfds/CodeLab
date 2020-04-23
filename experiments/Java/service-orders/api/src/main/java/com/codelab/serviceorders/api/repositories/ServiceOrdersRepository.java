package com.codelab.serviceorders.api.repositories;

import com.codelab.serviceorders.api.models.ServiceOrder;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ServiceOrdersRepository extends JpaRepository<ServiceOrder, Long>{

}