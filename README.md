# Python REST API Project

This project demonstrates Python REST API capabilities.

### Install Virtual Environment
1. Execute following command to create new virtual environment (**Mandatory**)
    ```
    sudo  pip install virtualenv
    ``` 
2. Then execute below command to create new **venv** folder (You can use any name)that stores libraries
    ```
    virtualenv venv
    ```
3. Then execute below command to activate the Python Shell
    ``` 
    source venv/bin/activate
    ```
### Set up DB
1. Configure DB credentials [here](com/demo/dao/CustomerDao.py)
2. And create database **employees** and table **customers** with the following commands
```
create database if not exists employees;
create table if not exists employees.customers
(
	name varchar(40) null,
	address varchar(200) null
);
```

## Run project
4. Go to [com/demo/web/CustomersController.py](com/demo/web/CustomersController.py) and run the project
5. Go to http://127.0.0.1:5000 to see list of customers
6. Create new customer using the URL http://127.0.0.1:5000/create 
