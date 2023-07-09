# database created#

create database master_db;

#using database#
use master_db;

#table employee creation

create table employee(
emp_id int ,
# add auto increment
emp_name varchar (30),
emp_password varchar (20),
emp_DOB varchar (10),
#change to date datatype
emp_phonenumber int unique key ,
emp_email varchar(50) unique key,
emp_data_of_joining  date ,
emp_department varchar(50),
emp_status char(10),
emp_access varchar(10),
primary key (emp_id)
);

# customer table creation#
create table customer
(
customer_id int ,
# add employee id
customer_name varchar(30),
customer_phone_number int unique key,
customer_email varchar(50) not null,
unique key(customer_email),
customer_city char(20),
customer_country char(20),
primary key (customer_id)
);

#Branch table #
create table branch
(
branch_id int,
# auto increment branch id
branch_name varchar(30),
branch_city varchar(20),
branch_country varchar(30),
branch_status char(20),
primary key(branch_id)
);

#products table #
create table product
(
product_id int ,
# auto increment 
product_name varchar(50),
product_description varchar(1000),
product_MRP int ,
product_sale_price int ,
# add least margin attribute
product_Tax int,
# rename tax attribute
product_quantity int ,
primary key (product_id)
);

#One more table need to be added 
#orders table#
create table orders
(
order_id int primary key auto_increment,
order_date date ,
Amount decimal(10,2),
quantity int ,
product_id int ,
customer_id int,
branch_id int ,
emp_id int,
constraint fk_employee foreign key (emp_id) references employee(emp_id),
constraint fk_customer foreign key(customer_id) references customer(customer_id),
constraint fk_branch foreign key (branch_id) references branch(branch_id),
constraint fk_product foreign key (product_id) references product(product_id)
);

-- Adding constraints foreign key to build relationship among multiple tables
alter table orders add constraint fk_product foreign key (product_id) references product (product_id);
alter table orders add constraint fk_customer foreign key (customer_id) references customer (customer_id);
alter table orders add constraint fk_branch foreign key (branch_id) references branch (branch_id);
alter table orders add constraint fk_emp foreign key (emp_id) references employee (emp_id);

insert into employee values(101,'ghouri','iam loverboy','17/06/1997',12345677,'masterghouri@mylove.com','2022-07-07','reinbazar','online','All');
insert into employee values(105,'alex','next buddy','12/06/1997',9988777,'levelbuddy@co.uk','2021-1-09','bazar','offline',' not All') ;
insert into branch values(111,'my branch','hyderabad','india','availabel') ;
insert into branch values(115,'second branch','london','united kingdom','partial availabel');
insert into customer values(100,'xyz',999888777,'hellomysqlworld@co.uk','london','united kingdom') ;
insert into customer values(999,'abc',888112578,'pythonprogrammingworld@gmail.com','new york','USA') ;
insert into product values(55,'hair brush','best hair comb in world!!',900,700,66,70);
insert into product values(11,'toys','toyworld',770,50,60,100);


select * from product;
select * from employee;
select * from customer;
select * from branch;

alter table orders modify order_id int auto_increment;

-- Inserting in orders table 
insert into orders (order_date,amount,quantity,product_id,customer_id,branch_id,emp_id) values('22-10-1',8000,50,11,100,115,105);

# performing join command to join multiple tables#

select * from orders o inner join product p 
on o.product_id=p.product_id 
inner join customer c on o.customer_id =c.customer_id 
inner join employee e on o.emp_id=e.emp_id
inner join branch b on o.branch_id = b.branch_id;

