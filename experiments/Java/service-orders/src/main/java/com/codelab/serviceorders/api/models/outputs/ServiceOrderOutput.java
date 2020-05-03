package com.codelab.serviceorders.api.models.outputs;

import java.math.BigDecimal;
import java.time.OffsetDateTime;
import java.util.List;

import com.codelab.serviceorders.api.models.enums.ServiceOrderStatus;

public class ServiceOrderOutput {

    private Long id;
    private ClientOutput client;
    private String description;
    private BigDecimal price;
    private ServiceOrderStatus status;
    private OffsetDateTime openDate;
    private OffsetDateTime closeDate;
    private List<CommentOutput> comments;

    public List<CommentOutput> getComments() {
        return comments;
    }

    public void setComments(List<CommentOutput> comments) {
        this.comments = comments;
    }

    public ClientOutput getClient() {
        return client;
    }

    public void setClient(ClientOutput client) {
        this.client = client;
    }

    public OffsetDateTime getCloseDate() {
        return closeDate;
    }

    public void setCloseDate(OffsetDateTime closeDate) {
        this.closeDate = closeDate;
    }

    public OffsetDateTime getOpenDate() {
        return openDate;
    }

    public void setOpenDate(OffsetDateTime openDate) {
        this.openDate = openDate;
    }

    public ServiceOrderStatus getStatus() {
        return status;
    }

    public void setStatus(ServiceOrderStatus status) {
        this.status = status;
    }

    public BigDecimal getPrice() {
        return price;
    }

    public void setPrice(BigDecimal price) {
        this.price = price;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

}