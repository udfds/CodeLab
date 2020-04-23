package com.codelab.serviceorders.api.services;

import java.time.OffsetDateTime;
import java.util.List;

import com.codelab.serviceorders.api.exceptions.EntityNotFoundException;
import com.codelab.serviceorders.api.exceptions.ModelException;
import com.codelab.serviceorders.api.models.Client;
import com.codelab.serviceorders.api.models.Comment;
import com.codelab.serviceorders.api.models.ServiceOrder;
import com.codelab.serviceorders.api.models.enums.ServiceOrderStatus;
import com.codelab.serviceorders.api.repositories.CommentsRepository;
import com.codelab.serviceorders.api.repositories.ServiceOrdersRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class ServiceOrdersService {

    @Autowired
    private ServiceOrdersRepository serviceOrdersRepository;

    @Autowired
    private CommentsRepository commentsRepository;

    @Autowired
    private ClientsService clientsService;

    public List<ServiceOrder> getServiceOrders() {
        return serviceOrdersRepository.findAll();
    }

    public ServiceOrder getServiceOrder(Long id) {
        ServiceOrder serviceOrder = serviceOrdersRepository.findById(id).orElse(null);
        if (serviceOrder == null) {
            throw new EntityNotFoundException("ServiceOrder not found");
        }

        return serviceOrder;
    }

    public ServiceOrder createServiceOrder(ServiceOrder draftServiceOrder) {
        Client client = clientsService.get(draftServiceOrder.getClient().getId());
        if (client == null) {
            throw new EntityNotFoundException("Client not found");
        }

        draftServiceOrder.setClient(client);
        draftServiceOrder.setStatus(ServiceOrderStatus.OPENED);
        draftServiceOrder.setOpenDate(OffsetDateTime.now());
        draftServiceOrder.setCloseDate(null);

        return serviceOrdersRepository.save(draftServiceOrder);
    }

    public void deleteServiceOrder(Long id) {
        ServiceOrder serviceOrder = serviceOrdersRepository.findById(id).orElse(null);
        if (serviceOrder == null) {
            throw new EntityNotFoundException("ServiceOrder not found");
        }

        serviceOrdersRepository.deleteById(id);
    }
    
    public Comment commentServiceOrder(Long id, String message) {
        ServiceOrder serviceOrder = serviceOrdersRepository.findById(id).orElse(null);
        if (serviceOrder == null) {
            throw new EntityNotFoundException("ServiceOrder not found");
        }

        Comment comment = new Comment();
        comment.setMessage(message);
        comment.setServiceOrder(serviceOrder);
        comment.setCreatedAt(OffsetDateTime.now());

        return commentsRepository.save(comment);
    }

    public ServiceOrder closeServiceOrder(Long id) {
        ServiceOrder serviceOrder = serviceOrdersRepository.findById(id).orElse(null);
        if (serviceOrder == null) {
            throw new EntityNotFoundException("ServiceOrder not found");
        }

        if (serviceOrder.getStatus() == ServiceOrderStatus.CLOSED) {
            throw new ModelException("ServiceOder already closed");
        }

        if (serviceOrder.getStatus() == ServiceOrderStatus.CANCELLED) {
            throw new ModelException("ServiceOder already cancelled");
        }

        serviceOrder.setStatus(ServiceOrderStatus.CLOSED);
        serviceOrder.setCloseDate(OffsetDateTime.now());

        return serviceOrdersRepository.save(serviceOrder);
    }

    public ServiceOrder cancelServiceOrder(Long id) {
        ServiceOrder serviceOrder = serviceOrdersRepository.findById(id).orElse(null);
        if (serviceOrder == null) {
            throw new EntityNotFoundException("ServiceOrder not found");
        }

        if (serviceOrder.getStatus() == ServiceOrderStatus.CLOSED) {
            throw new ModelException("ServiceOder already closed");
        }

        if (serviceOrder.getStatus() == ServiceOrderStatus.CANCELLED) {
            throw new ModelException("ServiceOder already cancelled");
        }

        serviceOrder.setStatus(ServiceOrderStatus.CANCELLED);

        return serviceOrdersRepository.save(serviceOrder);
    }
}