drop database if exists money_planner;

create database money_planner;

use money_planner;

-- category Table
create table category(id INT(20) NOT NULL auto_increment, name varchar(100), PRIMARY KEY (id)) DEFAULT CHARSET=utf8;

-- Insert default values to category
LOCK TABLES category WRITE;
insert into category (name) values("Housing"), ("Food"), ("Insurance"), ("Medical Care"), ("Transportation"), ("Child Care"), 
                                  ("Income Taxes"),("Saving"),("Entertainment");
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

create table amount(id INT(100) NOT NULL auto_increment, amount_value INT(100), transaction_date date, description varchar(100), expense_id INT(50), FOREIGN KEY(expense_id) references expense(id), PRIMARY KEY(id)) DEFAULT CHARSET=utf8;


-- Create Budget_Type Table

create table budget_type(id INT(20) NOT NULL auto_increment PRIMARY KEY, set_budget varchar(100)) DEFAULT CHARSET=utf8;

-- Insert default budget_type
LOCK TABLES budget_type WRITE;
insert into budget_type (set_budget) values
            ("Monthly"),
            ("Yearly");
UNLOCK TABLES; 

-- Create Budget Table

create table budget(id INT(100) NOT NULL auto_increment PRIMARY KEY, budget_value INT(100), budget_type_id INT(20), FOREIGN KEY(budget_type_id) references budget_type(id)); 

-- Create Monthly Income Table

create table income(id INT(20) NOT NULL auto_increment PRIMARY KEY, source varchar(100), amount INT(100), month date) DEFAULT CHARSET=utf8;     

create table source(id INT(20) NOT NULL auto_increment PRIMARY KEY, name varchar(100)) DEFAULT CHARSET=utf8;

insert into source (name) values ("Income Source/Employer"),("Part Time"),("Retirement/Pension"),("Support from Family/Friends"); 

