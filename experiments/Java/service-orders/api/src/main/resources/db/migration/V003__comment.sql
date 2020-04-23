create table comment (
    id bigint not null auto_increment,
    service_order_id bigint not null,
    message text not null,
    created_at datetime not null,

    primary key (id)
);

alter table comment add constraint fk_comment_service_order
	foreign key (service_order_id) references service_order (id);