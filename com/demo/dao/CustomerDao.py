import mysql.connector


class CustomerDao:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            port=33061,
            password="Test@2020",
            database="employees"
        );
        self.mycursor = self.mydb.cursor();

    def insertRecord(self, customer):
        try:
            mydb = self.mydb;
            mycursor = self.mycursor;
            sql = "INSERT INTO customers (name, address) VALUES (%s, %s)";
            values = (customer.name, customer.address);
            mycursor.execute(sql, values);
            mydb.commit();
            print(mycursor.rowcount, "Record Inserted");

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

    def insertRecords(self):
        try:
            mydb = self.mydb;
            mycursor = self.mycursor;
            sql = "INSERT INTO customers (name, address) VALUES (%s, %s)";
            values = val = [
                ('Peter', 'Lowstreet 4'),
                ('Amy', 'Apple st 652'),
                ('Hannah', 'Mountain 21'),
                ('Michael', 'Valley 345'),
                ('Sandy', 'Ocean blvd 2'),
                ('Betty', 'Green Grass 1'),
                ('Richard', 'Sky st 331'),
                ('Susan', 'One way 98'),
                ('Vicky', 'Yellow Garden 2'),
                ('Ben', 'Park Lane 38'),
                ('William', 'Central st 954'),
                ('Chuck', 'Main Road 989'),
                ('Viola', 'Sideway 1633')
            ]
            mycursor.executemany(sql, values);
            mydb.commit();
            print(mycursor.rowcount, "Records Inserted");


        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

    def getCustomers(self):
        mycursor = self.mycursor;
        mycursor.execute("Select * from customers");
        customers = mycursor.fetchall();
        for customer in customers:
            print(customer);
        return customers;

    def createDatabase(self):
        self.mycursor.execute("Create database employees");

    def createTable(self):
        self.mycursor.execute("""create table if not exists employees.customers
                                (
                                    name varchar(40) null,
                                    address varchar(200) null
                                );
                                """);
