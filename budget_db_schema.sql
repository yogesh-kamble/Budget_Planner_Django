drop database if exists money_planner;

create database money_planner;

use money_planner;

-- category Table
create table category(id INT(20) NOT NULL auto_increment, name varchar(100), PRIMARY KEY (id)) DEFAULT CHARSET=utf8;

-- Insert default values to category
LOCK TABLES category WRITE;
INSERT INTO `category` VALUES (1,'Housing'),(2,'Food'),(3,'Insurance'),(4,'Medical Care'),(5,'Transportation'),(6,'Child Care'),(7,'Income Taxes'),(8,'Saving'),(9,'Entertainment'),(11,'Shopping'),(12,'Vehicle Servicing'),(13,'Other');
UNLOCK TABLES;                                  

-- Expense Table
create table expense(id INT(50) NOT NULL auto_increment, name varchar(100), category_id INT(20), FOREIGN KEY (category_id) references category(id), PRIMARY KEY(id)) DEFAULT CHARSET=utf8;

-- Insert default values to expense
LOCK TABLES expense WRITE;
insert into expense (name,category_id) values
       ("Rent/Mortgage",1),
       ("Home Maintance",1),
       ("Gas/Electric",1),
       ("Water/Sewer/Garbage",1),
       ("Internet/Cable/Satellite",1),
       ("Landline/Cell Phone",1),
       ("Groceries/Household Items",2),
       ("Vehicle Payment",5),
       ("Gasoline/Oil",5);

UNLOCK TABLES;       

-- Create Amount table

create table amount(id INT(100) NOT NULL auto_increment, \
					amount_value INT(100), transaction_date date, \
					description varchar(100), category_id INT(50), \
					CONSTRAINT amount_fk_cat FOREIGN KEY(category_id) references category(id), \
					CONSTRAINT amount_pk PRIMARY KEY(id)) DEFAULT CHARSET=utf8;


-- Create Budget_Type Table

create table budget_type(id INT(20) NOT NULL auto_increment PRIMARY KEY, set_budget varchar(100)) DEFAULT CHARSET=utf8;

-- Insert default budget_type
LOCK TABLES budget_type WRITE;
insert into budget_type (set_budget) values
            ("Monthly"),
            ("Semi-Annually"),
            ("Annually");
UNLOCK TABLES; 

-- Create Budget Table
create table budget(id INT(100) NOT NULL auto_increment PRIMARY KEY, budget_value INT(100), budget_type_id INT(20), FOREIGN KEY(budget_type_id) references budget_type(id)); 

-- Add default income source
create table source(id INT(20) NOT NULL auto_increment PRIMARY KEY, name varchar(100)) DEFAULT CHARSET=utf8;

insert into source (name) values ("Income Source/Employer"),("Part Time"),("Retirement/Pension"),("Support from Family/Friends"),("Other");

-- create recurrence table
create table recurrence(id INT(20) NOT NULL auto_increment PRIMARY KEY, \
						recurrence_type varchar(20), \
						CONSTRAINT UNIQUE recurrence_type);

-- Insert Values to recurrence table
LOCK TABLES recurrence WRITE;
insert into recurrence(recurrence_type) values
			("One Time"),
			("Daily"),
			("Weekly"),
			("Monthly"),
			("Yearly");
UNLOCK TABLES;

-- Account need to be set up first after user registration.
create table account(id INT(20) NOT NULL auto_increment PRIMARY KEY, \
					 name varchar(20), \
					 balance INT(20)
					 CONSTRAINT UNIQUE KEY name);

-- Account Source Map table
create table account_source_map(id INT(20) NOT NULL auto_increment, source_id INT(20), account_id INT(20), \
								CONSTRAINT fk_sou FOREIGN KEY(source_id) references source(id),\
								CONSTRAINT fk_acc FOREIGN KEY(account_id) references account(id),\
								CONSTRAINT UNIQUE KEY (source_id, account_id), \
								CONSTRAINT acc_sou_red_pk PRIMARY KEY(id)) default charset=utf-8;

-- Create Income Table
create table income(id INT(20) NOT NULL auto_increment PRIMARY KEY, account_source_map_id INT(20), \
					amount INT(100), recurrence_id INT(20), income_date date, \
					CONSTRAINT fk_acc_sou FOREIGN KEY(account_source_map_id) references account_source_map(id), \
					CONSTRAINT fk_rec FOREIGN KEY(recurrence_id) references recurrence(id) 
					) DEFAULT CHARSET=utf8;

-- Create Net Worth Table
create table networth(id INT(20) NOT NULL auto_increment PRIMARY KEY, networth_value INT(100)); 

-- Create Currency Table
create table currency(id INT(20) NOT NULL auto_increment PRIMARY KEY, currency_type varchar(100)) DEFAULT CHARSET=utf8;

-- Insert Currency type
LOCK TABLES currency WRITE;
insert into currency(currency_type) values("Indian(INR)","US(Dollar)");
UNLOCK TABLES;

