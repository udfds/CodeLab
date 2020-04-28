package com.codelab.ecommerce.serviceorder.services;

import com.codelab.ecommerce.serviceorder.models.ServiceOrder;
import com.codelab.ecommerce.serviceorder.repositories.ServiceOrderRepository;
import com.fasterxml.jackson.databind.ObjectMapper;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;

@Service
public class ServiceOrderService {

    @Autowired
    ServiceOrderRepository serviceOrderRepository;

    @Autowired
    RedisTemplate<String, ServiceOrder> redisTemplate;

    public void saveServiceOrder(ServiceOrder serviceOrder) {
        try {
            redisTemplate.opsForHash().put("uuid", serviceOrder.getUuid(), serviceOrder);
        } catch (Exception exception) {
            exception.printStackTrace();
        }
    }

    public ServiceOrder findServiceOrder(String uuid) {
        Object object = redisTemplate.opsForHash().get("uuid", uuid);
        ServiceOrder serviceOrder = new ObjectMapper().convertValue(object, ServiceOrder.class);
        return serviceOrder;
    }
}