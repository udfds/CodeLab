package com.codelab.ecommerce.catalog;

import org.springframework.amqp.core.Queue;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.web.client.RestTemplate;

@SpringBootApplication
public class CatalogApplication {

	@Value("${queue.order.name}")
	private String orderQueue;
	
	public static void main(String[] args) {
		SpringApplication.run(CatalogApplication.class, args);
	}

	@Bean
	public RestTemplate getRestTemplate() {
	   return new RestTemplate();
	}
	 
    @Bean
    public Queue queue() {
        return new Queue(orderQueue, true);
	}
	
}
