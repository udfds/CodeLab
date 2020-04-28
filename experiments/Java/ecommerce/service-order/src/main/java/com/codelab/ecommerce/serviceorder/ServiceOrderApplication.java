package com.codelab.ecommerce.serviceorder;

import com.codelab.ecommerce.serviceorder.services.OrderReceiverService;

import org.springframework.amqp.core.Binding;
import org.springframework.amqp.core.BindingBuilder;
import org.springframework.amqp.core.Queue;
import org.springframework.amqp.core.TopicExchange;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.data.redis.repository.configuration.EnableRedisRepositories;
import org.springframework.amqp.rabbit.connection.ConnectionFactory;
import org.springframework.amqp.rabbit.listener.SimpleMessageListenerContainer;
import org.springframework.amqp.rabbit.listener.adapter.MessageListenerAdapter;

@EnableRedisRepositories
@SpringBootApplication
public class ServiceOrderApplication {

	@Value("${queue.order.name}")
	private String topicExchange;

	@Value("${queue.order.name}")
	private String orderQueue;
	
	public static void main(String[] args) {
		SpringApplication.run(ServiceOrderApplication.class, args);
	}

	// -------------------------------------------------------------------------------------------
	// RabbitMQ
	// -------------------------------------------------------------------------------------------

	@Bean
    public Queue queue() {
        return new Queue(orderQueue, true);
	}
	
	@Bean
	public TopicExchange exchange() {
		return new TopicExchange(topicExchange);
	}

	@Bean
	Binding binding(Queue queue, TopicExchange exchange) {
	  return BindingBuilder.bind(queue).to(exchange).with("Ecommerce.ProductOrder");
	}

	@Bean
	SimpleMessageListenerContainer container(ConnectionFactory connectionFactory, 
		org.springframework.amqp.rabbit.listener.adapter.MessageListenerAdapter listenerAdapter) {

	  SimpleMessageListenerContainer container = new SimpleMessageListenerContainer();
	  container.setConnectionFactory(connectionFactory);
	  container.setQueueNames(orderQueue);
	  container.setMessageListener(listenerAdapter);

	  return container;
	}
  
	@Bean
	MessageListenerAdapter listenerAdapter(OrderReceiverService receiverService) {
	  return new MessageListenerAdapter(receiverService, "receiveMessage");
	}

}
