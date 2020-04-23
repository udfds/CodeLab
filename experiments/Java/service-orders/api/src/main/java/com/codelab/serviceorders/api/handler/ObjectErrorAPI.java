package com.codelab.serviceorders.api.handler;

public class ObjectErrorAPI {

    private String field;
    private String message;
    
    public ObjectErrorAPI(String field, String message) {
        this.field = field;
        this.message = message;
    }

	public String getField() {
        return field;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public void setField(String field) {
        this.field = field;
    }

}