from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from wtforms import Form, validators, StringField

from com.demo.dao.CustomerDao import CustomerDao
# template folder location should be relevant to current file i.e. CustomersController.py
from com.demo.models.Customer import Customer

app = Flask(__name__, template_folder='../../../templates');
app.config.from_object(__name__);
#assets=Environment(app);
#js=Bundle('js/libraries/bootstrap.min.js','js/libraries/jquery-3.3.1.min.js', output='gen/packed.js');
#assets.register('js_all', js)

class ReusableForm(Form):
    name = StringField('name:', validators=[validators.required()])
    address=StringField('address:', validators=[validators.required()])

@app.route("/")
def home():
    return "Hello World";


@app.route("/showcustomers")
def getCustomers():
    customerDao = CustomerDao();
    return jsonify(customerDao.getCustomers());

@app.route("/customers")
def getCustomerPage():
    form = ReusableForm(request.form)
    return render_template("customers.html", form=form);

@app.route("/savecustomer",methods=['POST'])
def saveCustomer():
    if request.method=='POST':
        name=request.form['name'];
        address=request.form['address'];
        if name=='' or address=='':
            return "Customer data not saved. Name or Address is empty."
        customer=Customer(name,address);
        customerDao = CustomerDao();
        customerDao.insertRecord(customer);
    return "Customer Saved Successfully";

@app.route("/hello")
def getHello():
    return render_template("hello.html");

@app.route("/createcustomer")
def getSaveCustomerPage():
    form=ReusableForm(request.form)
    return render_template("createcustomer.html", form=form);


if __name__ == '__main__':
    app.run(debug=True);
