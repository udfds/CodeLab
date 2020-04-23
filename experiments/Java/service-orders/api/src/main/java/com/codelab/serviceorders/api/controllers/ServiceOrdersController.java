package com.codelab.serviceorders.api.controllers;

import java.util.ArrayList;
import java.util.List;

import javax.validation.Valid;

import com.codelab.serviceorders.api.models.Comment;
import com.codelab.serviceorders.api.models.ServiceOrder;
import com.codelab.serviceorders.api.models.inputs.CommentInput;
import com.codelab.serviceorders.api.models.inputs.ServiceOrderInput;
import com.codelab.serviceorders.api.models.outputs.CommentOutput;
import com.codelab.serviceorders.api.models.outputs.ServiceOrderOutput;
import com.codelab.serviceorders.api.services.ServiceOrdersService;

import org.modelmapper.ModelMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/serviceorders")
public class ServiceOrdersController {

    @Autowired
    private ServiceOrdersService serviceOrdersService;

    @Autowired
    private ModelMapper modelMapper;

    @GetMapping()
    public List<ServiceOrderOutput> getServiceOrders() {
        return toOutput(serviceOrdersService.getServiceOrders());
    }

    @GetMapping("/{id}")
    public ResponseEntity<ServiceOrderOutput> getServiceOrder(@PathVariable Long id) {
        ServiceOrder serviceOrder = serviceOrdersService.getServiceOrder(id);

        if (serviceOrder == null) {
            return ResponseEntity.notFound().build();

        } else {
            return ResponseEntity.ok(toOutput(serviceOrder));
        }
    }
    
    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public ServiceOrderOutput createServiceOrder(@Valid @RequestBody ServiceOrderInput serviceOrderInput) {
        ServiceOrder serviceOrder = fromInput(serviceOrderInput);

        serviceOrder = serviceOrdersService.createServiceOrder(serviceOrder);

        return toOutput(serviceOrder);
    }

    @GetMapping("/{id}/comments")
    public ResponseEntity<List<CommentOutput>> commentServiceOrder(@PathVariable Long id) {
        ServiceOrder serviceOrder = serviceOrdersService.getServiceOrder(id);
        
        ServiceOrderOutput serviceOrderOutput = toOutput(serviceOrder);

        return ResponseEntity.ok(serviceOrderOutput.getComments());
    }
    
    @PostMapping("/{id}/comments")
    public CommentOutput commentServiceOrder(@PathVariable Long id, @Valid @RequestBody CommentInput commentInput) {
        Comment comment = fromInput(commentInput);
        
        comment = serviceOrdersService.commentServiceOrder(id, comment.getMessage());
        
        return toOutput(comment);
    }

    @PostMapping("/{id}/close")
    public ServiceOrderOutput closeServiceOrder(@PathVariable Long id) {
        ServiceOrder serviceOrder = serviceOrdersService.closeServiceOrder(id);

        return toOutput(serviceOrder);
    }

    @PostMapping("/{id}/cancel")
    public ServiceOrderOutput cancelServiceOrder(@PathVariable Long id) {
        ServiceOrder serviceOrder = serviceOrdersService.cancelServiceOrder(id);

        return toOutput(serviceOrder);
    }

    // --------------------------------------------------------------------
    // Private functions
    // --------------------------------------------------------------------

    private ServiceOrder fromInput(ServiceOrderInput serviceOrderInput) {
        return modelMapper.map(serviceOrderInput, ServiceOrder.class);
    }

    private Comment fromInput(CommentInput commentInput) {
        return modelMapper.map(commentInput, Comment.class);
    }

    private ServiceOrderOutput toOutput(ServiceOrder serviceOrder) {
        return modelMapper.map(serviceOrder, ServiceOrderOutput.class);
    }

    private CommentOutput toOutput(Comment comment) {
        return modelMapper.map(comment, CommentOutput.class);
    }

    private List<ServiceOrderOutput> toOutput(List<ServiceOrder> serviceOrders) {
        List<ServiceOrderOutput> serviceOrderOuts = new ArrayList<>();
        for (ServiceOrder serviceOrder : serviceOrders) {
            serviceOrderOuts.add(toOutput(serviceOrder));
        }

        return serviceOrderOuts;
    }
}