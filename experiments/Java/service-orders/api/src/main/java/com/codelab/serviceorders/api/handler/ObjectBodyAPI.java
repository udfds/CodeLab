package com.codelab.serviceorders.api.handler;

import java.time.OffsetDateTime;
import java.util.List;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonInclude.Include;

@JsonInclude(Include.NON_NULL)
public class ObjectBodyAPI {

    private Integer status;
    private OffsetDateTime dateTime;
    private String message;
    private List<ObjectErrorAPI> fields;

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public OffsetDateTime getDateTime() {
        return dateTime;
    }

    public void setDateTime(OffsetDateTime dateTime) {
        this.dateTime = dateTime;
    }

    public Integer getStatus() {
        return status;
    }

    public void setStatus(Integer status) {
        this.status = status;
    }

    public List<ObjectErrorAPI> getFields() {
        return fields;
    }

    public void setFields(List<ObjectErrorAPI> fields) {
        this.fields = fields;
    }

}