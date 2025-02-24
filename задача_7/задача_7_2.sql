create table Authors (
    author_id serial primary key,
    first_name varchar(100) not null,
    last_name varchar(100) not null
);

create table Books (
    book_id serial primary key,
    title varchar(100) not null,
    year_published varchar(100) not null,
    price decimal(10,2) not null,
    author_id int not null,

    foreign key (author_id) references Authors(author_id) on delete cascade
);

create table Orders (
    order_id serial primary key,
    order_date date not null,
    total_amount decimal(10,2) not null
);