package com.codelab.serviceorders.api.exceptions;

public class EntityNotFoundException extends ModelException {

    private static final long serialVersionUID = 1L;

    public EntityNotFoundException(String message) {
        super(message);
    }
    
}