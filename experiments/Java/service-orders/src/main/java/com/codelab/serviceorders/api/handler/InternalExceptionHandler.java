package com.codelab.serviceorders.api.handler;

import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.List;

import com.codelab.serviceorders.api.exceptions.EntityNotFoundException;
import com.codelab.serviceorders.api.exceptions.ModelException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.MessageSource;
import org.springframework.context.i18n.LocaleContextHolder;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.FieldError;
import org.springframework.validation.ObjectError;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.context.request.WebRequest;
import org.springframework.web.servlet.mvc.method.annotation.ResponseEntityExceptionHandler;

@ControllerAdvice
public class InternalExceptionHandler extends ResponseEntityExceptionHandler {

    @Autowired
    private MessageSource messageSource;

    @Override
    protected ResponseEntity<Object> handleMethodArgumentNotValid(MethodArgumentNotValidException ex,
            HttpHeaders headers, HttpStatus status, WebRequest request) {
        
        ObjectBodyAPI objectBody = new ObjectBodyAPI();
        objectBody.setStatus(status.value());
        objectBody.setMessage(ex.getClass().getName());
        objectBody.setDateTime(OffsetDateTime.now());

        List<ObjectErrorAPI> objectErrors = new ArrayList<ObjectErrorAPI>();

        for (ObjectError objectError : ex.getBindingResult().getAllErrors()) {
            String field = null;
            String message = null;

            if (objectError instanceof FieldError) {
                field = ((FieldError) objectError).getField();
                message = messageSource.getMessage(objectError, LocaleContextHolder.getLocale());

                objectErrors.add(new ObjectErrorAPI(field, message));
            }

        }

        objectBody.setFields(objectErrors);

        return super.handleExceptionInternal(ex, objectBody, headers, status, request);
    }

    @ExceptionHandler(ModelException.class)
    public ResponseEntity<Object> handlerModelException(ModelException ex, WebRequest request) {
        ObjectBodyAPI objectBody = new ObjectBodyAPI();
        objectBody.setStatus(HttpStatus.BAD_REQUEST.value());
        objectBody.setMessage(ex.getMessage());
        objectBody.setDateTime(OffsetDateTime.now());

        return super.handleExceptionInternal(ex, objectBody, new HttpHeaders(), HttpStatus.BAD_REQUEST, request);
    }

    @ExceptionHandler(EntityNotFoundException.class)
    public ResponseEntity<Object> handlerModelException(EntityNotFoundException ex, WebRequest request) {
        ObjectBodyAPI objectBody = new ObjectBodyAPI();
        objectBody.setStatus(HttpStatus.NOT_FOUND.value());
        objectBody.setMessage(ex.getMessage());
        objectBody.setDateTime(OffsetDateTime.now());

        return super.handleExceptionInternal(ex, objectBody, new HttpHeaders(), HttpStatus.NOT_FOUND, request);
    }

}