package com.codelab.ecommerce.serviceorder.services;

import java.util.UUID;

import com.codelab.ecommerce.serviceorder.models.ServiceOrder;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class OrderReceiverService {

    @Autowired
    ServiceOrderService serviceOrderService;

    public void receiveMessage(String message) {

        ServiceOrder serviceOrder = createServiceOrder(message);

        if (serviceOrder != null) {
            serviceOrderService.saveServiceOrder(serviceOrder);
            System.out.println(message);
        }
    }

    public ServiceOrder createServiceOrder(String json) {
        ServiceOrder serviceOrder = new ServiceOrder();
        ObjectMapper objectMapper = new ObjectMapper();

        try {
            String email = objectMapper.readTree(json).get("email").textValue();
            String productUuid = objectMapper.readTree(json).get("productUuid").textValue();
            int quantity = objectMapper.readTree(json).get("quantity").asInt();
            String uuid = UUID.randomUUID().toString().replace("-", "");

            serviceOrder.setUuid(uuid);
            serviceOrder.setEmail(email);
            serviceOrder.setProductId(productUuid);
            serviceOrder.setQuantity(quantity);

            return serviceOrder;

        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }

        return null;
    }

}