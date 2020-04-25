package com.codelab.ecommerce.serviceorder.repositories;

import com.codelab.ecommerce.serviceorder.models.ServiceOrder;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ServiceOrderRepository extends JpaRepository<ServiceOrder, Long> {

}