package com.codelab.ecommerce.serviceorder.repositories;

import org.springframework.stereotype.Repository;
import com.codelab.ecommerce.serviceorder.models.ServiceOrder;
import org.springframework.data.repository.CrudRepository;

@Repository
public interface ServiceOrderRepository extends CrudRepository<ServiceOrder, String> {

}