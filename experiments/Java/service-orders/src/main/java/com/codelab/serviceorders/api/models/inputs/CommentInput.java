package com.codelab.serviceorders.api.models.inputs;

import javax.validation.constraints.NotBlank;

public class CommentInput {

    @NotBlank
    private String message;

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

}