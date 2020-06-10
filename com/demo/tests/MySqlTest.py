import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="bcmc1234",
    database="employees",
    auth_plugin="mysql_native_password"  # This line is optional, include if you SHA2 auth error
);

mycursor = mydb.cursor()

"""
#mycursor.execute("Create database employees");
#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
"""
try:
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
    print("Hello")


except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))

mycursor.execute("Select * from customers");
customers = mycursor.fetchall();
for customer in customers:
    print(customer);
