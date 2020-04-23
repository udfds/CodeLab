package com.codelab.serviceorders.api.beans;

import org.modelmapper.ModelMapper;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class ModelMapperBuilder {

    @Bean
    public ModelMapper modelMapperAPI() {
        return new ModelMapper();
    }

}