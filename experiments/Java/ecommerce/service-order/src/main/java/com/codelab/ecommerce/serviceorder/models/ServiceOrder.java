package com.codelab.ecommerce.serviceorder.models;

import java.io.Serializable;
import java.time.OffsetDateTime;

import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@RedisHash("ServiceOrder")
public class ServiceOrder implements Serializable{

    private static final long serialVersionUID = 1L;

    @Id
    private String uuid;
    private String name;
    private String email;
    private String phone;
    private String productId;
    private int quantity;
    private String status;
    private OffsetDateTime createdAt;

    public ServiceOrder() {
        
    }

    public ServiceOrder(String uuid, String name, String email, String phone, String productId, int quantity, String status, OffsetDateTime createdAt) {
        this.uuid = uuid;
        this.name = name;
        this.email = email;
        this.phone = phone;
        this.productId = productId;
        this.quantity = quantity;
        this.status = status;
        this.createdAt = createdAt;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public OffsetDateTime getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(OffsetDateTime createdAt) {
        this.createdAt = createdAt;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getProductId() {
        return productId;
    }

    public void setProductId(String productId) {
        this.productId = productId;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getUuid() {
        return uuid;
    }

    public void setUuid(String uuid) {
        this.uuid = uuid;
    }

}